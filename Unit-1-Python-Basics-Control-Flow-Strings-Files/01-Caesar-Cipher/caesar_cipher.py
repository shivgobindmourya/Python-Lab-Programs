import sys


def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decode":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        else:
            # Keep spaces, numbers and special characters unchanged
            result += char

    return result


def main():
    print("------ Caesar Cipher ------")

    # Get input from command line or prompt
    if len(sys.argv) >= 4:
        text = sys.argv[1]
        shift_input = sys.argv[2]
        mode = sys.argv[3].lower()
    else:
        text = input("Enter the message: ")
        shift_input = input("Enter shift key: ")
        mode = input("Enter mode (encode/decode): ").lower()

    # Validate shift key
    if not shift_input.isdigit():
        print("Error: Shift key must be an integer.")
        return

    shift = int(shift_input)

    # Validate mode
    if mode not in ("encode", "decode"):
        print("Error: Mode must be 'encode' or 'decode'.")
        return

    # Normalize shift
    shift %= 26

    result = caesar_cipher(text, shift, mode)

    print("\nOriginal :", text)
    print("Shift    :", shift)
    print("Mode     :", mode)
    print("Result   :", result)


if __name__ == "__main__":
    main()