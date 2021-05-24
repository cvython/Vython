from rply.token import BaseBox


class LogicOperators(BaseBox):
    def __init__(self, left, right=None):
        self.left = left
        self.right = right


class And(LogicOperators):
    def eval(self):
        if self.left.eval() and self.right.eval():
            return True
        else:
            return False


class Or(LogicOperators):
    def eval(self):
        if self.left.eval() or self.right.eval():
            return True
        else:
            return False


class Not(LogicOperators):
    def eval(self):
        if not self.left.eval():
            return True
        else:
            return False
