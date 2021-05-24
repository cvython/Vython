import os

class ExecuteScript(object):
    def __init__(self, filename=None, from_file=True, content=None, error=None, lexer=None, parser=None):
        self.filename = filename
        self.from_file = from_file
        self.content = content
        self.error = error
        self.lexer = lexer
        self.parser = parser

        if self.from_file:
            if not os.path.isfile(self.filename):
                if self.error:
                    self.error(f'{self.filename} is not a file')
            with open(self.filename, 'r') as file_content_reader:
                self.content = file_content_reader.read()

        self.execute_script()

    def execute_script(self):
        tokens = self.lexer.lex(self.content)
        parser = self.parser.parse(tokens)