def debug(lexer, text_input): # ONLY TO DEBUG
    b = lexer.lex(text_input)
    for i in list(b):
        print(i)