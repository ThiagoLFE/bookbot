from stats import get_num_words, count_characters, show_count_characters_formatted
import sys

def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def main():
    print("Usage: python3 main.py <path_to_book>")
    if len(sys.argv) >1:
        book_content = get_book_text(sys.argv[1])
        all_characters = count_characters(book_content)
        print(f"Found {get_num_words(book_content)} total words")

        show_count_characters_formatted(all_characters)

    else:
        sys.exit(1);

main()
