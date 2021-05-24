import sys

from repl import Repl
from run import ExecuteScript


class ArgumentParserException(object):
    def __init__(self, message, suggestion=None, fatal=True):
        self.message = message
        self.suggestion = suggestion
        self.is_fatal = fatal

        self.raise_exception()

    def raise_exception(self):
        print(f'[ERROR] {self.message}')
        if self.suggestion:
            print(self.suggestion)

        if self.is_fatal:
            sys.exit(1)


class ArgumentParser(object):
    commands = None
    flags = []

    def __init__(self, arguments=sys.argv[1:]):
        self.arguments = arguments
        self.length = len(self.arguments)

    def create_argument_parser(self):
        for argument in self.arguments:
            if not argument.startswith('-'):
                if not self.commands:
                    self.commands = argument
                else:
                    exception = ArgumentParserException(
                        f'Invalid flag: {argument}',
                        'Flags should start with a comment')
                continue

            if argument[2:] not in self.flags:
                self.flags.append(argument[2:])
        return self.commands, self.flags


def create_argument_parser(lexer, parser):
    argument_parser = ArgumentParser()
    command, flags = argument_parser.create_argument_parser()
    if not command or command == 'repl':
        Repl('>>> ', lexer, parser)
    elif command == 'help':
        print("Showing help")
    else:
        ExecuteScript(command,
                      error=ArgumentParserException,
                      lexer=lexer,
                      parser=parser)
