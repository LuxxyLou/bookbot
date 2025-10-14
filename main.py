from stats import get_num_words
from stats import num_unique_chars

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    num_chars = num_unique_chars(text)
    print(f"Found {num_words} total words")
    print(f"Found {num_chars} unique characters")   


def get_book_text(path):
    with open(path) as file:
        print("opening", path)
        return file.read()

main()


 