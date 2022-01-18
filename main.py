from solve import update_words, handle_input, print_words, load_words


words = load_words()
rule = "....."
required_chars = []
black_list_rules = []


while True:
    user_input = input("Your input: ")
    rule, required_chars, wrong_spot_char, black_list_rules = handle_input(user_input, required_chars, black_list_rules)
    words = update_words(words, rule, required_chars, wrong_spot_char, black_list_rules)
    print_words(words)