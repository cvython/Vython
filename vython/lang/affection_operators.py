from rply.token import BaseBox
import sys
from vython.errors import error, errors


class AffectionOperator(BaseBox):
    def __init__(self, var, right):
        self.right = right
        self.var = var
        self.kind = var.kind


class SumAffector(AffectionOperator):
    def eval(self):
        if self.right.kind == "string":
            self.kind = "string"

        try:
            self.var.value = self.var.value + self.right.eval()
            return self.var.value
        except:
            try:
                self.var.value = self.var.expression().sum(self.right.eval())
                return self.var.value
            except:
                error(
                    errors.IMPOSSIBLEOPERATION, "", {
                        "type": "values, types, operationtype",
                        "operationtype": "Addition Affection",
                        "values": [self.var.eval().eval(),
                                   self.right.eval()],
                        "types":
                        [self.var.kind.tostr(),
                         self.right.kind.tostr()]
                    })
                sys.exit(1)


class SubAffector(AffectionOperator):
    def eval(self):
        try:
            self.var.value = self.var.value - self.right.eval()
            return self.var.value
        except:
            try:
                self.var.value = self.var.expression().sub(self.right.eval())
                return self.var.value
            except:
                error(
                    errors.IMPOSSIBLEOPERATION, "", {
                        "type": "values, types, operationtype",
                        "operationtype": "Subtraction Affection",
                        "values": [self.var.eval().eval(),
                                   self.right.eval()],
                        "types":
                        [self.var.kind.tostr(),
                         self.right.kind.tostr()]
                    })
                sys.exit(1)


class MulAffector(AffectionOperator):
    def eval(self):
        try:
            self.var.value = self.var.value * self.right.eval()
            return self.var.value
        except:
            try:
                self.var.value = self.var.expression().mul(self.right.eval())
                return self.var.value
            except:
                error(
                    errors.IMPOSSIBLEOPERATION, "", {
                        "type": "values, types, operationtype",
                        "operationtype": "Multiplication Affection",
                        "values": [self.var.eval().eval(),
                                   self.right.eval()],
                        "types":
                        [self.var.kind.tostr(),
                         self.right.kind.tostr()]
                    })
                sys.exit(1)


class DivAffector(AffectionOperator):
    def eval(self):
        try:
            self.var.value = self.var.value / self.right.eval()
            return self.var.value
        except:
            try:
                self.var.value = self.var.expression().div(self.right.eval())
                return self.var.value
            except:
                error(
                    errors.IMPOSSIBLEOPERATION, "", {
                        "type": "values, types, operationtype",
                        "operationtype": "Division Affection",
                        "values": [self.var.eval().eval(),
                                   self.right.eval()],
                        "types":
                        [self.var.kind.tostr(),
                         self.right.kind.tostr()]
                    })
                sys.exit(1)


class DivEuAffector(AffectionOperator):
    def eval(self):
        try:
            self.var.value = self.var.value // self.right.eval()
            return self.var.value
        except:
            try:
                self.var.value = self.var.expression().diveu(self.right.eval())
                return self.var.value
            except:
                error(
                    errors.IMPOSSIBLEOPERATION, "", {
                        "type": "values, types, operationtype",
                        "operationtype": "Euclidean Division Affection",
                        "values": [self.var.eval().eval(),
                                   self.right.eval()],
                        "types":
                        [self.var.kind.tostr(),
                         self.right.kind.tostr()]
                    })
                sys.exit(1)


class ModAffector(AffectionOperator):
    def eval(self):
        try:
            self.var.value = self.var.value % self.right.eval()
            return self.var.value
        except:
            try:
                self.var.value = self.var.expression().mod(self.right.eval())
                return self.var.value
            except:
                error(
                    errors.IMPOSSIBLEOPERATION, "", {
                        "type": "values, types, operationtype",
                        "operationtype": "Modulo Affection",
                        "values": [self.var.eval().eval(),
                                   self.right.eval()],
                        "types":
                        [self.var.kind.tostr(),
                         self.right.kind.tostr()]
                    })
                sys.exit(1)


class PowAffector(AffectionOperator):
    def eval(self):
        try:
            self.var.value = self.var.value**self.right.eval()
            return self.var.value
        except:
            try:
                self.var.value = self.var.expression().pow(self.right.eval())
                return self.var.value
            except:
                error(
                    errors.IMPOSSIBLEOPERATION, "", {
                        "type": "values, types, operationtype",
                        "operationtype": "Power Affection",
                        "values": [self.var.eval().eval(),
                                   self.right.eval()],
                        "types":
                        [self.var.kind.tostr(),
                         self.right.kind.tostr()]
                    })
                sys.exit(1)
