import sys
from stats import get_num_words, get_character_counts, sort_dict
from string import ascii_lowercase

def get_book_text(filepath) -> str:
    with open(filepath, 'r') as f:
        contents = f.read()
    return contents

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    pages = get_book_text(book_path)
    wc = get_num_words(pages)
    character_counts = get_character_counts(pages)
    sorted_character_counts = sort_dict(character_counts)
    #print(f"{wc} words found in the document")
    print(f"Found {wc} total words")
    print(character_counts)
    print(sorted_character_counts)
    for char_count in sorted_character_counts:
        if char_count['char'].isalpha():
            print(f"{char_count['char']}: {char_count['num']}")

main()
