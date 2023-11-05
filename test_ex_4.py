import unittest

from ex_4 import move_first_letter_to_end


class TestClass(unittest.TestCase):
    def test_should_do_nothing(self):
        assert move_first_letter_to_end("") == ""

    def test_should_do_nothing_when_one_letter(self):
        assert move_first_letter_to_end("A") == "A"

    def test_should_reverse_word(self):
        assert move_first_letter_to_end("ABCDEF") == "BCDEFA"
