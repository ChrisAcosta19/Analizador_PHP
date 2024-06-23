import ply.yacc as yacc
from lexer import tokens

# Reglas de producción
def p_statement(p):
    '''statement : print_statement
                 | fscanf_statement
                 | assignment_statement
                 | if_statement
                 | array_declaration_statement'''
    p[0] = p[1]

# Gramática para INPUT
###fscanf(STDIN, "formato", $variables...)
def p_fscanf_statement(p):
    '''fscanf_statement : FSCANF LEFT_PAREN STDIN COMMA STRING COMMA variable_list RIGHT_PAREN SEMICOLON'''
    p[0] = ('fscanf', p[3], p[5], p[7])

def p_variable_list(p):
    '''variable_list : variable
                     | variable_list COMMA variable'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_variable(p):
    '''variable : ID'''
    p[0] = p[1]

# Gramática para PRINT
def p_print_statement(p):
    '''print_statement : ECHO LEFT_PAREN arguments RIGHT_PAREN SEMICOLON
                       | ECHO arguments SEMICOLON
                       | PRINT LEFT_PAREN arguments RIGHT_PAREN SEMICOLON
                       | PRINT arguments SEMICOLON'''
    operator = "echo"
    if p[1] == "print":
        operator = "print"
        if len(p) == 6: 
            p[0] = (operator, p[3])
        else:
            p[0] = (operator, p[2])

def p_arguments(p):
    '''arguments : argument
                 | arguments DOT argument'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_argument(p):
    '''argument : INTEGER
                | FLOAT
                | variable
                | TRUE
                | FALSE
                | STRING
                | expression'''
    p[0] = p[1]

# Gramática para ASIGNACION
def p_assignment_statement(p):
    '''assignment_statement : variable EQUALS argument SEMICOLON'''
    p[0] = ('assignment', p[1], p[3])

# Gramática para OPERACIONES + & -
def p_expression_arithmetic(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_factor(p):
    '''factor : INTEGER
              | FLOAT
              | variable
              | LEFT_PAREN expression RIGHT_PAREN'''
    if isinstance(p[1], str) and p[1].startswith('$'):
        p[0] = ('variable', p[1])  
    elif isinstance(p[1], int):
        p[0] = ('integer', p[1])
    elif isinstance(p[1], float):
        p[0] = ('float', p[1])   
    else:
        p[0] = p[2]    
     
# Gramática para IF
def p_if_statement(p):
    '''if_statement : IF LEFT_PAREN condition RIGHT_PAREN block
                    | IF LEFT_PAREN condition RIGHT_PAREN block ELSE block'''
    if len(p) == 6:
        p[0] = ('if', p[3], p[5])
    else:
        p[0] = ('if-else', p[3], p[5], p[7])

def p_block(p):
    '''block : LEFT_BRACE statements RIGHT_BRACE'''
    p[0] = p[2]

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_relational_operator(p):
    '''relational_operator : EQUAL_TO
                           | NOT_EQUAL_TO
                           | LESS_THAN
                           | GREATER_THAN
                           | LESS_EQUAL
                           | GREATER_EQUAL
                           | IDENTICAL_TO
                           | NOT_IDENTICAL_TO
                           | DIFFERENT'''
    p[0] = p[1]

def p_condition(p):
    '''condition : TRUE
                 | FALSE
                 | expression relational_operator expression
                 | condition LOGICAL_AND condition
                 | condition LOGICAL_OR condition
                 | condition LOGICAL_XOR condition
                 | LOGICAL_NOT condition'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = (p[2], p[1], p[3])

# Gramática para ERROR MSG
def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}'")
        return
    else:
        print("Syntax error at EOF")

# Gramática para ARRAYS

def p_array_declaration_statement(p):
    '''array_declaration_statement : variable EQUALS array SEMICOLON'''
    p[0] = ('array_declaration', p[1], p[3])

def p_array(p):
    '''array : ARRAY LEFT_PAREN array_elements RIGHT_PAREN'''
    p[0] = p[3]

def p_array_elements(p):
    '''array_elements : argument
                      | array_elements COMMA argument'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

# Construir el parser
parser = yacc.yacc()

# EJEMPLOS
data = [
    'fscanf(STDIN, "%d %s", $var1, $var2);',
    'print "Hello, World!";',
    '$var = 42;',
    'invalid_statement();',
    '$a = (10 + 5);',
    '$b = (20 - 3) * 2 / 4;',
    '$c = $a + $b - 15;',
    '''
    if ($a > 10 && $b < 20) {
        $c = $a + $b;
    } else {
        $c = $a - $b;
    }
    ''',
    '$a = array(10, 20, 30);'
]

linea = 1
for d in data:
    result = parser.parse(d)
    print(linea, result)
    linea += 1

# type: ignore