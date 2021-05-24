from rply.token import BaseBox
from vython.errors import error, Errors as errors
import sys

class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        if self.right.kind == "string" or self.left.kind == "string":
            self.kind = "string"
        else:
            self.kind = self.left.kind

class Sum(BinaryOp):
    def eval(self):
        try:
            return self.left.eval() + self.right.eval()
        except:
            try:
                return self.left.sum(self.right)
            except:
                error(
                    errors.IMPOSSIBLEOPERATION, "", {
                        "type": "values, types, operationtype",
                        "operationtype": "Addition",
                        "values": [self.left.eval(),
                                   self.right.eval()],
                        "types":
                        [self.left.kind.tostr(),
                         self.right.kind.tostr()]
                    })
                sys.exit(1)


class Sub(BinaryOp):
    def eval(self):
        try:
            return self.left.eval() - self.right.eval()
        except:
            try:
                return self.left.sub(self.right)
            except:
                error(
                    errors.IMPOSSIBLEOPERATION, "", {
                        "type": "values, types, operationtype",
                        "operationtype": "Substraction",
                        "values": [self.left.eval(),
                                   self.right.eval()],
                        "types":
                        [self.left.kind.tostr(),
                         self.right.kind.tostr()]
                    })
                sys.exit(1)


class Mul(BinaryOp):
    def eval(self):
        try:
            return self.left.eval() * self.right.eval()
        except:
            try:
                return self.left.mul(self.right)
            except:
                error(
                    errors.IMPOSSIBLEOPERATION, "", {
                        "type": "values, types, operationtype",
                        "operationtype": "Multiplication",
                        "values": [self.left.eval(),
                                   self.right.eval()],
                        "types":
                        [self.left.kind.tostr(),
                         self.right.kind.tostr()]
                    })
                sys.exit(1)


class Div(BinaryOp):
    def eval(self):
        try:
            return self.left.eval() / self.right.eval()
        except:
            try:
                return self.left.div(self.right)
            except:
                error(
                    errors.IMPOSSIBLEOPERATION, "", {
                        "type": "values, types, operationtype",
                        "operationtype": "Division",
                        "values": [self.left.eval(),
                                   self.right.eval()],
                        "types":
                        [self.left.kind.tostr(),
                         self.right.kind.tostr()]
                    })
                sys.exit(1)


class DivEu(BinaryOp):
    def eval(self):
        try:
            return self.left.eval() // self.right.eval()
        except:
            try:
                return self.left.diveu(self.right)
            except:
                error(
                    errors.IMPOSSIBLEOPERATION, "", {
                        "type": "values, types, operationtype",
                        "operationtype": "Euclidean Division",
                        "values": [self.left.eval(),
                                   self.right.eval()],
                        "types":
                        [self.left.kind.tostr(),
                         self.right.kind.tostr()]
                    })
                sys.exit(1)


class Pow(BinaryOp):
    def eval(self):
        try:
            return self.left.eval()**self.right.eval()
        except:
            try:
                return self.left.pow(self.right)
            except:
                error(
                    errors.IMPOSSIBLEOPERATION, "", {
                        "type": "values, types, operationtype",
                        "operationtype": "Power",
                        "values": [self.left.eval(),
                                   self.right.eval()],
                        "types":
                        [self.left.kind.tostr(),
                         self.right.kind.tostr()]
                    })
                sys.exit(1)


class Mod(BinaryOp):
    def eval(self):
        try:
            return self.left.eval() % self.right.eval()
        except:
            try:
                return self.left.mod(self.right)
            except:
                error(
                    errors.IMPOSSIBLEOPERATION, "", {
                        "type": "values, types, operationtype",
                        "operationtype": "Modulo",
                        "values": [self.left.eval(),
                                   self.right.eval()],
                        "types":
                        [self.left.kind.tostr(),
                         self.right.kind.tostr()]
                    })
                sys.exit(1)
