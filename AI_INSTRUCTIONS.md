# AI Instructions

These instructions define how AI contributors should work inside Project JARVIS.

## Project Identity

Project JARVIS is a local-first personal AI assistant. Treat it as a production-quality open-source project, even while the implementation is early.

Do not describe unimplemented features as complete. It is acceptable to document planned modules, but label them clearly as placeholders, planned, or in progress.

## Current Implementation Facts

The current repository includes:

- Piper text-to-speech integration in `voice/engine.py`.
- A local Piper voice model in `voice/models/`.
- Bundled Piper runtime files in `voice/piper/`.
- A voice smoke test in `test_voice.py`.
- An empty hearing module at `core/hearing.py`.
- Placeholder directories for `brain`, `dashboard`, `docs`, `memory`, and `skills`.
- Git project tracking.

The project direction includes Hermes through Ollama for local LLM inference, but the committed integration layer is not yet present.

## Development Principles

- Preserve the local-first philosophy.
- Keep modules small and auditable.
- Prefer explicit interfaces over hidden global behavior.
- Avoid unnecessary cloud dependencies.
- Do not commit secrets, credentials, transcripts, generated audio, caches, or local machine configuration.
- Update documentation when behavior or architecture changes.
- Keep generated files out of source control unless they are required project assets.

## Coding Guidelines

- Use clear Python modules and functions.
- Keep side effects obvious at module boundaries.
- Prefer standard library functionality where it is sufficient.
- Use dependency wrappers for external tools such as Piper and Ollama.
- Handle platform-specific behavior intentionally and document it.
- Add tests or smoke checks for user-visible behavior.

## Voice Guidelines

The current voice system uses Piper.

When changing voice behavior:

- Keep model paths configurable or clearly centralized.
- Do not overwrite source assets.
- Keep generated audio ignored by Git.
- Avoid blocking playback changes unless the calling code expects them.

## Hearing Guidelines

`core/hearing.py` is in progress.

When implementing hearing:

- Treat microphone input and transcripts as sensitive.
- Prefer local speech-to-text options.
- Keep capture, transcription, and wake/listen logic separate.
- Add clear failure behavior when no microphone or model is available.

## Brain / LLM Guidelines

The intended local model path is Hermes through Ollama.

When implementing the brain layer:

- Put Ollama-specific code behind a small client interface.
- Keep prompts versioned or easy to inspect.
- Avoid hard-coding model names outside configuration.
- Make failures understandable when Ollama is not running or the model is unavailable.
- Do not add hosted AI APIs unless explicitly approved and documented.

## Memory Guidelines

Memory is not implemented yet.

When adding memory:

- Store data locally by default.
- Make the storage format inspectable.
- Separate short-term session state from long-term memory.
- Provide deletion and reset paths early.

## Documentation Rules

- Keep README instructions accurate and runnable.
- Keep `ARCHITECTURE.md` aligned with real module boundaries.
- Keep `ROADMAP.md` honest about what is done, in progress, and planned.
- Add placeholders for future sections instead of inventing completed features.

## Placeholder

Future maintainers should add:

- Contribution guidelines.
- Test strategy.
- Release process.
- Security policy.
- Model configuration reference.
