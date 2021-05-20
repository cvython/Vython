from rply import LexerGenerator


class Lexer:
    def __init__(self, tokens, values):
        self.lexer = LexerGenerator()
        self.tokens = tokens
        self.values = values

    def _add_tokens(self):
        for i in range(len(self.tokens)):
            self.lexer.add(self.tokens[i], self.values[i])
        # Ignore spaces
        self.lexer.ignore('\t+')
        self.lexer.ignore(r' +')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
