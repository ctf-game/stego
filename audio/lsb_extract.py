import wave
import sys

def display_help():
    print("Usage: python script.py <audio_file>")
    print("Decode the hidden message from a wav file by extracting LSB.")

def extract_message_from_audio(file_path):
    song = wave.open(file_path, mode='rb')
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    string = "".join(chr(int("".join(map(str, extracted[i:i+8])), 2)) for i in range(0, len(extracted), 8))
    decoded = string.split("###")[0]
    song.close()
    return decoded

def main():
    if len(sys.argv) != 2:
        display_help()
        sys.exit(1)

    audio_file = sys.argv[1]
    try:
        decoded_message = extract_message_from_audio(audio_file)
        print("Successfully decoded:", decoded_message)
    except Exception as e:
        print(f"Error: {e}")
        display_help()

if __name__ == "__main__":
    main()
