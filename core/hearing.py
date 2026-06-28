from __future__ import annotations

import wave
from pathlib import Path
from typing import Optional

import sounddevice as sd
from faster_whisper import WhisperModel

try:
    import ctranslate2
except ImportError:  # pragma: no cover - faster-whisper normally installs this.
    ctranslate2 = None


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RECORDING_PATH = PROJECT_ROOT / "recording.wav"
DEFAULT_MODEL_SIZE = "base"
DEFAULT_SAMPLE_RATE = 16_000
DEFAULT_DURATION_SECONDS = 5

_model: Optional[WhisperModel] = None
_model_device: Optional[str] = None


def prefer_cuda_device() -> str:
    """Return cuda when available, otherwise return cpu."""
    if ctranslate2 is None:
        return "cpu"

    try:
        return "cuda" if ctranslate2.get_cuda_device_count() > 0 else "cpu"
    except Exception:
        # If CUDA probing fails for any reason, keep the hearing path usable.
        return "cpu"


def load_model(model_size: str = DEFAULT_MODEL_SIZE) -> WhisperModel:
    """Load the Faster-Whisper model once and reuse it across transcriptions."""
    global _model, _model_device

    if _model is not None:
        return _model

    device = prefer_cuda_device()
    compute_type = "float16" if device == "cuda" else "int8"

    try:
        _model = WhisperModel(model_size, device=device, compute_type=compute_type)
        _model_device = device
    except Exception:
        # Some machines report CUDA but cannot actually run it. Fall back to CPU.
        if device == "cuda":
            _model = WhisperModel(model_size, device="cpu", compute_type="int8")
            _model_device = "cpu"
        else:
            raise

    return _model


def record_microphone(
    output_path: Path | str = DEFAULT_RECORDING_PATH,
    duration_seconds: int = DEFAULT_DURATION_SECONDS,
    sample_rate: int = DEFAULT_SAMPLE_RATE,
) -> Path:
    """Record audio from the default microphone and save it as a WAV file."""
    output_path = Path(output_path)

    # Use mono 16-bit PCM because it is simple, portable, and Whisper-friendly.
    audio = sd.rec(
        int(duration_seconds * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16",
    )
    sd.wait()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(output_path), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio.tobytes())

    return output_path


def transcribe_audio(audio_path: Path | str) -> str:
    """Transcribe an audio file with the cached Faster-Whisper model."""
    model = load_model()
    segments, _info = model.transcribe(str(audio_path), beam_size=5)

    # Faster-Whisper streams segments lazily, so join them into one clean string.
    return " ".join(segment.text.strip() for segment in segments).strip()


def listen_once(
    output_path: Path | str = DEFAULT_RECORDING_PATH,
    duration_seconds: int = DEFAULT_DURATION_SECONDS,
) -> str:
    """Record once from the microphone, transcribe the result, and return text."""
    recording_path = record_microphone(
        output_path=output_path,
        duration_seconds=duration_seconds,
    )
    return transcribe_audio(recording_path)


def get_model_device() -> Optional[str]:
    """Expose the active model device for diagnostics and future UI status."""
    return _model_device
