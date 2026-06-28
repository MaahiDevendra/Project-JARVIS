# Roadmap

This roadmap tracks the path from the current voice-first scaffold toward a local-first personal assistant. Items are intentionally scoped to avoid overstating the current implementation.

## Current Baseline

Done:

- Project structure created.
- Git tracking initialized.
- Piper runtime and voice model present in the repository.
- `voice.engine.speak(text)` implemented.
- `test_voice.py` voice smoke test added.
- Generated WAV files ignored by Git.
- Documentation first drafts added.

In progress:

- Hearing module scaffold at `core/hearing.py`.
- Local LLM direction using Hermes through Ollama.

## Phase 1: Stabilize Voice Foundation

- Make voice paths configurable.
- Add basic error messages for missing Piper executable or model files.
- Add a non-interactive voice smoke test option.
- Decide whether generated audio should always use one fixed file or temporary files.
- Document supported operating systems.

## Phase 2: Add Hearing

- Choose a local speech-to-text engine.
- Implement microphone capture in `core/hearing.py`.
- Separate audio capture from transcription.
- Add clear failure handling for missing microphones or models.
- Add a manual hearing test script.

## Phase 3: Add Local Brain Layer

- Add an Ollama client wrapper.
- Configure Hermes as the first local model target.
- Add a simple text-in / text-out assistant loop.
- Route model responses to the Piper voice engine.
- Handle Ollama unavailable, model missing, and timeout states cleanly.

## Phase 4: Assistant Loop

- Connect hearing -> brain -> voice.
- Add a local configuration file.
- Add session logging with privacy controls.
- Keep all transcripts and state local by default.
- Add interrupt / stop behavior for long responses.

## Phase 5: Memory

- Define memory requirements and boundaries.
- Choose an initial local storage format.
- Implement short-term session memory.
- Add opt-in long-term memory.
- Add delete, export, and reset operations.

## Phase 6: Skills

- Define a skill interface.
- Add permission and side-effect conventions.
- Implement one small local skill as a reference.
- Document how skills are discovered and executed.

## Phase 7: Dashboard

- Decide whether the dashboard should be web-based, desktop-based, or CLI-first.
- Show assistant status, model status, voice status, and recent local activity.
- Add configuration controls for model, voice, and privacy settings.

## Phase 8: Project Hardening

- Add automated tests for core modules.
- Add setup instructions for a clean machine.
- Add contribution guidelines.
- Add a license.
- Add security and privacy documentation.
- Prepare an initial tagged release.

## Future Ideas

Placeholder for ideas that should not be treated as committed scope:

- Wake word support.
- Multiple voices.
- Local tool execution policies.
- Offline package setup.
- Plugin-style skill distribution.
