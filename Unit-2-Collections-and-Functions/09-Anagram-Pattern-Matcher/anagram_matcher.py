# Program: Anagram Detection and Matching Tool

import re
from collections import Counter


# Function 1: Clean text by removing spaces and punctuation
def clean_text(text):
    return re.sub(r"[^a-zA-Z0-9]", "", text).lower()


# Function 2: Check anagrams using sorting
def are_anagrams_sorting(word1, word2):
    word1 = clean_text(word1)
    word2 = clean_text(word2)

    if not word1 or not word2:
        return False

    return sorted(word1) == sorted(word2)


# Function 3: Check anagrams using dictionary counting
def are_anagrams_counting(word1, word2):
    word1 = clean_text(word1)
    word2 = clean_text(word2)

    if not word1 or not word2:
        return False

    if len(word1) != len(word2):
        return False

    return Counter(word1) == Counter(word2)


# Function 4: Generate an immutable tuple key
def create_anagram_key(text):
    cleaned = clean_text(text)

    if not cleaned:
        return ()

    character_count = Counter(cleaned)

    return tuple(sorted(character_count.items()))


# Function 5: Group anagrams using dictionary lookup
def group_anagrams(words):
    groups = {}

    for word in words:
        key = create_anagram_key(word)

        if not key:
            print(f"Skipping invalid or empty input: {word!r}")
            continue

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return groups


# Main program
print("========== ANAGRAM DETECTION TOOL ==========")

while True:
    print("\n1. Check Two Words")
    print("2. Find Anagrams in a List")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        word1 = input("Enter the first word or phrase: ")
        word2 = input("Enter the second word or phrase: ")

        if not clean_text(word1) or not clean_text(word2):
            print("Please enter valid, non-empty text.")
            continue

        print("\n========== ANAGRAM RESULTS ==========")

        if are_anagrams_sorting(word1, word2):
            print("Result using sorting: They are anagrams.")
        else:
            print("Result using sorting: They are not anagrams.")

        if are_anagrams_counting(word1, word2):
            print("Result using dictionary counting: They are anagrams.")
        else:
            print("Result using dictionary counting: They are not anagrams.")

        print("First word key:", create_anagram_key(word1))
        print("Second word key:", create_anagram_key(word2))

    elif choice == "2":
        text = input("Enter words or phrases separated by commas: ")

        words = [word.strip() for word in text.split(",")]

        groups = group_anagrams(words)

        print("\n========== ANAGRAM GROUPS ==========")

        found = False

        for group in groups.values():
            if len(group) > 1:
                print(group)
                found = True

        if not found:
            print("No anagram pairs found.")

    elif choice == "3":
        print("Exiting Anagram Detection Tool. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")

