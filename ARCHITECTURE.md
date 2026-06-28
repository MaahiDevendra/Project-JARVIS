# Architecture

Project JARVIS is organized as a local-first assistant with separate modules for reasoning, hearing, speaking, memory, skills, and user interface work. The implementation is early, so this document describes both the current repo and the intended boundaries.

## Current System Snapshot

```text
User
  |
  | manual Python call
  v
test_voice.py
  |
  v
voice.engine.speak(text)
  |
  v
Piper executable + local ONNX voice model
  |
  v
speech.wav -> Windows audio playback
```

The only implemented runtime path today is text-to-speech. The hearing, reasoning, memory, dashboard, and skills areas are present as project boundaries but are not yet complete.

## Modules

### `voice/`

Status: implemented first draft.

Responsibilities:

- Convert assistant text into spoken audio.
- Use the bundled Piper executable.
- Use the local `en_US-hfc_male-medium.onnx` voice model.
- Write generated speech to `voice/speech.wav`.
- Play the generated audio through Windows sound playback.

Current entry point:

- `voice.engine.speak(text: str)`

### `core/`

Status: in progress.

Responsibilities:

- Hold core assistant runtime modules that do not belong to a specific interface.
- Provide the future hearing pipeline.

Current files:

- `core/hearing.py`: placeholder for speech-to-text / microphone input work.

### `brain/`

Status: placeholder.

Intended responsibilities:

- Coordinate assistant reasoning.
- Connect to the local Hermes model through Ollama.
- Manage prompts, turns, and response routing.

No committed implementation exists yet.

### `memory/`

Status: placeholder.

Intended responsibilities:

- Store local assistant memory.
- Keep user-owned state on disk.
- Provide clear read/write behavior and future migration paths.

No committed implementation exists yet.

### `skills/`

Status: placeholder.

Intended responsibilities:

- Contain locally auditable assistant capabilities.
- Keep integrations modular.
- Avoid hidden side effects.

No committed implementation exists yet.

### `dashboard/`

Status: placeholder.

Intended responsibilities:

- Provide a local UI for status, interaction, configuration, and debugging.

No committed implementation exists yet.

## Local LLM Direction

The project is intended to use Hermes through Ollama for local inference. The integration layer has not yet been committed in this repository. When added, it should remain isolated behind a small interface so the assistant can change models without rewriting the rest of the system.

Expected boundary:

```text
brain/
  local_model_client -> Ollama -> Hermes
```

## Data Flow Target

Planned assistant loop:

```text
Microphone
  -> core.hearing
  -> brain orchestration
  -> Ollama / Hermes
  -> voice.engine
  -> Speaker
```

Memory and skills should be explicit participants in this loop, not hidden global behavior.

## Persistence

Current persistence:

- Generated audio at `voice/speech.wav`.
- Git-tracked source and bundled voice assets.

Planned persistence:

- Local memory files under `memory/`.
- Local configuration files, format to be decided.

## Security and Privacy

- Default to local execution.
- Document every network dependency before adding it.
- Keep secrets out of Git.
- Treat microphone input, memory, and transcripts as sensitive user data.
- Prefer transparent file formats for local state.

## Open Architecture Questions

- Which speech-to-text engine should power `core/hearing.py`?
- What shape should the Ollama client interface take?
- What memory format should be used first: JSON, SQLite, or another local store?
- How should skills declare permissions and side effects?
- What dashboard framework, if any, best fits the local-first goal?
