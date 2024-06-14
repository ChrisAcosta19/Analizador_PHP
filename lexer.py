import ply.lex as lex

reserved = {
    '__halt_compiler' : 'HALT_COMPILER',
    'endif' : 'ENDIF',
    'elseif' : 'ELSEIF',
    'default' : 'DEFAULT',
    'insteadof' : 'INSTEADOF',
    'endforeach' : 'ENDFOREACH',
    'declare' : 'DECLARE',
    'array' : 'ARRAY',
    'match' : 'MATCH',
    'goto' : 'GOTO',
    'fn' : 'FN',
    'endfor' : 'ENDFOR',
    'continue' : 'CONTINUE',
    'case' : 'CASE',
    'if' : 'IF',
    'else' : 'ELSE',
    'break' : 'BREAK',
    'while' : 'WHILE',
    'echo' : 'ECHO',
    'for' : 'FOR',
    'foreach' : 'FOREACH',
    'function' : 'FUNCTION',
    'return' : 'RETURN',
    'class' : 'CLASS',
    'interface' : 'INTERFACE',
    'extends' : 'EXTENDS',
    'implements' : 'IMPLEMENTS',
    'public' : 'PUBLIC',
    'private' : 'PRIVATE',
    'protected' : 'PROTECTED',
    'static' : 'STATIC',
    'final' : 'FINAL',
    'abstract' : 'ABSTRACT',
    'new' : 'NEW',
    'try' : 'TRY',
    'catch' : 'CATCH',
    'throw' : 'THROW',
    'finally' : 'FINALLY',
    'instanceof' : 'INSTANCEOF',
    'namespace' : 'NAMESPACE',
    'use' : 'USE',
    'require' : 'REQUIRE',
    'include' : 'INCLUDE',
    'const' : 'CONST',
    'and' : 'AND',
    'or' : 'OR',
    'xor' : 'XOR',
    'print' : 'PRINT',
    'echo' : 'ECHO',
    'var' : 'VAR',
    'global' : 'GLOBAL',
    'isset' : 'ISSET',
    'empty' : 'EMPTY',
    'unset' : 'UNSET',
    'die' : 'DIE',
    'exit' : 'EXIT',
    'eval' : 'EVAL',
    'include_once' : 'INCLUDE_ONCE',
    'require_once' : 'REQUIRE_ONCE',
    'yield' : 'YIELD',
    'yield from' : 'YIELD_FROM',
    'as' : 'AS',
    'endswitch' : 'ENDSWITCH',
    'callable' : 'CALLABLE',
    'do' : 'DO',
    'enddeclare' : 'ENDDECLARE',
    'endwhile' : 'ENDWHILE',
    'list' : 'LIST',
    'trait' : 'TRAIT',
    'switch' : 'SWITCH',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'null' : 'NULL',
}

# List of token names.   This is always required
tokens = [
    'ID',
    'NAME',
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

def t_NAME(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t

def t_ID(t):
    r'\$[a-zA-Z_]\w*'
    t.type = reserved.get(t.value[1:],'ID')    # Check for reserved words
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
    print("Carácter inesperado '%s' en la linea %d, columna %d" %
           (t.value[0], t.lexer.lineno, t.lexer.lexpos))
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
greet 20.34 3 % 4 ** 10
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
