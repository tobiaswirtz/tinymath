from tinymath_token import Token, TokenList

class Lexer():
    def __init__(self):
        pass

    def build_tokens(self, token_candidate_type, token_candidate, tokens):
        if token_candidate != "":
            if token_candidate_type == "number":
                token_candidate = float(token_candidate)
            new_token = Token(token_candidate_type, token_candidate)
            tokens.append(new_token)
        return tokens

    def lex(self, input_str):
        chars = iter(input_str)
        tokens = []
        current_type = ""
        current_token = ""
        for c in chars:
            if c in "+-/*^":
                tokens = self.build_tokens(current_type, current_token, tokens)
                tokens = self.build_tokens("operator", c, tokens)
                current_type = ""
                current_token = ""
            if c in "0123456789.": 
                current_token = current_token + c
                current_type = "number"
            if c in "()":
                tokens = self.build_tokens(current_type, current_token, tokens)
                tokens = self.build_tokens("parenthesis", c, tokens)
                current_type = ""
                current_token = ""
            else: pass

        if current_token != "":
            tokens = self.build_tokens(current_type, current_token, tokens)

        return TokenList(tokens)


