import unittest
import practice


class MyTestCase(unittest.TestCase):
    def test_assertEqual_practice_with_neg_ints(self):
        self.assertEqual(-1, -1)
    def test_assertEqual_practice_with_strings(self):
        self.assertEqual("Hello", "Hello")

    def test_get_sign_neg5(self):
        self.assertEqual(-1, practice.get_sign(-5))

    def test_get_sign_neg1(self):
        self.assertEqual(-1, practice.get_sign(-1))

    def test_get_sign_0(self):
        self.assertEqual(0, practice.get_sign(0), msg="Error: 0 has no sign; sign cannot be 1")

    def test_get_sign_pos1(self):
        self.assertEqual(1, practice.get_sign(1))

    def test_get_sign_pos5(self):
        self.assertEqual(1, practice.get_sign(5))

    def test_input_positive_integer_argument_is_confirmed_before_processing(self):
        self.assertEqual(6, practice.confirm_my_input(6))

    def test_input_with_no_argument_is_confirmed_as_None(self):
        self.assertEqual(-1, practice.confirm_my_input())

if __name__ == '__main__':
    unittest.main()
