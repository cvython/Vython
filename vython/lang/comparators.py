from rply.token import BaseBox


class Comparators(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.value = False


class Egal(Comparators):
    def eval(self):
        if self.left.eval() == self.right.eval():
            return True
        else:
            return False


class Less(Comparators):
    def eval(self):
        if self.left.eval() < self.right.eval():
            return True
        else:
            return False


class More(Comparators):
    def eval(self):
        if self.left.eval() > self.right.eval():
            return True
        else:
            return False


class LessOrEgal(Comparators):
    def eval(self):
        if self.left.eval() <= self.right.eval():
            return True
        else:
            return False


class MoreOrEgal(Comparators):
    def eval(self):
        if self.left.eval() >= self.right.eval():
            return True
        else:
            return False
