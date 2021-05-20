from rply import ParserGenerator
import sys

from Main.Errors import error, errors

from Main.SYS.BinaryOperators import Sum, Sub, Mul, Div, Mod, Pow, DivEu
from Main.SYS.AffectionOperators import SumAffector, SubAffector, DivEuAffector, MulAffector, DivAffector,\
    ModAffector, PowAffector
from Main.SYS.Expressions import ExpressionBase, Nothing
from Main.SYS.Functions import Print, Input, Int, Str, Float, Type, Boolean, CanBe
from Main.SYS.Variables import Variable, Variables, AffectionVar, ListVar
from Main.SYS.UniqueOperators import Increment, Decrement
from Main.SYS.Comparators import Egal, Less, LessOrEgal, More, MoreOrEgal
from Main.SYS.Conditions import If, IfElse, Else, ElseIf, IfElseIf, IfElseIfElse, ElseIfs
from Main.SYS.LogicOperators import And, Or, Not
from Main.SYS.Statements import Statement, StatementList
from Main.SYS.Loops import Loop, While
from Main.SYS.Types import List, MemberType


class Parser:
    def __init__(self, tokens):
        self.pg = ParserGenerator(
            tokens,
            precedence=[
                ('left', ['NEWLINE']),
                ('left', ['EGAL']),
                ('left', ['AND', 'OR', 'NOT']),
                ('left', ['IS', 'LESS', 'MORE', 'LESSE', 'MOREE']),
                ('left', ['SUMAFF', 'SUBAFF']),
                ('left', ['MULAFF', 'DIVAFF', 'DIVEUAFF', 'MODAFF']),
                ('left', ['POWAFF']),
                ('left', ['SUM', 'SUB']),
                ('left', ['MUL', 'DIV', 'DIVEU', 'MOD']),
                ('left', ['POW'])
            ]
        )
        self.var = Variables()

    def parse(self):
        @self.pg.production('program : statementlist')
        def program(p):
            return p[0].eval()

        @self.pg.production('statementlist : statementlist NEWLINE statement')
        @self.pg.production('statementlist : statementlist NEWLINE loop_statement')
        @self.pg.production('statementlist : statementlist NEWLINE if_statement')
        def statementlistexp(p):
            return StatementList(p[2], p[0])

        @self.pg.production('statementlist : statement')
        @self.pg.production('statementlist : loop_statement')
        @self.pg.production('statementlist : if_statement')
        @self.pg.production('statementlist : statementlist NEWLINE')
        def statementlist(p):
            if p[0].gettokentype() == 'statement':
                return StatementList(p[0])
            else:
                return StatementList(None, p[0])

        @self.pg.production('loop_statement : LOOP INTEGER OPEN_CRO NEWLINE statementlist NEWLINE CLOSE_CRO')
        def loop(p):
            return Loop(int(p[1].value), p[4])

        @self.pg.production('loop_statement : LOOP INTEGER NEWLINE OPEN_CRO NEWLINE statementlist NEWLINE CLOSE_CRO')
        def loop2(p):
            return Loop(int(p[1].value), p[5])

        @self.pg.production('loop_statement : WHILE expression OPEN_CRO NEWLINE statementlist NEWLINE CLOSE_CRO')
        def whileexp(p):
            return While(p[1], p[4])

        @self.pg.production('loop_statement : WHILE expression NEWLINE OPEN_CRO NEWLINE statementlist NEWLINE '
                            'CLOSE_CRO')
        def whileexp2(p):
            return While(p[1], p[5])

        @self.pg.production('if_statement : IF expression OPEN_CRO NEWLINE statementlist NEWLINE CLOSE_CRO')
        def ifexp(p):
            return If(p[1], p[4])

        @self.pg.production('if_statement : IF expression NEWLINE OPEN_CRO NEWLINE statementlist NEWLINE CLOSE_CRO')
        def ifexp2(p):
            return If(p[1], p[5])

        @self.pg.production('else_statement : ELSE OPEN_CRO NEWLINE statementlist NEWLINE CLOSE_CRO')
        def elseexp(p):
            return Else(p[3])

        @self.pg.production('else_statement : ELSE NEWLINE OPEN_CRO NEWLINE statementlist NEWLINE CLOSE_CRO')
        def elseexp2(p):
            return Else(p[4])

        @self.pg.production('elseif_statement : ELSEIF expression OPEN_CRO NEWLINE statementlist NEWLINE '
                            'CLOSE_CRO')
        def elseif(p):
            return ElseIfs(ElseIf(p[1], p[4]))

        @self.pg.production('elseif_statement : ELSEIF expression NEWLINE OPEN_CRO NEWLINE statementlist NEWLINE '
                            'CLOSE_CRO')
        def elseif2(p):
            return ElseIfs(ElseIf(p[1], p[5]))

        @self.pg.production('elseif_statement : elseif_statement elseif_statement')
        def elseif3(p):
            return p[0].add(p[1])

        @self.pg.production('if_statement : if_statement else_statement')
        def ifelse(p):
            if type(p[0]) == IfElse:
                error(errors.UNEXPECTEDSYNTAX, "Alone Else", {"type": ""})
                sys.exit(1)
            elif type(p[0]) == IfElseIf:
                return IfElseIfElse(If(p[0].ifcondition, p[0].ifstatementlist), p[0].elseifs, p[1])
            else:
                return IfElse(p[0], p[1])

        @self.pg.production('if_statement : if_statement elseif_statement')
        def ifelseif(p):
            if type(p[0]) == IfElse:
                error(errors.UNEXPECTEDSYNTAX, "Alone ElseIf", {"type": ""})
                sys.exit(1)
            return IfElseIf(p[0], p[1])

        @self.pg.production('statement : expression COMMENT')
        @self.pg.production('statement : expression')
        def statement(p):
            return Statement(p[0])

        @self.pg.production('statement : COMMENT')
        def statement(p):
            return Nothing()

        @self.pg.production('expression : IDENTIFIER EGAL expression')
        def programvar(p):
            if type(p[2]) == List:
                error(errors.EXPECTEDSYNTAX, "Expected hook around List.", {"type": "token",
                                                                            "token": p[0]})
                sys.exit(1)
            var = self.var.get(p[0].value)
            if var is not None:
                if type(var) == ListVar:
                    error(errors.INVALIDTYPE, "Cannot have basic type.", {"type": "token", "token": p[0]})
                    sys.exit(1)
                return AffectionVar(var, p[2])
            else:
                var = Variable(p[0].value, p[2])
                self.var.add(var)
            return var

        @self.pg.production('expression : IDENTIFIER EGAL CRO_OPEN CRO_CLOSE')
        def programvar2(p):
            var = self.var.get(p[0].value)
            if var is not None:
                if type(var) == Variable:
                    error(errors.INVALIDTYPE, "Cannot have complex type.", {"type": "token", "token": p[0]})
                    sys.exit(1)
                return AffectionVar(var, List())
            else:
                var = ListVar(p[0].value, List())
                self.var.add(var)
            return var

        @self.pg.production('expression : IDENTIFIER EGAL CRO_OPEN expression CRO_CLOSE')
        def programvar3(p):
            var = self.var.get(p[0].value)
            if var is not None:
                if type(var) == Variable:
                    error(errors.INVALIDTYPE, "Cannot have complex type.", {"type": "token", "token": p[0]})
                    sys.exit(1)
                return AffectionVar(var, List(p[3]))
            else:
                var = ListVar(p[0].value, List(p[3]))
                self.var.add(var)
            return var

        @self.pg.production('expression : IDENTIFIER POINT IDENTIFIER OPEN_PAREN CLOSE_PAREN')
        def membervar(p):
            var = self.var.get(p[0].value)
            if var is not None:
                return MemberType(p[2].value, var)
            else:
                error(errors.NOTDECLARED, "Variable is not declared.", {"type": "token", "token": p[0]})
                sys.exit(1)

        @self.pg.production('expression : IDENTIFIER POINT IDENTIFIER OPEN_PAREN expression CLOSE_PAREN')
        def membervar2(p):
            var = self.var.get(p[0].value)
            if var is not None:
                return MemberType(p[2].value, var, [p[4]])
            else:
                error(errors.NOTDECLARED, "Variable is not declared.", {"type": "token", "token": p[0]})
                sys.exit(1)

        @self.pg.production('expression : expression VIRGULE expression')
        def list(p):
            return List(p[0], p[2])

        @self.pg.production('expression : CANBE OPEN_PAREN expression VIRGULE STRING CLOSE_PAREN')
        def programfunc2(p):
            func = p[0]
            exp = p[2]
            if func.gettokentype() == 'CANBE':
                return CanBe(exp, p[4].value[1:-1])

        @self.pg.production('expression : INT OPEN_PAREN expression CLOSE_PAREN')
        @self.pg.production('expression : FLOATF OPEN_PAREN expression CLOSE_PAREN')
        @self.pg.production('expression : BOOL OPEN_PAREN expression CLOSE_PAREN')
        @self.pg.production('expression : STR OPEN_PAREN expression CLOSE_PAREN')
        @self.pg.production('expression : TYPE OPEN_PAREN expression CLOSE_PAREN')
        @self.pg.production('expression : PRINT OPEN_PAREN expression CLOSE_PAREN')
        @self.pg.production('expression : ENTER OPEN_PAREN STRING CLOSE_PAREN')
        def programfunc1(p):
            func = p[0]
            exp = p[2]
            if func.gettokentype() == "INT":
                return Int(exp)
            elif func.gettokentype() == "FLOATF":
                return Float(exp)
            elif func.gettokentype() == "BOOL":
                return Boolean(exp)
            elif func.gettokentype() == "STR":
                return Str(exp)
            elif func.gettokentype() == "TYPE":
                return Type(exp)
            elif func.gettokentype() == "PRINT":
                return Print(exp)
            else:
                return Input(exp.value)

        @self.pg.production('expression : EXIT OPEN_PAREN CLOSE_PAREN')
        @self.pg.production('expression : ENTER OPEN_PAREN CLOSE_PAREN')
        @self.pg.production('expression : PRINT OPEN_PAREN CLOSE_PAREN')
        def programfunc0(p):
            func = p[0]
            if func.gettokentype() == "EXIT":
                sys.exit(0)
            elif func.gettokentype() == "ENTER":
                return Input()
            else:
                return Print()

        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def expressionparen(p):
            return p[1]

        @self.pg.production('expression : IDENTIFIER INCREMENT')
        @self.pg.production('expression : IDENTIFIER DECREMENT')
        def uniqueop(p):
            var = self.var.get(p[0].value)
            if var is not None:
                if p[1].gettokentype() == "INCREMENT":
                    return Increment(var)
                else:
                    return Decrement(var)
            else:
                error(errors.NOTDECLARED, "Variable is not declared.", {"type": "token", "token": p[0]})
                sys.exit(1)

        @self.pg.production('expression : IDENTIFIER SUMAFF expression')
        @self.pg.production('expression : IDENTIFIER SUBAFF expression')
        @self.pg.production('expression : IDENTIFIER MULAFF expression')
        @self.pg.production('expression : IDENTIFIER DIVAFF expression')
        @self.pg.production('expression : IDENTIFIER MODAFF expression')
        @self.pg.production('expression : IDENTIFIER POWAFF expression')
        @self.pg.production('expression : IDENTIFIER DIVEUAFF expression')
        def affectionop(p):
            var = self.var.get(p[0].value)
            op = p[1]
            if var is not None:
                if op.gettokentype() == 'SUMAFF':
                    return SumAffector(var, p[2])
                elif op.gettokentype() == 'SUBAFF':
                    return SubAffector(var, p[2])
                elif op.gettokentype() == 'MULAFF':
                    return MulAffector(var, p[2])
                elif op.gettokentype() == 'MODAFF':
                    return ModAffector(var, p[2])
                elif op.gettokentype() == 'POWAFF':
                    return PowAffector(var, p[2])
                elif op.gettokentype() == 'DIVEUAFF':
                    return DivEuAffector(var, p[2])
                else:
                    return DivAffector(var, p[2])
            else:
                error(errors.NOTDECLARED, "Variable is not declared.", {"type": "token", "token": p[0]})
                sys.exit(1)

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        @self.pg.production('expression : expression MOD expression')
        @self.pg.production('expression : expression POW expression')
        @self.pg.production('expression : expression DIVEU expression')
        def binaryop(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'MUL':
                return Mul(left, right)
            elif operator.gettokentype() == 'MOD':
                return Mod(left, right)
            elif operator.gettokentype() == 'POW':
                return Pow(left, right)
            elif operator.gettokentype() == 'DIVEU':
                return DivEu(left, right)
            else:
                return Div(left, right)

        @self.pg.production('expression : expression AND expression')
        @self.pg.production('expression : expression OR expression')
        def logicoperators2(p):
            op = p[1]
            e1 = p[0]
            e2 = p[2]
            if op.gettokentype() == "AND":
                return And(e1, e2)
            else:
                return Or(e1, e2)

        @self.pg.production('expression : NOT expression')
        def logicoperator1(p):
            return ExpressionBase(Not(p[1]).eval(), "boolean")

        @self.pg.production('expression : expression IS expression')
        @self.pg.production('expression : expression LESS expression')
        @self.pg.production('expression : expression LESSE expression')
        @self.pg.production('expression : expression MORE expression')
        @self.pg.production('expression : expression MOREE expression')
        def comparators(p):
            c = p[1]
            e1 = p[0]
            e2 = p[2]
            if c.gettokentype() == "IS":
                return Egal(e1, e2)
            elif c.gettokentype() == "LESS":
                return Less(e1, e2)
            elif c.gettokentype() == "MORE":
                return More(e1, e2)
            elif c.gettokentype() == "LESSE":
                return LessOrEgal(e1, e2)
            else:
                return MoreOrEgal(e1, e2)

        @self.pg.production('expression : SUB expression')
        @self.pg.production('expression : SUM expression')
        def uniqueop(p):
            ope = p[0]
            exp = p[1]
            if ope.gettokentype() == 'SUM':
                return Sum(ExpressionBase(0, "integer"), exp)
            else:
                return Sub(ExpressionBase(0, "integer"), exp)

        @self.pg.production('expression : IDENTIFIER CRO_OPEN INTEGER CRO_CLOSE')
        def expressionlist(p):
            var = self.var.get(p[0].value)
            if var is not None:
                return var.get(int(p[2].value))
            else:
                error(errors.NOTDECLARED, "Variable is not declared.", {"type": "token", "token": p[0]})
                sys.exit(1)

        @self.pg.production('expression : FLOAT')
        @self.pg.production('expression : INTEGER')
        @self.pg.production('expression : STRING')
        @self.pg.production('expression : BOOLEAN')
        @self.pg.production('expression : IDENTIFIER')
        def expression(p):
            if p[0].gettokentype() == 'FLOAT':
                return ExpressionBase(float(p[0].value), "float")
            elif p[0].gettokentype() == 'STRING':
                return ExpressionBase(str(p[0].value)[1:-1], "string")
            elif p[0].gettokentype() == 'BOOLEAN':
                if p[0].value == "false":
                    return ExpressionBase(False, "boolean")
                return ExpressionBase(True, "boolean")
            elif p[0].gettokentype() == 'IDENTIFIER':
                var = self.var.get(p[0].value)
                if var is not None:
                    return ExpressionBase(var.value, var.kind, var)
                else:
                    error(errors.NOTDECLARED, "Variable is not declared.", {"type": "token", "token": p[0]})
                    sys.exit(1)
            else:
                return ExpressionBase(int(p[0].value), "integer")

        @self.pg.error
        def error_handle(token):
            print("Syntax unexcepted : \n - Position :", token.getsourcepos(),
                  "\n - Token : Valeur =", token.getstr(), "| Type =", token.gettokentype())
            sys.exit(1)

    def get_parser(self):
        parser = self.pg.build()
        return parser
