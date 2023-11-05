import unittest

from ex_1 import add_one_to_binary_tape


class TestClass(unittest.TestCase):
    def test_should_return_1110(self):
        assert add_one_to_binary_tape("1101") == "1110"

    def test_should_return_1111(self):
        assert add_one_to_binary_tape("1110") == "1111"

    def test_should_add_bit_shift_return_1000(self):
        assert add_one_to_binary_tape("111") == "1000"