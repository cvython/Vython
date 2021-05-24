import sys
from vython.errors import error, Errors as errors

class Type:
    def __init__(self, exp):
        self.name = ""
        self.exp = exp
        self.paramMember = []

    def callmember(self, membre, param):
        self.paramMember = param
        try:
            return eval("self." + membre + "()")
        except AttributeError:
            error(
                errors.NOTDECLARED, "Unknown Member", {
                    "type": "typeerror, member",
                    "member": membre,
                    "typeerror": self.name
                })
            sys.exit(1)

    def tostr(self):
        return self.name


class NoneType(Type):
    def __init__(self, exp):
        super(NoneType, self).__init__(exp)
        self.name = "none"


class IntType(Type):
    def __init__(self, exp):
        super(IntType, self).__init__(exp)
        self.name = "integer"


class StrType(Type):
    def __init__(self, exp):
        super(StrType, self).__init__(exp)
        self.name = "string"

    def sum(self, value1, value2):
        return str(value1) + str(value2)

    def sub(self, value1, value2):
        return str(value1)[:len(value1) - value2]

    def increment(self, value1):
        return value1 + value1

    def length(self):
        nbarg = 0
        if len(self.paramMember) != nbarg:
            error(
                errors.NUMBERARG, "", {
                    "type": "nbwanted, nbgived, member",
                    "member": "length",
                    "nbgived": len(self.paramMember),
                    "nbwanted": nbarg
                })
            sys.exit(1)
        return len(self.exp.eval())


class FloatType(Type):
    def __init__(self, exp):
        super(FloatType, self).__init__(exp)
        self.name = "float"


class BoolType(Type):
    def __init__(self, exp):
        super(BoolType, self).__init__(exp)
        self.name = "bool"


class List(Type):
    def __init__(self, exp=None, exp2=None):
        super(List, self).__init__(exp)
        self.name = "list"
        self.kind = self
        if exp is None and exp2 is None:
            self.var = []
        elif exp is None:
            if type(exp2) == List:
                self.var = exp2.var
            else:
                self.var = [exp2]
        elif exp2 is None:
            if type(exp) == List:
                self.var = exp.var
            else:
                self.var = [exp]
        else:
            if type(exp) == List and type(exp2) == List:
                self.var = exp.var
                for i in exp2.var:
                    self.var.append(i)
            elif type(exp) == List:
                self.var = exp.var
                self.var.append(exp2)
            elif type(exp2) == List:
                self.var = [exp]
                for i in exp2.var:
                    self.var.append(i)
            else:
                self.var = [exp, exp2]

    def add(self, exp):
        self.var.append(exp)

    def getexpression(self):
        return self.var

    def eval(self):
        for i in range(len(self.var)):
            self.var[i].value = self.var[i].eval()

    def length(self):
        nbarg = 0
        if len(self.paramMember) != nbarg:
            error(
                errors.NUMBERARG, "", {
                    "type": "nbwanted, nbgived, member",
                    "member": "length",
                    "nbgived": len(self.paramMember),
                    "nbwanted": nbarg
                })
            sys.exit(1)
        self.eval()
        return len(self.var)

    def remove(self):
        nbarg = 1
        if len(self.paramMember) != nbarg:
            error(
                errors.NUMBERARG, "", {
                    "type": "nbwanted, nbgived, member",
                    "member": "length",
                    "nbgived": len(self.paramMember),
                    "nbwanted": nbarg
                })
            sys.exit(1)
        if type(self.paramMember[0].kind) != IntType:
            error(
                errors.INVALIDTYPE, "", {
                    "type": "typewanted, typegived, member",
                    "member": "remove",
                    "typegived": self.paramMember[0].kind.tostr(),
                    "typewanted": IntType(None).tostr()
                })
            sys.exit(1)
        self.eval()
        value = self.var[self.paramMember[0].eval()]
        del self.var[self.paramMember[0].eval()]
        return value.eval()


typesOfMembers = {"length": IntType, "remove": NoneType}


class MemberType:
    def __init__(self, name, var, param=None):
        if param is None:
            param = []
        self.name = name
        self.var = var
        try:
            self.kind = typesOfMembers[self.name](None)
        except KeyError:
            error(
                errors.NOTDECLARED, "Unknown Member", {
                    "type": "typeerror, member",
                    "member": self.name,
                    "typeerror": self.var.gettype().tostr()
                })
            sys.exit(1)
        self.param = param

    def eval(self):
        return self.var.gettype().callmember(self.name, self.param)
