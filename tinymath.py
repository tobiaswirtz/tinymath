from lexer import Lexer
from tinymath_parser import Parser
from tinymath_interpreter import Interpreter

while True:
    try:
        text = input("> ")
        lx = Lexer()
        tl = lx.lex(text)
        parser = Parser(tl.token_list)
        tree = parser.parse()
        if not tree: continue
        ip = Interpreter()
        value = ip.visit(tree)
        print(value)
    except Exception as e:
        print(e)
