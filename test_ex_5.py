import unittest

from ex_5 import swap_start_and_end_bits


class TestClass(unittest.TestCase):
    def test_should_swap_bits(self):
        assert swap_start_and_end_bits("11010") == "01011"

    def test_should_do_nothing(self):
        assert swap_start_and_end_bits("1") == "1"

    def test_should_swap_when_two_bits_provided(self):
        assert swap_start_and_end_bits("12") == "21"
