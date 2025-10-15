from stats import get_num_words
from stats import num_unique_chars
from stats import sort_chars

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    num_chars = num_unique_chars(text)
    print("=" * 12, "BOOKBOT", "=" * 12)
    print("Analyzing book found at", filepath, "...")
    print("-" * 11, " ", "Word Count", " ", "-" * 11)
    print("Found", num_words, "total words")
    print("---------", "Character Count ", "-------") 
    print(sort_chars(num_chars))
    print("=" * 13, "END", "=" * 15)

def get_book_text(path):
    with open(path) as file:
        print("opening", path)
        return file.read()

main()


 