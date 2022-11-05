class Token():
    def __init__(self, token_type, input_val):
        self.token_type = token_type
        self.value = input_val

    def __repr__(self):
        return f"Type: {self.token_type}, Value: {str(self.value)}"

class TokenList():
    def __init__(self, token_list):
        self.token_list = token_list

    def __repr__(self):
        printable_token_list = ""
        for token in self.token_list:
            printable_token_list = printable_token_list + "\n" + token.token_type + " " + token.value
        return printable_token_list
## TODO: Implement value types

