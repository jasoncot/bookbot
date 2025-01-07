def count_characters(text):
    map = {}
    for char in text.lower():
        if not char in letters_in_sequence():
            continue

        if not char in map:
            map[char] = 0
        map[char] += 1
    return map


def break_into_words(text):
    return text.split()

def read_file(filename):
    file_contents = None

    with open(filename) as f:
        file_contents = f.read()

    return file_contents

def letters_in_sequence():
    return 'abcdefghijklmnopqrstuvwxyz'

def letters_by_occurance(map):
    list_of_pairs = []
    for key in map:
        list_of_pairs.append((map[key], key))
    list_of_pairs.sort(key=lambda pair: pair[0], reverse=True)

    sorted_keys = []
    for key in list_of_pairs:
        sorted_keys.append(key[1])

    return sorted_keys

def print_report(filename):
    file_contents = read_file(filename)
    if file_contents == None:
        raise Exception(f"unable to open file {filename}")
    
    word_count = len(break_into_words(file_contents))
    char_map = count_characters(file_contents)

    print(f"--- begin report of {filename} ---")
    print(f"{word_count} words found in the document")
    print("")
    for char in letters_by_occurance(char_map):
        print(f"The '{char}' character was found {char_map[char]} times")
    print("--- End report ---")
    

def main():
    print_report("./books/frankenstein.txt")

main()