from pathlib import Path
import subprocess

BASE_DIR = Path(__file__).parent

PIPER = BASE_DIR / "piper" / "piper.exe"
MODEL = BASE_DIR / "models" / "en_US-hfc_male-medium.onnx"
OUTPUT = BASE_DIR / "speech.wav"


def speak(text: str):
    subprocess.run(
        [
            str(PIPER),
            "--model",
            str(MODEL),
            "--output_file",
            str(OUTPUT),
        ],
        input=text,
        text=True,
        check=True,
    )

    subprocess.run(
        [
            "powershell",
            "-c",
            f'(New-Object Media.SoundPlayer "{OUTPUT}").PlaySync()'
        ],
        check=True,
    )