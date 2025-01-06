def count_characters(text):
    map = {}
    for char in text.lower():
        if not char in map:
            map[char] = 0
        map[char] += 1
    return map


def break_into_words(text):
    return text.split()

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print(len(break_into_words(file_contents)))
        print(count_characters(file_contents))

main()