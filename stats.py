def get_num_words(text: str) -> int:
    count = 0
    for word in text.split():
        count += 1
    return count

def get_character_counts(text: str) -> dict:
    character_counts = {}
    for word in text.split():
        for character in word.lower():
            if character not in character_counts:
                character_counts[character] = 1
            else:
                character_counts[character] += 1
    return character_counts

def sort_on(items):
    return items["num"]

def sort_dict(unsorted: dict) -> list:
    unsorted_list = [{"char": x, "num": unsorted[x]} for x in unsorted]
    unsorted_list.sort(reverse=True, key=sort_on)
    return unsorted_list
