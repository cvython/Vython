from rply.token import BaseBox
from vython.lang.types import IntType, StrType, BoolType, FloatType, List, NoneType
import sys
from vython.errors import error, Errors as errors

types = {
    "integer": IntType,
    "string": StrType,
    "boolean": BoolType,
    "float": FloatType,
    "list": List,
    "none": NoneType
}

class ExpressionBase(BaseBox):
    def __init__(self, value, kind, var=None):
        self.value = value
        if type(kind) == str:
            self.kind = types[kind](self)
        else:
            self.kind = kind
        self.var = var

    def eval(self):
        if self.var is not None:
            from vython.lang.variables import ListVar
            if type(self.var) == ListVar:
                self.var.eval()
            self.value, self.kind = self.var.value, self.var.kind
        return self.value

    def gettype(self):
        return self.kind

    def sum(self, exp):
        try:
            self.value = self.kind.sum(self.eval(), exp.eval())
        except:
            self.value = exp.kind.sum(exp.eval(), self.eval())
        return self.value

    def sub(self, exp):
        self.value = self.kind.sub(self.eval(), exp.eval())
        return self.value

    def increment(self):
        self.value = self.kind.increment(self.eval())
        return self.value


class ExpressionFromList(ExpressionBase):
    def __init__(self, var, indice):
        self.value = ""
        self.kind = types["list"](self)
        self.var = var
        self.indice = indice

    def eval(self):
        var = self.var.exp.var
        if len(var) <= self.indice:
            values = self.var.exp.getexpression()
            value = []
            for i in values:
                value.append(i.eval())
            error(errors.INDEXOUTOFRANGE, "", {
                "type": "max, index",
                "index": self.indice,
                "max": len(var) - 1
            })
            sys.exit(1)
        self.value, self.kind = var[self.indice].value, var[self.indice].kind
        return self.value


class Nothing(BaseBox):
    @staticmethod
    def eval():
        return None
    
    @staticmethod
    def gettokentype():
        return "statement"
