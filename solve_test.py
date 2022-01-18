import unittest

from solve import update_words, handle_input


class TestUpdateWords(unittest.TestCase):
    def test_should_filter_out_words_based_on_rules_1(self):
        words = [
            "coirs",
            "coked",
            "cokey",
            "Coker",
            "cokes",
            "cokie",
            "Colan",
            "Colas",
            "colat",
            "Colby",
            "colds",
        ]
        rules = "cok.."
        required_chars = ["c", "o", "k"]
        black_list_chars = ["....r"]
        wrong_spot_chars = []
        expected = ["coked", "cokey", "cokes", "cokie"]

        result = update_words(words, rules, required_chars, wrong_spot_chars, black_list_chars)

        self.assertEqual(result, expected)
        
    def test_should_filter_out_words_based_on_rules_2(self):
        words = [
            "which",
            "being",
            "while",
            "built",
            "third",
            "union",
        ]
        rules = "..i.."
        required_chars = ["i"]
        wrong_spot_chars = []
        black_list_chars = ["g....", ".u...", "...l.", "....d"]
        expected = ["which"]

        result = update_words(words, rules, required_chars, wrong_spot_chars, black_list_chars)

        self.assertEqual(result, expected)


class TestHandleInput(unittest.TestCase):
    def test_should_handle_input_correctly(self):
        test_cases = [
            ("FREED BGBBB", (".r...", ["r"], [], ["f....","..e..", "...e.", "....d"])),
            ("PORSE GYYBB", ("p....", ["p","o","r"], [(1, 'o'), (2, 'r')], ["...s.", "....e"])),
            ("GUILD BBGBB", ("..i..", ["i"], [], ["g....", ".u...", "...l.", "....d"])),
        ]

        for user_input, expected in test_cases:
            result = handle_input(user_input, [], [])

            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()