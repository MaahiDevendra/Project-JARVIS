# Project JARVIS

Project JARVIS is a local-first personal AI assistant project. The current codebase is an early foundation for a voice-enabled assistant that runs on a developer workstation, favors local models and local data, and keeps external dependencies explicit.

The project is currently centered on:

- A local language-model direction using Hermes through Ollama.
- A Piper-based text-to-speech voice engine.
- A Git-tracked, open-source-friendly project structure.
- A hearing module stub that is ready for speech-to-text work.

This repository is not yet a complete assistant. It is a production-minded first implementation scaffold.

## Philosophy

- Local-first by default.
- User-owned memory and configuration.
- Clear boundaries between brain, voice, hearing, dashboard, memory, and skills.
- Small, auditable modules before broad automation.
- No hidden cloud dependency unless explicitly added and documented.

## Current Status

Implemented:

- `voice.engine.speak(text)`: generates speech with Piper and plays the resulting WAV file on Windows.
- `test_voice.py`: simple voice test entry point.
- Bundled Piper runtime under `voice/piper/`.
- Piper model files under `voice/models/`.
- Empty module areas for future brain, dashboard, memory, and skills work.
- `core/hearing.py` placeholder for the hearing pipeline.

In progress:

- Hearing / speech-to-text module.
- Hermes + Ollama integration layer.
- Assistant orchestration loop.
- Memory and skill interfaces.

## Repository Layout

```text
Project-JARVIS/
  brain/             # Future reasoning and assistant orchestration
  core/              # Core assistant modules, including hearing
  dashboard/         # Future local UI
  docs/              # Project documentation
  memory/            # Future local memory storage
  skills/            # Future assistant skills and tools
  voice/             # Piper voice runtime, models, and voice engine
  test_voice.py      # Manual voice test
```

## Requirements

Current known requirements:

- Windows
- Python 3
- Piper runtime included in `voice/piper/`
- Piper voice model included in `voice/models/`
- Ollama for the planned Hermes local LLM layer

## Quick Start

From the project root:

```powershell
python test_voice.py
```

This should synthesize and play:

```text
Welcome back, Sir. Let's start building.
```

Generated audio files are ignored by Git.

## Development Notes

- Keep new functionality local-first unless the project explicitly documents otherwise.
- Prefer small modules with clear responsibilities.
- Do not commit generated audio, caches, secrets, or machine-local configuration.
- Update `ARCHITECTURE.md` when adding new subsystems.
- Update `AI_INSTRUCTIONS.md` when changing assistant behavior or project rules.

## Roadmap

See `ROADMAP.md`.

## License

Placeholder: add license before public release.
