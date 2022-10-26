import unittest
from unittest.mock import patch
from formula_engine import Value, Function

class TestValueFunction(unittest.TestCase):

    def test_addition(self):
        x = Value(5)
        y = Value(10)
        self.assertEqual((x+y).__repr__(), 15)

    def test_subtraction(self):
        x = Value(10)
        y = Value(4)
        self.assertEqual((x-y).__repr__(), 6)


class TestFunctionFunction(unittest.TestCase):

    @patch('builtins.input', return_value='5+10-3')
    def test_evaluation(self, input):
        entered = input()
        print(entered)
        func = Function(entered)
        func.evaluate()
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
