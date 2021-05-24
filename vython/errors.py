import sys


class Errors:
    NOTDECLARED = "NotDeclared"
    INVALIDTYPE = "InvalidType"
    UNEXPECTEDSYNTAX = "UnexceptedSyntax"
    EXPECTEDSYNTAX = "ExpectedSyntax"
    IMPOSSIBLEOPERATION = "ImpossibleOperation"
    NUMBERARG = "InvalidNumber"
    INDEXOUTOFRANGE = "IndexOutOfRange"


class _ThrowException(object):
    def __init__(self, error_type, message, info):
        self.elements = info.get("type").split(", ") if info else []
        self.message = message
        self.error = error_type
        self.info = info

        self.evoke_exception()

    def evoke_exception(self):
        print(f"{self.error} : {self.message}")

        if "token" in self.elements:
            print(" - Position : Lign",
                  self.info["token"].getsourcepos().lineno, "| Column",
                  self.info["token"].getsourcepos().colno)
            if self.error == Errors.NOTDECLARED:
                print(" - Name :", self.info["token"].getstr())
        if "var" in self.elements:
            print(" - Variable : Name =", self.info["var"].name, "| Type =",
                  self.info["var"].kind.tostr())
        if "member" in self.elements:
            print(" - Member :", self.info["member"])
        if "value" in self.elements:
            print(" - Value :", self.info["value"])
        if "nbgived" in self.elements:
            print(" - Number Gived :", self.info["nbgived"])
        if "nbwanted" in self.elements:
            print(" - Number Expected :", self.info["nbwanted"])
        if "typegived" in self.elements:
            print(" - Type Gived :", self.info["typegived"])
        if "typewanted" in self.elements:
            print(" - Type Expected :", self.info["typewanted"])
        if "operationtype" in self.elements:
            print(" - Operation :", self.info["operationtype"])
        if "index" in self.elements:
            print(" - Index :", self.info["index"])
        if "max" in self.elements:
            print(" - Maximum :", self.info["max"])
        if "values" in self.elements:
            print(" - Values :", self.info["values"][0], "|",
                  self.info["values"][1])
        if "types" in self.elements:
            print(" - Types :", self.info["types"][0], "|",
                  self.info["types"][1])


def error(error_type, message, info):
    _ThrowException(error_type, message, info)
    sys.exit()
    return None