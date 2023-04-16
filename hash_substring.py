# python3
from hashlib import sha1

def read_input():
    # this function needs to acquire input both from keyboard and file
    input_type = input("Enter 'I' for input from keyboard or 'F' for input from file: ").upper().strip()
    if input_type == 'I':
        return (input().rstrip(), input().rstrip())
    elif input_type == 'F':
        file_name = input("Enter the file name: ").strip()
        with open(file_name, "r") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
            return (pattern, text)
    else:
        raise ValueError("Invalid input type")

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def hash_function(s):
    return int(sha1(s.encode()).hexdigest(), 16)

def get_occurrences(pattern, text):
    # this function should find the occurrences using Rabin Karp algorithm
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = hash_function(pattern)
    text_hash = hash_function(text[:pattern_len])
    occurrences = []

    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash:
            if text[i:i+pattern_len] == pattern:
                occurrences.append(i)
        if i < text_len - pattern_len:
            text_hash = hash_function(text[i+1:i+1+pattern_len])

    return occurrences

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


