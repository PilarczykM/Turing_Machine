import unittest

from ex_3 import replace_a_with_c


class TestClass(unittest.TestCase):
    def test_should_return_BCCC(self):
        assert replace_a_with_c("BACA") == "BCCC"


    def test_should_return_empty(self):
        assert replace_a_with_c("") == ""

    def test_should_return_word_full_of_c(self):
        assert replace_a_with_c("AAAA") == "CCCC"

    def test_will_do_nothing(self):
        assert replace_a_with_c("XYZCBE") == "XYZCBE"