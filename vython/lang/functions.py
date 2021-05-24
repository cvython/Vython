from rply.token import BaseBox
from vython.lang.expressions import ExpressionBase
import sys
from vython.lang.types import BoolType, StrType, IntType, FloatType
from vython.errors import error, Errors as errors


class CanBe(BaseBox):
    def __init__(self, exp, value):
        self.value = value
        self.exp = exp
        self.kind = BoolType(ExpressionBase(True, "boolean"))

    def eval(self):
        if self.value == "int":
            try:
                int(self.exp.eval())
                return True
            except:
                return False
        elif self.value == "float":
            try:
                float(self.exp.eval())
                return True
            except:
                return False
        elif self.value == "str":
            try:
                str(self.exp.eval())
                return True
            except:
                return False
        elif self.value == "bool":
            try:
                bool(self.exp.eval())
                return True
            except:
                return False
        else:
            error(
                errors.INVALIDTYPE, "", {
                    "type": "operationtype, typegived, typewanted",
                    "typewanted": "integer, string, float, boolean",
                    "typegived": self.value,
                    "operationtype": "CanBe Function"
                })
            sys.exit(1)


class Print(BaseBox):
    def __init__(self, value=ExpressionBase("", "string")):
        self.value = value
        self.kind = StrType(ExpressionBase("", "string"))

    def eval(self):
        self.value = self.value.eval()
        print(self.value)
        return self.value


class Input(BaseBox):
    def __init__(self, text=""):
        self.text = text[1:-1]
        self.kind = StrType(ExpressionBase("", "string"))

    def eval(self):
        try:
            data = input(self.text)
            return data
        except KeyboardInterrupt:
            return ''


class Int(BaseBox):
    def __init__(self, exp):
        self.exp = exp
        self.kind = IntType(ExpressionBase(0, "integer"))

    def eval(self):
        try:
            return int(self.exp.eval())
        except:
            error(
                errors.IMPOSSIBLEOPERATION, "", {
                    "type": "operationtype, value",
                    "operationtype": "Become Integer",
                    "value": self.exp.eval()
                })
            sys.exit(1)


class Float(BaseBox):
    def __init__(self, exp):
        self.exp = exp
        self.kind = FloatType(ExpressionBase(0.0, "float"))

    def eval(self):
        try:
            return float(self.exp.eval())
        except:
            error(
                errors.IMPOSSIBLEOPERATION, "", {
                    "type": "operationtype, value",
                    "operationtype": "Become Float",
                    "value": self.exp.eval()
                })
            sys.exit(1)


class Str(BaseBox):
    def __init__(self, exp):
        self.exp = exp
        self.kind = StrType(ExpressionBase("", "string"))

    def eval(self):
        try:
            return str(self.exp.eval())
        except:
            error(
                errors.IMPOSSIBLEOPERATION, "", {
                    "type": "operationtype, value",
                    "operationtype": "Become String",
                    "value": self.exp.eval()
                })
            sys.exit(1)


class Boolean(BaseBox):
    def __init__(self, exp):
        self.exp = exp
        self.kind = BoolType(ExpressionBase(True, "boolean"))

    def eval(self):
        try:
            return bool(self.exp.eval())
        except:
            error(
                errors.IMPOSSIBLEOPERATION, "", {
                    "type": "operationtype, value",
                    "operationtype": "Become Boolean",
                    "value": self.exp.eval()
                })
            sys.exit(1)


class Type(BaseBox):
    def __init__(self, exp):
        self.exp = exp
        self.kind = StrType(ExpressionBase("", "string"))

    def eval(self):
        self.exp.eval()
        return self.exp.gettype().tostr()
