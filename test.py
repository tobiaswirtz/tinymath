import unittest
from lexer import Lexer
from nodes import *
from tinymath_interpreter import Interpreter
from values import Number


class TestLexerFunction(unittest.TestCase):
    
    def test_lex(self):
        lx = Lexer()
        tl = lx.lex("5+10(4*4.1^6-4)")
        self.assertEqual(tl.token_list[0].value, 5.0)
        self.assertEqual(tl.token_list[1].value, "+")
        self.assertEqual(tl.token_list[2].value, 10)
        self.assertEqual(tl.token_list[3].value, "(")
        self.assertEqual(tl.token_list[4].value, 4)
        self.assertEqual(tl.token_list[5].value, "*")
        self.assertEqual(tl.token_list[6].value, 4.1)
        self.assertEqual(tl.token_list[7].value, "^")
        self.assertEqual(tl.token_list[8].value, 6)
        self.assertEqual(tl.token_list[9].value, "-")
        self.assertEqual(tl.token_list[10].value, 4)
        self.assertEqual(tl.token_list[11].value, ")")
        self.assertEqual(tl.token_list[0].token_type, "number")
        self.assertEqual(tl.token_list[1].token_type, "operator")
        self.assertEqual(tl.token_list[2].token_type, "number")
        self.assertEqual(tl.token_list[3].token_type, "parenthesis")
        self.assertEqual(tl.token_list[4].token_type, "number")
        self.assertEqual(tl.token_list[5].token_type, "operator")
        self.assertEqual(tl.token_list[6].token_type, "number")
        self.assertEqual(tl.token_list[7].token_type, "operator")
        self.assertEqual(tl.token_list[8].token_type, "number")
        self.assertEqual(tl.token_list[9].token_type, "operator")
        self.assertEqual(tl.token_list[10].token_type, "number")
        self.assertEqual(tl.token_list[11].token_type, "parenthesis")

class TestInterpreter(unittest.TestCase):

	def test_numbers(self):
		value = Interpreter().visit(NumberNode(51.2))
		self.assertEqual(value, Number(51.2))

	def test_single_operations(self):
		result = Interpreter().visit(AddNode(NumberNode(27), NumberNode(14)))
		self.assertEqual(result.value, 41.0)

		result = Interpreter().visit(SubNode(NumberNode(27), NumberNode(14)))
		self.assertEqual(result.value, 13.0)

		result = Interpreter().visit(MulNode(NumberNode(27), NumberNode(14)))
		self.assertEqual(result.value, 378.0)

		result = Interpreter().visit(DivNode(NumberNode(27), NumberNode(14)))
		self.assertAlmostEqual(result.value, 1.92857, 5)

		result = Interpreter().visit(ExpNode(NumberNode(2), NumberNode(4)))
		self.assertAlmostEqual(result.value, 16.0)

		with self.assertRaises(Exception):
			Interpreter().visit(DivNode(NumberNode(27), NumberNode(0)))
			
	def test_full_expression(self):
		tree = AddNode(
			NumberNode(27),
			MulNode(
				SubNode(
					DivNode(
						NumberNode(43),
						NumberNode(36)
					),
					NumberNode(48)
				),
				NumberNode(51)
			)
		)

		result = Interpreter().visit(tree)
		self.assertAlmostEqual(result.value, -2360.08, 2)

if __name__ == '__main__':
    unittest.main()
