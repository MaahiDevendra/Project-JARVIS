from core.hearing import DEFAULT_RECORDING_PATH, get_model_device, listen_once


def main() -> None:
    # This manual smoke test records from the default microphone for 5 seconds.
    print("JARVIS Hearing Test")
    print(f"Recording to: {DEFAULT_RECORDING_PATH}")
    print("Listening for 5 seconds...")

    text = listen_once()

    print(f"Whisper device: {get_model_device() or 'not loaded'}")
    print(f"Recognized text: {text}")


if __name__ == "__main__":
    main()
