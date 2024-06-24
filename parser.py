import os
import ply.yacc as yacc
from datetime import datetime
from lexer import tokens, data, logs_dir, git_username
global log_file

def p_program(p):
    '''program : OPEN_TAG statements CLOSE_TAG'''
    p[0] = p[2]

def p_statements(p):
    '''statements : statement2
                  | statements statement2'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_statement2(p):
    '''statement2 : statement SEMICOLON
                  | if_statement
                  | while_statement
                  | for_statement
                  | ONE_LINE_COMMENT
                  | MULTI_LINE_COMMENT'''
    p[0] = p[1]

# Reglas de producción
def p_statement(p):
    '''statement : print_statement
                 | fscanf_statement
                 | fgets_statement
                 | assignment_statement
                 | array_declaration_statement
                 | BREAK
                 | CONTINUE'''
    p[0] = p[1]

# Gramática para INPUT
###fgets(STDIN)
def p_fgets_statement(p):
    '''fgets_statement : FGETS LEFT_PAREN STDIN RIGHT_PAREN'''
    p[0] = ('fgets', p[3])

###fscanf(STDIN, "formato", $variables...)
def p_fscanf_statement(p):
    '''fscanf_statement : FSCANF LEFT_PAREN STDIN COMMA STRING COMMA variable_list RIGHT_PAREN'''
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

def p_assignment_operator(p):
    '''assignment_operator : EQUALS
                           | PLUS_EQUALS
                           | MINUS_EQUALS
                           | TIMES_EQUALS
                           | DIVIDE_EQUALS
                           | MOD_EQUALS'''
    p[0] = p[1]

# Gramática para ASIGNACION
def p_assignment_statement(p):
    '''assignment_statement : variable assignment_operator argument
                             | variable PLUS_PLUS
                             | variable MINUS_MINUS'''
    if len(p) == 4:
        p[0] = ('assignment', p[1], p[2], p[3])
    else:
        p[0] = ('increment', p[1], p[2])

# Gramática para PRINT
def p_print_statement(p):
    '''print_statement : print_function LEFT_PAREN arguments RIGHT_PAREN
                       | print_function arguments'''
    if len(p) == 6:
        p[0] = (p[1], p[3])
    else:
        p[0] = (p[1], p[2])

def p_print_function(p):
    '''print_function : PRINT
                      | ECHO'''
    p[0] = p[1]

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
                | STRING
                | variable                
                | expression
                | condition
                | assignment_statement'''
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

# Gramática para WHILE
def p_while_statement(p):
    '''while_statement : WHILE LEFT_PAREN condition RIGHT_PAREN block'''
    p[0] = ('while', p[3], p[5])

# Gramática para FOR
def p_for_part1(p):
    '''for_part1 : FOR LEFT_PAREN assignment_list SEMICOLON
                 | FOR LEFT_PAREN SEMICOLON'''
    if len(p) == 5:
        p[0] = (p[1], p[3])
    else:
        p[0] = p[1]

def p_for_part2(p):
    '''for_statement : for_part1 condition for_part3
                     | for_part1 for_part3'''
    if len(p) == 4:
        p[0] = (p[1], p[2], p[3])
    else:
        p[0] = (p[1], p[2])

def p_for_part3(p):
    '''for_part3 : SEMICOLON statement_list RIGHT_PAREN for_part4
                 | SEMICOLON RIGHT_PAREN for_part4'''
    if len(p) == 5:
        p[0] = (p[2], p[4])
    else:
        p[0] = (p[3])

def p_for_part4(p):
    '''for_part4 : block
                 | SEMICOLON'''
    p[0] = p[1]

def p_assignment_list(p):
    '''assignment_list : assignment_statement
                       | assignment_list COMMA assignment_statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list COMMA statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_block(p):
    '''block : LEFT_BRACE statements RIGHT_BRACE
             | LEFT_BRACE RIGHT_BRACE'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = []

def p_condition(p):
    '''condition : TRUE
                 | FALSE
                 | expression relational_operator expression
                 | condition logical_operator condition
                 | LOGICAL_NOT condition
                 | LEFT_PAREN condition RIGHT_PAREN'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = (p[2], p[1], p[3])

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

def p_logical_operator(p):
    '''logical_operator : LOGICAL_AND
                        | LOGICAL_OR
                        | LOGICAL_XOR'''
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
    '''array_declaration_statement : variable EQUALS array'''
    p[0] = ('array_declaration', p[1], p[3])

def p_array(p):
    '''array : ARRAY LEFT_PAREN array_elements RIGHT_PAREN
             | LEFT_BRACKET array_elements RIGHT_BRACKET'''
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

# Generar nombre de archivo de log basado en la fecha y hora actual
log_file_name = datetime.now().strftime(f'sintactico-{git_username}-%d%m%Y-%Hh%M.txt')

# Abrir archivo de log para escritura en la carpeta 'logs'
with open(os.path.join(logs_dir, log_file_name), 'w', encoding='UTF-8') as log_file:
    result = parser.parse(data)
    for line in result:
        log_file.write(f'{line}\n')

# Mensaje de confirmación
print(f'Archivo de log generado: {log_file_name} en la carpeta\n {logs_dir}.')

# type: ignore