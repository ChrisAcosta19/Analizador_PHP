global log_file
import os
from datetime import datetime
import ply.lex as lex

reserved = {
    '__halt_compiler': 'HALT_COMPILER',
    'endif': 'ENDIF',
    'elseif': 'ELSEIF',
    'default': 'DEFAULT',
    'insteadof': 'INSTEADOF',
    'endforeach': 'ENDFOREACH',
    'declare': 'DECLARE',
    'match': 'MATCH',
    'goto': 'GOTO',
    'fn': 'FN',
    'endfor': 'ENDFOR',
    'continue': 'CONTINUE',
    'case': 'CASE',
    'if': 'IF',
    'else': 'ELSE',
    'break': 'BREAK',
    'while': 'WHILE',
    'echo': 'ECHO',
    'for': 'FOR',
    'foreach': 'FOREACH',
    'function': 'FUNCTION',
    'return': 'RETURN',
    'class': 'CLASS',
    'interface': 'INTERFACE',
    'extends': 'EXTENDS',
    'implements': 'IMPLEMENTS',
    'public': 'PUBLIC',
    'private': 'PRIVATE',
    'protected': 'PROTECTED',
    'static': 'STATIC',
    'final': 'FINAL',
    'abstract': 'ABSTRACT',
    'new': 'NEW',
    'try': 'TRY',
    'catch': 'CATCH',
    'throw': 'THROW',
    'finally': 'FINALLY',
    'instanceof': 'INSTANCEOF',
    'namespace': 'NAMESPACE',
    'use': 'USE',
    'require': 'REQUIRE',
    'include': 'INCLUDE',
    'const': 'CONST',
    'and': 'AND',
    'or': 'OR',
    'xor': 'XOR',
    'print': 'PRINT',
    'echo': 'ECHO',
    'var': 'VAR',
    'global': 'GLOBAL',
    'isset': 'ISSET',
    'empty': 'EMPTY',
    'unset': 'UNSET',
    'die': 'DIE',
    'exit': 'EXIT',
    'eval': 'EVAL',
    'include_once': 'INCLUDE_ONCE',
    'require_once': 'REQUIRE_ONCE',
    'yield': 'YIELD',
    'yield from': 'YIELD_FROM',
    'as': 'AS',
    'endswitch': 'ENDSWITCH',
    'callable': 'CALLABLE',
    'do': 'DO',
    'enddeclare': 'ENDDECLARE',
    'endwhile': 'ENDWHILE',
    'list': 'LIST',
    'trait': 'TRAIT',
    'switch': 'SWITCH',
    'null': 'NULL',
    'async': 'ASYNC',
    'await': 'AWAIT',
    'bool': 'BOOL',
    'clone': 'CLONE',
    'enum': 'ENUM',
    'iterable': 'ITERABLE',
    'mixed': 'MIXED',
    'object': 'OBJECT',
    'self': 'SELF',
    'string': 'STRING',
    'void': 'VOID',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'array' : 'ARRAY',
}

# List of token names.   This is always required
tokens = [
    # Christopher Acosta
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
    'KEY_VALUE',

    # Jefferson Eras
    'COMMA',
    'LOGICAL_NOT',
    'LOGICAL_AND',
    'LOGICAL_OR',
    'LOGICAL_XOR',
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_EQUAL',
    'GREATER_EQUAL',
    'PHP_OPEN_TAG',
    'PHP_CLOSE_TAG',
    'CALL',
    'STRING',
    # Peter Miranda


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
t_COMMA = r','
t_CALL = r'->'
t_KEY_VALUE = r'=>'

def t_PHP_OPEN_TAG(t):
    r'<\?php'
    return t


def t_PHP_CLOSE_TAG(t):
    r'\?>'
    return t


def t_FLOAT(t):
    r'-?(\.\d+|\d+\.\d*)'
    t.value = float(t.value)
    return t


def t_NAME(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'NAME')    # Check for reserved words
    return t


def t_ID(t):
    r'\$[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
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
    r'(\'[^\'\\]*(\\.[^\\]*)*\')|("[^"\\]*(\\.[^\\]*)*")'
    return t

def t_LOGICAL_AND(t):
    r'&&|and'
    return t


def t_LOGICAL_OR(t):
    r'\|\||or'
    return t


def t_LOGICAL_XOR(t):
    r'xor'
    return t

def t_LOGICAL_NOT(t):
    r'!'
    return t

# Comparison operators
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_EQUAL = r'<='
t_GREATER_EQUAL = r'>='

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t\r\n'


# Error handling rule
def t_error(t):
    error_message = "Carácter inesperado '%s' en la linea %d, columna %d" % (t.value[0], t.lexer.lineno, t.lexer.lexpos)
    log_file.write(error_message + '\n')
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
<?php
?> 
'''

# Obtener la ubicación del script actual
script_dir = os.path.dirname(__file__)

# Crear carpeta 'logs' en la misma ubicación que el script
logs_dir = os.path.join(script_dir, 'logs')
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Generar nombre de archivo de log basado en la fecha y hora actual
git_username = "ChrisAcosta19"
log_file_name = datetime.now().strftime(f'lexico-{git_username}-%d%m%Y-%Hh%M.txt')

# Abrir archivo de log para escritura en la carpeta 'logs'
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
print(f'Archivo de log generado: {log_file_name} en la carpeta {logs_dir}.')