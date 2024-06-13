import ply.lex as lex

reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE',
}

# List of token names.   This is always required
tokens = [
    'FLOAT',
    'INTEGER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'POWER',
    'LPAREN',
    'RPAREN',
    'ID',
] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_POWER = r'\*\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_FLOAT(t):
    r'-?(\.\d+|\d+\.\d*)'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\$[a-zA-Z_]\w*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# A regular expression rule with some action code
def t_INTEGER(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
23.45 3 % 4 ** 10
  + -20 *2
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
