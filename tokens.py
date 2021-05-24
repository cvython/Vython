tokens = {
    'COMMENT': r'#.*',
    'NEWLINE': r'\n+',

    'STRING': r'(\"([^\\\n]|(\\.))*?\")|(\'([^\\\n]|(\\.))*?\')',
    'BOOLEAN': r'(true)|(false)',
    'FLOAT': r'-?\d+\.\d+',
    'INTEGER': r'-?\d+',

    'ELSEIF': r'(else if)|(elseif)',
    'IF': r'if',
    'OPEN_CRO': r'\{',
    'CLOSE_CRO': r'\}',
    'ELSE': r'else',

    'LOOP': r'loop',
    'WHILE': r'while',

    'AND': r'(and)|(&&)',
    'OR': r'(or)|(\|\|)',
    'NOT': r'(not)|(!)',

    'PRINT': r'show',
    'EXIT': r'exit',
    'ENTER': r'enter',
    'INT': r'int',
    'FLOATF': r'float',
    'STR': r'str',
    'TYPE': r'type',
    'BOOL': r'boolean',
    'CANBE': r'canbe',
    'VIRGULE': r',',

    'IS': r'\=\=',
    'LESSE': r'\<\=',
    'MOREE': r'\>\=',
    'LESS': r'\<',
    'MORE': r'\>',

    'INCREMENT': r'\+\+',
    'DECREMENT': r'\-\-',
    'SUMAFF': r'\+\=',
    'SUBAFF': r'\-\=',
    'MULAFF': r'\*\=',
    'DIVAFF': r'\/\=',
    'DIVEUAFF': r'\/\/\=',
    'MODAFF': r'\%\=',
    'POWAFF': r'\^\=',

    'SUM': r'\+',
    'SUB': r'\-',
    'MUL': r'\*',
    'DIV': r'\/',
    'DIVEU': r'\/\/',
    'MOD': r'\%',
    'POW': r'\^',

    'EGAL': r'\=',
    'IDENTIFIER': r"[a-zA-Z][a-zA-Z0-9]*",

    'OPEN_PAREN': r'\(',
    'CLOSE_PAREN': r'\)',
    'CRO_OPEN': r'\[',
    'CRO_CLOSE': r'\]',
    'POINT': r'\.'
}