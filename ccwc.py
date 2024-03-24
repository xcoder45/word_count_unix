import sys

def count_bytes(file):
    byte_count = len(file.read())
    return byte_count

def count_lines(file):
    line_count = sum(1 for line in file)
    return line_count

def count_words(file):
    word_count = sum(len(line.split()) for line in file)
    return word_count

def count_characters(file):
    character_count = sum(len(line) for line in file)
    return character_count

def main():
    if len(sys.argv) == 1:
        file = sys.stdin
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        file = open(filename, 'r', encoding='utf-8')
    else:
        print("Usage: python ccwc.py [filename]")
        sys.exit(1)

    try:
        byte_count = count_bytes(file)
        line_count = count_lines(file)
        word_count = count_words(file)
        character_count = count_characters(file)

        print("Byte count:", byte_count)
        print("Line count:", line_count)
        print("Word count:", word_count)
        print("Character count:", character_count)

    finally:
        if file is not sys.stdin:
            file.close()

if __name__ == "__main__":
    main()
