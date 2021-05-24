def debug(lexer, text_input):  
    b = lexer.lex(text_input)
    for i in list(b):
        print(i)
