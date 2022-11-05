from nodes import *

class Parser():
    def __init__(self, token_list):
        self.tokens = iter(token_list)
        self.advance()

    def raise_error(self):
        raise Exception("Invalid syntax")

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

   
    def factor(self):
        token = self.current_token

        if token.value == "(":
            self.advance()
            result = self.expression()

            if self.current_token.value != ")":
                self.raise_error()

            self.advance()
            return result


        elif token.token_type == "number":
            self.advance()
            return NumberNode(token.value)
        
        elif token.value == "+":
            self.advance()
            return PlusNode(self.factor())

        elif token.value == "-":
            self.advance()
            return MinusNode(self.factor())

        self.raise_error()

    def exp(self):

        result = self.factor()

        while self.current_token != None and self.current_token.value == "^":
            self.advance()
            result = ExpNode(result, self.factor())

        return result

    def term(self):
        result = self.exp()

        while self.current_token != None and self.current_token.value in "*/":
            if self.current_token.value == "*":
                self.advance()
                result = MulNode(result, self.exp())
            elif self.current_token.value == "/":
                self.advance()
                result = DivNode(result, self.exp())

        return result


    def expression(self):
        result = self.term()

        while self.current_token != None and self.current_token.value in "+-":
            if self.current_token.value == "+":
                self.advance()
                result = AddNode(result, self.term())
            elif self.current_token.value == "-":
                self.advance()
                result = SubNode(result, self.term())
            
        return result

    def parse(self):
        if self.current_token == None:
            return None

        result = self.expression()
        
        if self.current_token != None:
            self.raise_error()

        return result
