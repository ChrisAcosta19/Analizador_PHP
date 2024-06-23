import ply.yacc as yacc
from lexer import tokens

# Reglas de producción
def p_statement(p):
    '''statement : print_statement
                 | fscanf_statement
                 | assignment_statement
                 | if_statement
                 | array_declaration_statement
                 | error'''
    p[0] = p[1]

# Gramática para PRINT

def p_print_statement(p):
    '''print_statement : ECHO LEFT_PAREN arguments RIGHT_PAREN SEMICOLON
                       | ECHO arguments SEMICOLON
                       | PRINT LEFT_PAREN argument RIGHT_PAREN SEMICOLON
                       | PRINT argument SEMICOLON'''
    operator = "echo"
    if p[1] == "print":
        operator = "print"
        if len(p) == 6: 
            p[0] = (operator, p[3])
        else:
            p[0] = (operator, p[2])

def p_arguments(p):
    '''arguments : argument
                 | arguments COMMA argument'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_argument(p):
    '''argument : INTEGER
                | STRING
                | ID'''
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

# Gramática para ASIGNACION
def p_assignment_statement(p):
    '''assignment_statement : ID EQUALS expression SEMICOLON'''
    p[0] = ('assignment', p[1], p[3])

def p_expression(p):
    '''expression : INTEGER
                  | STRING'''
    p[0] = p[1]

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
              | ID
              | LEFT_PAREN expression RIGHT_PAREN'''
    if isinstance(p[1], str) and p[1].startswith('$'):
        p[0] = ('variable', p[1])  
    elif isinstance(p[1], int):
        p[0] = ('integer', p[1])   
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

def p_condition(p):
    '''condition : expression
                 | condition LOGICAL_AND condition
                 | condition LOGICAL_OR condition
                 | condition RELATIONAL_OPERATOR condition
                 '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

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

def p_assignment_statement(p):
    '''assignment_statement : ID EQUALS expression SEMICOLON'''
    p[0] = ('assignment', p[1], p[3])

def p_expression_statement(p):
    '''expression_statement : expression SEMICOLON'''
    p[0] = p[1]

# Gramática para ERROR MSG
def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}'")
        return
    else:
        print("Syntax error at EOF")

# Gramática para ARRAYS

def p_array_declaration_statement(p):
    '''array_declaration_statement : ID EQUALS array SEMICOLON'''
    p[0] = ('array_declaration', p[1], p[3])

def p_array(p):
    '''array : LEFT_BRACKET array_elements RIGHT_BRACKET'''
    p[0] = p[2]

def p_array_elements(p):
    '''array_elements : array_element
                      | array_elements COMMA array_element'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_array_element(p):
    '''array_element : INTEGER
                     | STRING
                     | variable_access'''
    p[0] = p[1]

def p_variable_access(p):
    '''variable_access : ID'''
    p[0] = ('variable', p[1])

# Construir el parser
parser = yacc.yacc()

# EJEMPLOS

data1 = 'fscanf(STDIN, "%d %s", $var1, $var2);'
data2 = 'print "Hello, World!";'
data3 = '$var = 42;'
data4 = 'invalid_statement();'
data5 = '$a = (10 + 5);'
data6 = '$b = (20 - 3) * 2 / 4;'
data7 = '$c = $a + $b - 15;'
data8 = '''
if ($a > 10 && $b < 20) {
    $c = $a + $b;
} else {
    $c = $a - $b;
}
'''

data9 = '$a = [10, 20, 30];'

# PRUEBA

#result1 = parser.parse(data1)
#print(result1)  

result2 = parser.parse(data2)
print(result2)

result3 = parser.parse(data3)
print(result3)

result4 = parser.parse(data4)

result5 = parser.parse(data5)
print(result5)  

result6 = parser.parse(data6)
print(result6)  

result7 = parser.parse(data7)
print(result7) 

result8 = parser.parse(data8)
print(result8)

result9 = parser.parse(data9)
print(result9)

# type: ignore