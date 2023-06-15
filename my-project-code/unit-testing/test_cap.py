import unittest
import cap

# create class that inherits from unittest.TestCase
class TestCap(unittest.TestCase):
    # normally number the tests that are going to be called
    def test_one_word(self):
        # test data to be used
        test_text = 'frog'
        # call the function to be tested
        result = cap.capitalze_first_letter(test_text)
        # does it give the result we expected
        self.assertEqual(result,'Frog')

    # building up some regression tests
    def test_two_multiple_words(self):
        test_text = 'frog butterfly'
        result = cap.capitalze_first_letter(test_text)
        self.assertEqual(result,'Frog Butterfly')

# QA department test automation
if __name__ == '__main__':
    unittest.main()


