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
        expected = ["coked", "cokey", "cokes", "cokie"]

        result = update_words(words, rules, required_chars, black_list_chars)

        self.assertEqual(result, expected)


class TestHandleInput(unittest.TestCase):
    def test_should_handle_input_correctly(self):
        test_cases = [
            ("FREED BGBBB", (".r...", ["r"], ["f.eed"])),
            ("PORSE GYYBB", ("p....", ["p","o","r"], ["...se"])),
        ]

        for user_input, expected in test_cases:
            result = handle_input(user_input, [], [])

            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()