class Errors:
    def __init__(self):
        self.NOTDECLARED = "NotDeclared"
        self.INVALIDTYPE = "InvalidType"
        self.UNEXPECTEDSYNTAX = "UnexceptedSyntax"
        self.EXPECTEDSYNTAX = "ExpectedSyntax"
        self.IMPOSSIBLEOPERATION = "ImpossibleOperation"
        self.NUMBERARG = "InvalidNumber"
        self.INDEXOUTOFRANGE = "IndexOutOfRange"


errors = Errors()


def error(typeerror, message, info):
    typeselements = info["type"].split(", ")
    print(typeerror, ":", message)
    if "token" in typeselements:
        print(" - Position : Lign", info["token"].getsourcepos().lineno, "| Column",
              info["token"].getsourcepos().colno)
        if typeerror == errors.NOTDECLARED:
            print(" - Name :", info["token"].getstr())
    if "var" in typeselements:
        print(" - Variable : Name =", info["var"].name, "| Type =", info["var"].kind.tostr())
    if "member" in typeselements:
        print(" - Member :", info["member"])
    if "value" in typeselements:
        print(" - Value :", info["value"])
    if "nbgived" in typeselements:
        print(" - Number Gived :", info["nbgived"])
    if "nbwanted" in typeselements:
        print(" - Number Expected :", info["nbwanted"])
    if "typegived" in typeselements:
        print(" - Type Gived :", info["typegived"])
    if "typewanted" in typeselements:
        print(" - Type Expected :", info["typewanted"])
    if "operationtype" in typeselements:
        print(" - Operation :", info["operationtype"])
    if "index" in typeselements:
        print(" - Index :", info["index"])
    if "max" in typeselements:
        print(" - Maximum :", info["max"])
    if "values" in typeselements:
        print(" - Values :", info["values"][0], "|", info["values"][1])
    if "types" in typeselements:
        print(" - Types :", info["types"][0], "|", info["types"][1])
