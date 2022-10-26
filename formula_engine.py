##TODOS
# implement addition, subtraction
# implement multiplication, division

class Function():
    def __init__(self, input_formula):
        self.input_formula = input_formula
    
    def evaluate(self):
        
        ## Define operators
        ops = ["+", "-", "*", "/"]
        list_formula = []
        last_begin = 0
        for i in range(0, len(self.input_formula)):
            if self.input_formula[i] in ops:
                list_formula.append(self.input_formula[last_begin:i])
                list_formula.append(self.input_formula[i])
                last_begin = i+1
        list_formula.append(self.input_formula[last_begin:len(self.input_formula)])
        

class Value():
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Value(self.value + other.value)

    def __sub__(self, other):
        return Value(self.value - other.value)

    def __mul__(self, other):
        return Value(self.value *  other.value)

    def __truediv__(self, other):
        return Value(self.value / other.value)
    
    def __repr__(self):
        return int(self.value)
