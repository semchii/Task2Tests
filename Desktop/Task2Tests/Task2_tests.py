from unittest import TestCase, main
from analyzer import analyzer


class AnalyzerTest(TestCase):
    def setUp(self):
        self.cases = [
            ("What Is an Example of an API?", "Text contains: "
                                              "22 characters, 7 words, 1 sentences, 0 sentences with "
                                              "dot, 0 sentences with exclamation mark, 1 sentences with question "
                                              "mark, 0 sentences with one or more comma, you need 0.0 min to read it.")
        ]

    def test_normal_behavior(self):
        for expected_value, input_value in self.cases:
            self.assertEqual(analyzer(input_value), expected_value)


if __name__ == '__main__':
    main()
