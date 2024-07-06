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
                  | function_statement
                  | ONE_LINE_COMMENT
                  | MULTI_LINE_COMMENT
                  | class_declaration'''
    p[0] = p[1]

# Reglas de producción
def p_statement(p):
    '''statement : print_statement
                 | fscanf_statement
                 | fgets_statement
                 | assignment_statement
                 | array_declaration_statement
                 | BREAK
                 | CONTINUE
                 | function_call
                 | return_statement'''
    p[0] = p[1]

# Gramática para funciones de la forma básica (sin argumentos por defecto)
# Gramática para funciones con argumentos por defecto
def p_function_statement(p):
    '''function_statement : FUNCTION NAME LEFT_PAREN array_elements RIGHT_PAREN block
                          | FUNCTION NAME LEFT_PAREN RIGHT_PAREN block'''
    if len(p) == 8:
        p[0] = ('function', p[2], p[4], p[6])
    else:
        p[0] = ('function', p[2], [], p[5])

# Gramática para funciones anónimas (closures)
def p_anonymous_function(p):
    '''anonymous_function : FUNCTION LEFT_PAREN array_elements RIGHT_PAREN block
                          | FUNCTION LEFT_PAREN RIGHT_PAREN block'''
    if len(p) == 6:
        p[0] = ('anonymous_function', p[3], p[5])
    else:
        p[0] = ('anonymous_function', [], p[4])

def p_return_statement(p):
    '''return_statement : RETURN arguments'''
    p[0] = (p[1], p[2])

def p_function_call(p):
    '''function_call : function_name LEFT_PAREN arguments RIGHT_PAREN
                     | function_name LEFT_PAREN RIGHT_PAREN'''
    if len(p) == 5:
        p[0] = (p[1], p[3])
    else:
        p[0] = (p[1], [])

def p_function_name(p):
    '''function_name : NAME
                     | variable'''
    p[0] = p[1]

# Gramática para INPUT
###fgets(STDIN)
def p_fgets_statement(p):
    '''fgets_statement : FGETS LEFT_PAREN STDIN RIGHT_PAREN'''
    p[0] = (p[1], p[3])

###fscanf(STDIN, "formato", $variables...)
def p_fscanf_statement(p):
    '''fscanf_statement : FSCANF LEFT_PAREN STDIN COMMA STRING COMMA variable_list RIGHT_PAREN'''
    p[0] = (p[1], p[3], p[5], p[7])

def p_variable_list(p):
    '''variable_list : variable
                     | variable_list COMMA variable'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_variable(p):
    '''variable : ID
                | ID CALL NAME'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[2], p[3])

# Gramática para ASIGNACION
def p_assignment_statement(p):
    '''assignment_statement : variable assignment_operator argument
                            | variable PLUS_PLUS
                            | variable MINUS_MINUS'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = (p[2], p[1])

def p_assignment_operator(p):
    '''assignment_operator : EQUALS
                           | PLUS_EQUALS
                           | MINUS_EQUALS
                           | TIMES_EQUALS
                           | DIVIDE_EQUALS
                           | MOD_EQUALS'''
    p[0] = p[1]

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
                 | arguments DOT argument
                 | arguments COMMA argument'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_argument(p):
    '''argument : STRING                
                | expression
                | array
                | array_indexing
                | function_call
                | variable CALL function_call
                | anonymous_function
                | assignment_statement
                | fgets_statement
                | object_creation
                | casting argument'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = (p[1], p[2], p[3])

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
              | condition
              | LEFT_PAREN expression RIGHT_PAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

# Gramática para IF
def p_if_statement(p):
    '''if_statement : IF parenthesized_condition block
                    | IF parenthesized_condition block else_if_extended
                    | IF parenthesized_condition block else_if_extended if_part3
                    | IF parenthesized_condition block if_part3'''
    if len(p) == 4:
        p[0] = (p[1], p[2], p[3])
    elif len(p) == 5:
        p[0] = (p[1], p[2], p[3], p[4])
    else:
        p[0] = (p[1], p[2], p[3], p[4], p[5])

def p_else_if_extended(p):
    '''else_if_extended : if_part2
                        | else_if_extended if_part2'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_else_if_statement(p):
    'if_part2 : ELSEIF parenthesized_condition block'
    p[0] = (p[1], p[2], p[3])

