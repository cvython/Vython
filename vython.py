from Main.lexer import Lexer
from Main.parser import Parser
import sys

from arguments import create_argument_parser
from tokens import tokens

lexer = Lexer(list(tokens.keys()), list(tokens.values())).get_lexer()
parser_object = Parser(list(tokens.keys()))
parser_object.parse()
parser = parser_object.get_parser()

create_argument_parser(lexer, parser)

# if len(sys.argv) >= 2:
#     try:
#         with open(sys.argv[1]) as f:
#             text_input = f.read()
#             tokens = lexer.lex(text_input)
#             parser.parse(tokens)
#     except IOError:
#         pass
# else:
#     launched = True
#     while launched:
#         text_input = input(">>> ")
#         tokens = lexer.lex(text_input)
#         parser.parse(tokens)
