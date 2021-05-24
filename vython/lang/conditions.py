from rply.token import BaseBox


class If(BaseBox):
    def __init__(self, condition, statementlist):
        self.condition = condition
        self.statementlist = statementlist

    def eval(self):
        if bool(self.condition.eval()):
            self.statementlist.eval()

    @staticmethod
    def gettokentype():
        return 'statement'


class Else(BaseBox):
    def __init__(self, statementlist):
        self.statementlist = statementlist


class ElseIf(BaseBox):
    def __init__(self, condition, statementlist):
        self.condition = condition
        self.statementlist = statementlist

    def eval(self):
        if bool(self.condition.eval()):
            self.statementlist.eval()
            return True
        return False


class ElseIfs(BaseBox):
    def __init__(self, elseif):
        self.elseifs = []
        self.elseifs.append(elseif)

    def add(self, elseif):
        for i in elseif.elseifs:
            self.elseifs.append(i)
        return self

    def eval(self):
        find = False
        for i in range(len(self.elseifs)):
            if self.elseifs[i].eval():
                find = True
                break
        return find


class IfElseIf(BaseBox):
    def __init__(self, ifexp, elseifs):
        self.ifcondition = ifexp.condition
        self.ifstatementlist = ifexp.statementlist
        self.elseifs = elseifs

    def eval(self):
        if bool(self.ifcondition.eval()):
            self.ifstatementlist.eval()
        else:
            self.elseifs.eval()


class IfElseIfElse(BaseBox):
    def __init__(self, ifexp, elseifs, elseexp):
        self.ifcondition = ifexp.condition
        self.ifstatementlist = ifexp.statementlist
        self.elseifs = elseifs
        self.elsestatementlist = elseexp.statementlist

    def eval(self):
        if bool(self.ifcondition.eval()):
            self.ifstatementlist.eval()
        else:
            if not self.elseifs.eval():
                self.elsestatementlist.eval()


class IfElse(BaseBox):
    def __init__(self, ifexp, elseexp):
        self.condition = ifexp.condition
        self.statementlistif = ifexp.statementlist
        self.statementlistelse = elseexp.statementlist

    def eval(self):
        if bool(self.condition.eval()):
            self.statementlistif.eval()
        else:
            self.statementlistelse.eval()

    @staticmethod
    def gettokentype():
        return 'statement'
