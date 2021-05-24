from rply.token import BaseBox
from vython.lang.expressions import ExpressionBase, ExpressionFromList
from vython.lang.types import List


class Variables(BaseBox):
    def __init__(self):
        self.vars = []

    def add(self, var):
        if self.get(var.name) is not None:
            self.set(var.name, var.value)
        else:
            self.vars.append(var)

    def get(self, nom):
        for i in self.vars:
            if i.name == nom:
                return i

    def set(self, nom, exp):
        var = self.get(nom)
        if var is not None:
            var.value = exp


class Variable(BaseBox):
    def __init__(self, name, exp):
        self.name = name
        self.exp = exp
        self.kind = exp.kind
        self.value = None

    def expression(self):
        return ExpressionBase(self.value, self.kind)

    def get(self, indice):
        return ExpressionBase(None, "none")

    def gettype(self):
        return self.kind

    def eval(self):
        self.value = self.exp.eval()
        self.kind = self.exp.kind
        return ExpressionBase(self.value, self.kind)


class ListVar(BaseBox):
    def __init__(self, name, exp):
        self.name = name
        self.exp = exp
        self.kind = exp
        self.value = []
        self.values = []

    def expression(self):
        return ExpressionBase(self.values, self.kind, self)

    def get(self, indice):
        return ExpressionFromList(self, indice)

    def gettype(self):
        return self.kind

    def eval(self):
        self.exp.eval()
        self.values = self.exp.getexpression()
        self.value = []
        for i in self.values:
            self.value.append(i.eval())
        return self.value


class AffectionVar(BaseBox):
    def __init__(self, var, exp):
        self.var = var
        self.exp = exp

    def eval(self):
        if type(self.exp) == List and type(self.var.exp) == List:
            self.var.exp.var = self.exp.var
        else:
            self.var.exp = self.exp
        self.var.eval()
        return self.var
