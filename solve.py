import re


def load_words():
    with open("5chars.txt", "r") as f:
        words = [word.strip() for word in f.readlines()]

    return words


def update_words(words, rule, required_chars, black_list_rules):
    updated = []

    for word in words:
        if any([re.search(black_list_rule, word) for black_list_rule in black_list_rules]):
            continue
        elif not any([char.lower() in required_chars for char in word]):
            continue
        elif re.search(rule, word):
            updated.append(word)

    return updated
    

def handle_input(user_input, required_chars, black_list_rules):
    rule = ""
    word, result = user_input.split(" ")

    for index, char in enumerate(result):
        black_list = [".",".",".",".","."]
        insert_char = word[index].lower()
        if char == "G":
            rule += insert_char
            if insert_char not in required_chars:
                required_chars.append(insert_char)
        elif char == "Y":
            rule += "."
            if insert_char not in required_chars:
                required_chars.append(insert_char)
        else:
            rule += "."
            black_list[index] = insert_char
            black_list_rules.append("".join(black_list))

    return rule, required_chars, black_list_rules


def print_words(words):
    for word in words:
        print(word)