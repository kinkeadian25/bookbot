import sys

def main():
    text = read_book("books/frankenstein.txt")
    word_count = get_word_count(text)
    print(word_count)
    char_counts = count_per_char(text)
    print(char_counts)
    full_book_report(char_counts, word_count)
    
def full_book_report(char_counts, word_count):
    sorted_chars = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    sorted_char_dict = dict(sorted_chars)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    for k, v in sorted_char_dict.items():
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")

def count_per_char(text):
    char_counts = {}
    low_text = text.lower()
    for c in low_text:
        if c.isalpha():
            if c in char_counts:
                char_counts[c] += 1
            else:
                char_counts[c] = 1

    return char_counts

def get_word_count(text):
    words = text.split()
    return len(words)

def read_book(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

if __name__ == "__main__":
    sys.exit(main())