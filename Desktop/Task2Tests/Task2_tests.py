from unittest import TestCase, main
from analyzer import analyzer


class AnalyzerTest(TestCase):
    def setUp(self):
        self.cases = [
            ("What Is an Example of an API?",
             "Text contains:\n"
             "22 characters 7 words, 1 sentences,\n"
             "0 sentences with dot, 0 sentences with exclamation mark,\n"
             "1 sentences with question mark,\n"
             "0 sentences with one or more comma, you need 0.0  min to read it.")
        ]

    def test_normal_behavior(self):
        for input_value, expected_value in self.cases:
            self.assertEqual(analyzer(input_value), expected_value)


if __name__ == '__main__':
    main()
