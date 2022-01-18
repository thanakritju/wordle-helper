import re


def load_words():
    with open("5chars.txt", "r") as f:
        words = [word.strip() for word in f.readlines()]

    return words


def update_words(words, rule, required_chars, black_list_rules):
    updated = []

    # Built exception rule
    black_list_rule = [ _.replace('.', '') for _ in black_list_rules]
    black_list_rule = ''.join(black_list_rule)

    # rebuilt required chars position
    required_chars_pattern = []
    for required_char in required_chars:
        match = re.match('([\w])', required_char)
        matched_pos = match.start()
        matched_char = match.group(0)
        required_chars_pattern.append((matched_pos, matched_char))

    for word in words:

        # Use regular expression to filter out the word that contain any blacklist characters
        if re.search('['+black_list_rule+']', word) :
            continue

        # Have to contain all required characters
        elif not [char.lower() in required_chars for char in word].count(True) >= len(required_chars):
            continue

        # Filter out words that still have wrong spot char in the same place
        elif any([ word[req_pos] == req_char for req_pos, req_char in required_chars_pattern]):
            continue

        # Perfectly matched with the ruled pattern
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