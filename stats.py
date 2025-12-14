# stats.py
def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text_lower = text.lower()
    all_characters = {}

    for character in text_lower:
        if character in all_characters:
            all_characters[character] += 1
        else:
            all_characters[character] = 1

    return all_characters

def show_count_characters_formatted(all_characters):
    print("--------- Character Count -------")
    
    characters_list = []
    
    for character in all_characters:
        characters_list.append({
            "char": character,
            "qtd": all_characters[character]
        })
    
    characters_list.sort(key=lambda item: item["qtd"], reverse=True)

    for item in characters_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["qtd"]}")
            