#Keita Matvijuka 13. Grupa 221RDB506

import sys

def acquire_input():
    user_input = input().strip().upper()
    if user_input == "I":
        pattern = input().strip()
        text = input().strip()
    elif user_input == "F":
        filename = 'tests/06'
        try:
            with open(filename) as file:
                pattern = file.readline().strip()
                text = file.readline().strip()
        except FileNotFoundError:
            print("Error: file not found")
            sys.exit(1)
    else:
        print("Error: invalid input choice")
        sys.exit(1)
    return user_input, pattern, text

def display_occurrences(output):
    print(' '.join(map(str, output)))

def find_occurrences(user_input, pattern, text):
    text_len = len(text)
    pattern_len = len(pattern)
    prime = 31
    prime_powers = [pow(prime, i) for i in range(pattern_len)]
    pattern_hash_value = sum([ord(pattern[i]) * prime_powers[pattern_len - 1 - i] for i in range(pattern_len)])
    text_hash_value = sum([ord(text[i]) * prime_powers[pattern_len - 1 - i] for i in range(pattern_len)])
    matched_positions = []

    for i in range(text_len - pattern_len + 1):
        if pattern_hash_value == text_hash_value:
            if pattern == text[i:i + pattern_len]:
                matched_positions.append(i)
        if i < text_len - pattern_len:
            text_hash_value = (text_hash_value - ord(text[i]) * prime_powers[pattern_len - 1]) * prime + ord(text[i + pattern_len])

    return matched_positions

if __name__ == '__main__':
    display_occurrences(find_occurrences(*acquire_input()))
