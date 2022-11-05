from values import Number
from nodes import *

class Interpreter:
    def __init__(self):
        pass

    def visit(self, node):
        func_name = f'visit_{type(node).__name__}'
        func = getattr(self, func_name)
        return func(node)

    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_SubNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MulNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_DivNode(self, node):
        return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)

    def visit_DivNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("Division by zero")

    def visit_ExpNode(self, node):
        return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)
