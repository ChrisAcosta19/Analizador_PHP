import os
from datetime import datetime
import ply.lex as lex
#from test import data

reserved = {
    'elseif': 'ELSEIF',
    'continue': 'CONTINUE',
    'if': 'IF',
    'else': 'ELSE',
    'break': 'BREAK',
    'while': 'WHILE',
    'for': 'FOR',
    'return': 'RETURN',
    'class': 'CLASS',
    'public': 'PUBLIC',
    'private': 'PRIVATE',
    'protected': 'PROTECTED',
    'new': 'NEW',
    'print': 'PRINT',
    'function': 'FUNCTION',
    'fgets' : 'FGETS',
    'STDIN' : 'STDIN',
    'fscanf' : 'FSCANF',
    'echo': 'ECHO',
    'unset': 'UNSET',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'array' : 'ARRAY',
    'int' : 'INT_TYPE',
    'float' : 'FLOAT_TYPE',
    'return': 'RETURN',
    'count': 'COUNT',
}

# List of token names.   This is always required
tokens = [
    'ID',
    'NAME',
    'FLOAT',
    'INTEGER',
    'EQUAL_TO',
    'NOT_EQUAL_TO',
    'IDENTICAL_TO',
    'NOT_IDENTICAL_TO',
    'DIFFERENT',
    'COMMA',
    'LOGICAL_NOT',
    'LOGICAL_AND',
    'LOGICAL_OR',
    'LOGICAL_XOR',
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_EQUAL',
    'GREATER_EQUAL',
    'CALL',
    'STRING',
    'OPEN_TAG',
    'CLOSE_TAG',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'POWER',
    'KEY_VALUE',
    'DOT',
    
    # Peter Miranda
    'EQUALS',
    'PLUS_EQUALS',
    'MINUS_EQUALS',
    'TIMES_EQUALS',
    'DIVIDE_EQUALS',
    'MOD_EQUALS',
    'PLUS_PLUS',
    'MINUS_MINUS',
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'LEFT_BRACKET',
    'RIGHT_BRACKET',
    'LEFT_PAREN',
    'RIGHT_PAREN',
    'SEMICOLON',
    'ONE_LINE_COMMENT',
    'MULTI_LINE_COMMENT',
] + list(reserved.values())

# Comparison operators
t_IDENTICAL_TO = r'==='
t_NOT_IDENTICAL_TO = r'!=='
t_NOT_EQUAL_TO = r'!='
t_EQUAL_TO = r'=='
t_LESS_EQUAL = r'<='
t_GREATER_EQUAL = r'>='
t_DIFFERENT = r'<>'
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'

# Regular expression rules for simple tokens
t_POWER = r'\*\*'
t_MOD = r'%'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_COMMA = r','
t_CALL = r'->'
t_KEY_VALUE = r'=>'
t_DOT = r'\.'
t_LOGICAL_NOT = r'!'

# Assignment Operators - PM
t_EQUALS = r'\='
t_PLUS_EQUALS = r'\+\='
t_MINUS_EQUALS = r'\-\='
t_TIMES_EQUALS = r'\*\='
t_DIVIDE_EQUALS = r'\/\='
t_MOD_EQUALS = r'\%\='
t_PLUS_PLUS = r'\+\+'
t_MINUS_MINUS = r'\-\-'

# Delimiters - PM
t_OPEN_TAG = r'<\?php'
t_CLOSE_TAG = r'\?>'

t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'

t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'

t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'

t_SEMICOLON = r'\;'

#DEFS
def t_ID(t):
    r'\$[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t

def t_FLOAT(t):
    r'-?(\.\d+|\d+\.\d*)'
    t.value = float(t.value)
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

# Jefferson Eras
def t_STRING(t):
    r'(?:(?:"[^"\\]*(?:\\.[^"\\]*)*")|(?:\'[^\'\\]*(?:\\.[^\'\\]*)*\'))'
    return t

def t_LOGICAL_AND(t):
    r'&& | and'
    return t

def t_LOGICAL_OR(t):
    r'\|\| | or'
    return t

def t_LOGICAL_XOR(t):
    r'xor'
    return t

def t_NAME(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'NAME')    # Check for reserved words
    return t

#def PM
def t_ONE_LINE_COMMENT(t):
    r'//.*|\#.*'
    return t
    
def t_MULTI_LINE_COMMENT(t):
    r'/\*((?s:.*?))\*/'
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    log_file.write("Error Léxico: Carácter inesperado '%s' en la linea %d, columna %d\n" % (t.value[0], t.lexer.lineno, t.lexer.lexpos))
    t.lexer.skip(1)

def analizar_lexico(data):
    # Build the lexer
    lexer = lex.lex()

    # Obtener la ubicación del script actual
    script_dir = os.path.dirname(__file__)

    # Crear carpeta 'logs' en la misma ubicación que el script
    logs_dir = os.path.join(script_dir, 'logs')
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Generar nombre de archivo de log basado en la fecha y hora actual
    git_username = "ChrisAcosta19"

    # log_file_name = datetime.now().strftime(f'lexico-{git_username}-%d%m%Y-%Hh%M.txt')
    log_file_name = 'lexico.txt'

    # Abrir archivo de log para escritura en la carpeta 'logs'
    global log_file
    with open(os.path.join(logs_dir, log_file_name), 'w', encoding='UTF-8') as log_file:
        # Darle al lexer la entrada
        lexer.input(data)

        # Tokenizar
        while True:
            tok = lexer.token()
            if not tok:
                break      # No hay más entrada
            # Escribir token en archivo de log
            log_file.write(f'{tok}\n')

    # Mensaje de confirmación
    print(f'Archivo de log generado: {log_file_name} en la carpeta\n {logs_dir}.')