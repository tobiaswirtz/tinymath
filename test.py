import unittest
from unittest.mock import patch
from lexer import Lexer

class TestLexerFunction(unittest.TestCase):
    
    def test_lex(self):
        lx = Lexer()
        tl = lx.lex("5+10(4*4.1^6-4)")
        self.assertEqual(tl.token_list[0].value, "5")
        self.assertEqual(tl.token_list[1].value, "+")
        self.assertEqual(tl.token_list[2].value, "10")
        self.assertEqual(tl.token_list[3].value, "(")
        self.assertEqual(tl.token_list[4].value, "4")
        self.assertEqual(tl.token_list[5].value, "*")
        self.assertEqual(tl.token_list[6].value, "4.1")
        self.assertEqual(tl.token_list[7].value, "^")
        self.assertEqual(tl.token_list[8].value, "6")
        self.assertEqual(tl.token_list[9].value, "-")
        self.assertEqual(tl.token_list[10].value, "4")
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



if __name__ == '__main__':
    unittest.main()
