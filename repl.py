class Repl(object):
    def __init__(self, prompt_message, lexer, parser):
        self.lexer = lexer
        self.parser = parser
        self.message = prompt_message

        self.create_repl()

    def create_repl(self):
        is_repl_launched = True
        while is_repl_launched:
            try:
                repl_input = input(self.message)
                tokens = self.lexer.lex(repl_input)
                parser = self.parser.parse(tokens)
            except KeyboardInterrupt:
                print("Your keyboard interrupted")
                is_repl_launched = False