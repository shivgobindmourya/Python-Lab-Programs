import string
from collections import Counter


def clean_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Clean extra whitespace
    text = " ".join(text.split())

    return text


def analyze_text(text):
    cleaned_text = clean_text(text)

    # Split text into words
    words = cleaned_text.split()

    # Total word count
    total_words = len(words)

    # Frequency table
    frequency = Counter(words)

    # Find palindromes
    palindromes = sorted(set(
        word for word in words
        if len(word) > 1 and word == word[::-1]
    ))

    print("\n===== TEXT ANALYSIS REPORT =====")
    print("Total Words:", total_words)

    print("\nPalindromes:")
    if palindromes:
        for word in palindromes:
            print("-", word)
    else:
        print("No palindromes found.")

    print("\nWord Frequency:")
    print("-------------------------")
    print(f"{'Word':<20} {'Count':<10}")
    print("-------------------------")

    for word, count in frequency.most_common():
        print(f"{word:<20} {count:<10}")

    print("-------------------------")


def main():
    print("===== Text Analyzer =====")
    print("1. Enter text manually")
    print("2. Read text from a file")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        print("\nEnter your text.")
        print("Type 'END' on a new line to finish:")

        lines = []

        while True:
            line = input()

            if line == "END":
                break

            lines.append(line)

        text = "\n".join(lines)

    elif choice == "2":
        filename = input("Enter file name: ")

        try:
            with open(filename, "r", encoding="utf-8") as file:
                text = file.read()

        except FileNotFoundError:
            print("Error: File not found.")
            return

        except PermissionError:
            print("Error: Permission denied.")
            return

    else:
        print("Invalid choice.")
        return

    if not text.strip():
        print("Error: No text provided.")
        return

    analyze_text(text)


if __name__ == "__main__":
    main()