def p_else_statement(p):
    'if_part3 : ELSE block'
    p[0] = (p[1], p[2])

# Gramática para WHILE
def p_while_statement(p):
    '''while_statement : WHILE parenthesized_condition block'''
    p[0] = (p[1], p[2], p[3])

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
    '''condition : simple_condition
                 | negated_condition
                 | complex_condition
                 | parenthesized_condition'''
    p[0] = p[1]

def p_simple_condition(p):
    '''simple_condition : TRUE
                        | FALSE
                        | variable
                        | relational_expression'''
    p[0] = p[1]

def p_negated_condition(p):
    'negated_condition : LOGICAL_NOT condition'
    p[0] = (p[1], p[2])

def p_complex_condition(p):
    'complex_condition : condition logical_operator condition'
    p[0] = (p[2], p[1], p[3])

def p_parenthesized_condition(p):
    'parenthesized_condition : LEFT_PAREN condition RIGHT_PAREN'
    p[0] = p[2]

def p_relational_expression(p):
    '''relational_expression : expression relational_operator expression'''
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

def p_casting(p):
    'casting : LEFT_PAREN casting_type RIGHT_PAREN'
    p[0] = p[2]

def p_casting_type(p):
    '''casting_type : INT_TYPE
                    | FLOAT_TYPE'''
    p[0] = p[1]

# Gramática para ARRAYS
def p_array_declaration_statement(p):
    '''array_declaration_statement : variable EQUALS array'''
    p[0] = ('array_declaration', p[1], p[3])

def p_array(p):
    '''array : ARRAY LEFT_PAREN array_elements RIGHT_PAREN
             | LEFT_BRACKET array_elements RIGHT_BRACKET'''
    if len(p) == 5:
        p[0] = p[3]
    else:
        p[0] = p[2]

def p_array_elements(p):
    '''array_elements : array_argument
                      | array_elements COMMA array_argument'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

# Gramática para argumentos de arrays asociativos e indexados
def p_array_argument(p):
    '''array_argument : argument
                      | clave KEY_VALUE argument'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[3])

def p_clave(p):
    '''clave : STRING
             | INTEGER'''
    p[0] = p[1]

def p_array_indexing(p):
    '''array_indexing : variable LEFT_BRACKET INTEGER RIGHT_BRACKET'''
    p[0] = ('array_indexing', p[1], p[3])

def p_class_declaration(p):
    '''class_declaration : CLASS NAME LEFT_BRACE class_statements RIGHT_BRACE
                         | CLASS NAME LEFT_BRACE RIGHT_BRACE'''
    if len(p) == 6:
        p[0] = ('class', p[2], p[4])
    else:
        p[0] = ('class', p[2], [])

def p_class_statements(p):
    '''class_statements : class_statement
                        | class_statements class_statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_class_statement(p):
    '''class_statement : method_declaration
                       | property_declaration
                       | ONE_LINE_COMMENT
                       | MULTI_LINE_COMMENT'''
    p[0] = p[1]

def p_method_declaration(p):
    '''method_declaration : visibility_operator function_statement'''
    p[0] = ('method', p[1], p[2])

def p_property_declaration(p):
    '''property_declaration : visibility_operator variable SEMICOLON'''
    p[0] = ('property', p[1], p[2])

def p_visibility_operator(p):
    '''visibility_operator : PUBLIC
                           | PRIVATE
                           | PROTECTED'''
    p[0] = p[1]

def p_object_creation(p):
    '''object_creation : NEW NAME LEFT_PAREN RIGHT_PAREN
                       | NEW NAME LEFT_PAREN arguments RIGHT_PAREN'''
    if len(p) == 5:
        p[0] = (p[1], p[2])
    else:
        p[0] = (p[1], p[2], p[4])

# Gramática para ERROR MSG
def p_error(p):
    if p:
        print(f"Syntax error at token {p}")
        log_file.write(f'{p}\n')
        return
    else:
        print("Syntax error at EOF")

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