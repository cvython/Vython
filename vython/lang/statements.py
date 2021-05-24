from rply.token import BaseBox


class Statement(BaseBox):
    def __init__(self, exp):
        self.exp = exp

    def eval(self):
        self.exp.eval()

    @staticmethod
    def gettokentype():
        return "statement"


class StatementList(BaseBox):
    def __init__(self, statement, sl=None):
        if sl is not None:
            self.statements = sl.statements
        else:
            self.statements = []
        if statement is not None:
            self.statements.append(statement)

    def eval(self):
        for i in self.statements:
            i.eval()

    @staticmethod
    def gettokentype():
        return "statementlist"
