from rply.token import BaseBox
import sys
from Main.Errors import error, errors

class UniqueOp(BaseBox):
    def __init__(self, var):
        self.var = var


class Increment(UniqueOp):
    def eval(self):
        try:
            self.var.value = self.var.value + 1
            return self.var.value
        except:
            try:
                self.var.value = self.var.expression().increment()
                return self.var.value
            except:
                error(
                    errors.IMPOSSIBLEOPERATION, "", {
                        "type": "operationtype, var",
                        "operationtype": "Increase",
                        "var": self.var
                    })
                sys.exit(1)


class Decrement(UniqueOp):
    def eval(self):
        try:
            self.var.value = self.var.value - 1
            return self.var.value
        except:
            try:
                self.var.value = self.var.expression().decrement()
                return self.var.value
            except:
                error(
                    errors.IMPOSSIBLEOPERATION, "", {
                        "type": "operationtype, var",
                        "operationtype": "Decrease",
                        "var": self.var
                    })
                sys.exit(1)
