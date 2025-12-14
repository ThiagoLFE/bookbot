from stats import get_num_words, count_characters, show_count_characters_formatted

def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def main():
    book_content = get_book_text("./books/frankenstein.txt")
    all_characters = count_characters(book_content)
    print(f"Found {get_num_words(book_content)} total words")

    show_count_characters_formatted(all_characters)

main()
