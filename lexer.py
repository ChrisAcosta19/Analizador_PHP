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
    'DOT',

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
    'CALL',
    'STRING',

    # Peter Miranda
    'EQUALS',
    'PLUS_EQUALS',
    'MINUS_EQUALS',
    'TIMES_EQUALS',
    'DIVIDE_EQUALS',
    'MOD_EQUALS',
    'PLUS_PLUS',
    'MINUS_MINUS',
    'OPEN_TAG',
    'CLOSE_TAG',
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
t_DOT = r'\.'

# Assignment Operators - PM
t_EQUALS = r'\='
t_PLUS_EQUALS = r'\+\='
t_MINUS_EQUALS = r'\-\='
t_TIMES_EQUALS = r'\*\='
t_DIVIDE_EQUALS = r'\/='
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

#def PM
def t_ONE_LINE_COMMENT(t):
    r'//.*'
    #pass
    return t
    
def t_MULTI_LINE_COMMENT(t):
    r'/\*((?s:.*?))\*/'
    #pass
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
// Solicitud de datos en línea de comandos
echo "Introduce tu nombre: ";
$name = trim(fgets(STDIN));
echo "Introduce tu edad: ";
$age = (int)trim(fgets(STDIN));
echo "Introduce tu altura en metros (por ejemplo, 1.75): ";
$height = (float)trim(fgets(STDIN));
// Flotantes y operadores aritméticos
$weight = 70.5; // Peso en kilogramos
$bmi = $weight / ($height * $height); // Índice de Masa Corporal (IMC)
echo "Hola, $name. Tu IMC es " . $bmi . ".\n";
// Enumeraciones (simuladas con arrays)
$colors = ["RED", "GREEN", "BLUE"];
$favoriteColor = $colors[1]; // Asignando "GREEN"
echo "Tu color favorito es $favoriteColor.\n";
// Operadores lógicos y relacionales
$isAdult = ($age >= 18);
$isTall = ($height > 1.75);
if ($isAdult && $isTall) {
 echo "Eres adulto y alto.\n";
} elseif ($isAdult && !$isTall) {
 echo "Eres adulto pero no alto.\n";
} elseif (!$isAdult && $isTall) {
 echo "Eres alto pero no adulto.\n";
} else {
 echo "No eres ni adulto ni alto.\n";
}
// Operadores de asignación
$count = 0;
$count += 10; // Incremento en 10
$count -= 2; // Decremento en 2
$count *= 3; // Multiplicación por 3
$count /= 4; // División por 4
$count++; // Incremento en 1
$count--; // Decremento en 1
echo "El valor de count es $count.\n";
// Switch statement
echo "Introduce un número del 1 al 3: ";
$number = (int)trim(fgets(STDIN));
switch ($number) {
 case 1:
 echo "Elegiste el número uno.\n";
 break;
 case 2:
 echo "Elegiste el número dos.\n";
 break;
 case 3:
 echo "Elegiste el número tres.\n";
 break;
 default:
 echo "Número fuera de rango.\n";
 break;
}
/*
 Comentarios de múltiples líneas
 Ejemplo de bucles while y do-while
*/
// Bucle while
$i = 0;
while ($i < 3) {
 echo "While loop iteración: $i\n";
 $i++;
}
// Bucle do-while
$j = 0;
do {
 echo "Do-while loop iteración: $j\n";
 $j++;
} while ($j < 3);
// Otros operadores relacionales
$a = 5;
$b = 10;
$c = 5;
echo "a == b: " . var_export($a == $b, true) . "\n"; // false
echo "a != b: " . var_export($a != $b, true) . "\n"; // true
echo "a < b: " . var_export($a < $b, true) . "\n"; // true
echo "a > b: " . var_export($a > $b, true) . "\n"; // false
echo "a <= c: " . var_export($a <= $c, true) . "\n"; // true
echo "a >= c: " . var_export($a >= $c, true) . "\n"; // true
?>
'''

# Obtener la ubicación del script actual
script_dir = os.path.dirname(__file__)

# Crear carpeta 'logs' en la misma ubicación que el script
logs_dir = os.path.join(script_dir, 'logs')
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Generar nombre de archivo de log basado en la fecha y hora actual
git_username = "PeterMiranda"
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