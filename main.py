
from vython.lexer import Lexer
from vython.parser import Parser


from arguments import create_argument_parser
from tokens import tokens

lexer = Lexer(list(tokens.keys()), list(tokens.values())).get_lexer()
parser_object = Parser(list(tokens.keys()))
parser_object.parse()
parser = parser_object.get_parser()

create_argument_parser(lexer, parser)
