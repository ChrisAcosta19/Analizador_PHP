import os
import ply.yacc as yacc
from datetime import datetime
from lexerPHP import tokens, logs_dir, git_username, reserved
from test import data
global log_file

# Agregar las variables declaradas en un diccionario
variables = {}
defined_functions = {}
php_functions = ['trim', 'var_export']

# Regla semántica: Una variable debe ser inicializada antes de ser usada
def validar_inicializacion_variables(p, indice):
    if not isinstance(p[indice], str) or p[indice] in variables:
        return True
    else:
        log_file.write(f"Error semántico: Variable {p[indice]} no ha sido inicializada\n")
        return False

# Verificar si un string es un número   
def esNumero(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Gramática para el programa principal
def p_program(p):
    '''program : OPEN_TAG statements CLOSE_TAG'''
    p[0] = p[2]

# Gramática para lista de sentencias
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

def p_statement(p):
    '''statement : print_statement
                 | fscanf_statement
                 | fgets_statement
                 | assignment_statement
                 | array_declaration_statement
                 | BREAK
                 | CONTINUE
                 | function_call
                 | return_statement
                 | array_indexing
                 | array_add_element
                 | array_modify_element
                 | array_remove_element
                 | array_count_elements
                 | expression'''
    p[0] = p[1]

# Gramática para funciones con/sin argumentos
# Función para verificar la definición de una función
def check_function_definition(func_name, params, block):
    if func_name in defined_functions:
        log_file.write(f"Error semántico: La función '{func_name}' ya ha sido definida.\n")
        return False
    
    defined_functions[func_name] = {
        'params': params,
        'block': block
    }
    return True

# Función para verificar la llamada a una función
def check_function_call(func_name, args):
    if func_name in php_functions:
        return True

    if func_name not in defined_functions:
        log_file.write(f"Error semántico: La función '{func_name}' no está definida.\n")
        return False
    
    # Regla_Semantica = El numero de argumentos debe ser igual al numero de parametros de la funcion definida.
    expected_params = defined_functions[func_name]['params']
    if len(args) != len(expected_params):
        log_file.write(f"Error semántico: La función '{func_name}' espera {len(expected_params)} argumentos, se encontraron {len(args)}.\n")
        return False
    return True

def p_function_statement(p):
    '''function_statement : FUNCTION NAME LEFT_PAREN parameters RIGHT_PAREN block
                          | FUNCTION NAME LEFT_PAREN RIGHT_PAREN block'''
    if len(p) == 7:
        check_function_definition(p[2], p[4], p[6])
        p[0] = ('function', p[2], p[4], p[6])
    else:
        check_function_definition(p[2], [], p[5])
        p[0] = ('function', p[2], [], p[5])


# Gramática para funciones anónimas (closures)
def p_anonymous_function(p):
    '''anonymous_function : FUNCTION LEFT_PAREN parameters RIGHT_PAREN block
                          | FUNCTION LEFT_PAREN RIGHT_PAREN block'''
    if len(p) == 6:
        p[0] = ('anonymous_function', p[3], p[5])
    else:
        p[0] = ('anonymous_function', [], p[4])

def p_parameters(p):
    '''parameters : parameter
                  | parameters COMMA parameter'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_parameter(p):
    '''parameter : variable
                 | variable EQUALS argument'''
    if len(p) == 2:
        p[0] = p[1]
        # Guardar parámetro sin valor en el diccionario
        variables[p[1]] = None
    else:
        p[0] = (p[1], p[3])
        # Guardar parámetro con valor en el diccionario
        variables[p[1]] = p[3]

def p_return_statement(p):
    '''return_statement : RETURN arguments'''
    p[0] = (p[1], p[2])

# Gramática para llamadas a funciones
def p_function_call(p):
    '''function_call : NAME LEFT_PAREN arguments RIGHT_PAREN
                     | NAME LEFT_PAREN RIGHT_PAREN'''
    if len(p) == 5:    
        check_function_call(p[1], p[3])
        p[0] = ('function_call', p[1], p[3])
    else:
        check_function_call(p[1], [])
        p[0] = ('function_call', p[1], [])

# Gramática para INPUT
## fgets(STDIN)
def p_fgets_statement(p):
    '''fgets_statement : FGETS LEFT_PAREN STDIN RIGHT_PAREN'''
    p[0] = (p[1], p[3])

## fscanf(STDIN, "formato", $variables...)
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

# Gramática para VARIABLES
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
        p[0] = (p[1], p[2], p[3])

        if p[2] == '=':
            variables[p[1]] = p[3]
        elif isinstance(p[3], str):
            # Regla semántica: Solo se puede usar +=, -=, *=, /=, %= con números
            log_file.write(f"Error semántico: {p[3]} no es un número, por lo que no se puede usar +=, -=, *=, /=, %= para modificar una variable\n")
        else:
            if validar_inicializacion_variables(p, 1):
                if isinstance(variables[p[1]], str):
                    if esNumero(variables[p[1]][1:-1]):
                        variables[p[1]] = float(variables[p[1]][1:-1])
                    else:
                        # Regla semántica: La variable a hacerle +=, -=, *=, /=, %= debe ser un número
                        log_file.write(f"Error semántico: {p[1]} no es un número, por lo que no se puede hacer +=, -=, *=, /=, %= sobre ella\n")
                        return

                if p[2] == '+=':
                    variables[p[1]] += p[3]
                elif p[2] == '-=':
                    variables[p[1]] -= p[3]
                elif p[2] == '*=':
                    variables[p[1]] *= p[3]
                elif p[2] == '/=':
                    variables[p[1]] /= p[3]
                else:
                    variables[p[1]] %= p[3]
    else:
        p[0] = (p[1], p[2])

        if validar_inicializacion_variables(p, 1):
            if isinstance(variables[p[1]], str):
                if esNumero(variables[p[1]][1:-1]):
                    variables[p[1]] = float(variables[p[1]][1:-1])
                else:
                    # Regla semántica: La variable a hacerle incremento o decremento debe ser un número
                    log_file.write(f"Error semántico: {p[1]} no es un número, por lo que no se puede hacer ++ o -- sobre ella\n")
                    return

            if p[2] == '++':
                variables[p[1]] += 1
            else:
                variables[p[1]] -= 1

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
                | ID CALL function_call
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
        p[0] = (p[1], p[2], p[3])

# Gramática para OPERACIONES * / % **
def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | term MOD factor
            | term POWER factor
            | factor'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[2], p[3])

def p_factor(p):
    '''factor : INTEGER
              | FLOAT
              | condition
              | STRING
              | LEFT_PAREN expression RIGHT_PAREN'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]

        if isinstance(p[1], str):
            # Regla semántica: Convertir un string a número cuando sea posible en una expresión aritmética
            if esNumero(p[1][1:-1]):
                p[0] = float(p[1][1:-1])
            # Regla semántica: Convertir un booleano a entero en una expresión aritmética
            elif p[1] == 'true':
                p[0] = 1
            elif p[1] == 'false':
                p[0] = 0
            # Regla semántica: No se pueden hacer operaciones aritméticas con strings que no sean números
            elif p[1].startswith('"') or p[1].startswith("'"):
                log_file.write(f"Error semántico: {p[1]} no es un número, por lo que no puede usarse en expresiones aritméticas\n")
                p[0] = 0
            # Regla semántica: Una variable debe contener un número o un string que sea un número para ser usada en una expresión aritmética
            # Nota: una expresión aritmética o condición se consideran números por el cálculo de su resultado
            elif validar_inicializacion_variables(p, 1):
                if not isinstance(variables[p[1]], str):
                    p[0] = variables[p[1]]
                elif esNumero(variables[p[1]][1:-1]):
                    p[0] = float(variables[p[1]][1:-1])
                else:
                    log_file.write(f"Error semántico: {p[1]} no es un número, por lo que no puede usarse en expresiones aritméticas\n")

# Gramática para IF, IF-ELSE, IF-ELSEIF, IF-ELSEIF-ELSE
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

# Gramática para bloques de código
def p_block(p):
    '''block : LEFT_BRACE statements RIGHT_BRACE
             | LEFT_BRACE RIGHT_BRACE'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = []

# Gramática para condiciones
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
    p[0] = (p[1], p[2], p[3])

def p_parenthesized_condition(p):
    'parenthesized_condition : LEFT_PAREN condition RIGHT_PAREN'
    p[0] = p[2]

def p_relational_expression(p):
    '''relational_expression : expression relational_operator expression'''
    p[0] = (p[1], p[2], p[3])

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

# Gramática para conversión de tipos
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
    variables[p[1]] = ('array_declaration', p[3])

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

# Verificar si el índice está dentro de los límites del array
def validar_indice(p, array_name, indice):
    if array_name in variables and isinstance(variables[array_name], tuple) and variables[array_name][0] == 'array_declaration':
        array = variables[array_name][1]
        if isinstance(indice, int) and 0 <= indice < len(array):
            return True
        else:
            log_file.write(f"Error semántico: Índice {indice} fuera de los límites del array {array_name}\n")
            return False
    else:
        log_file.write(f"Error semántico: {array_name} no es un array\n")
        return False


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

def esArray(p, indice):
    if validar_inicializacion_variables(p, indice):
        valor = variables[p[indice]]
        if isinstance(valor, tuple):
            return valor[0] == 'array_declaration'
    return False

#validar clave
def validar_clave(p, array_name, clave):
    if array_name in variables and isinstance(variables[array_name], tuple) and variables[array_name][0] == 'array_declaration':
        array = variables[array_name][1]
        if isinstance(array, dict):
            if clave in array:
                return True
            else:
                log_file.write(f"Error semántico: La clave '{clave}' no existe en el array asociativo {array_name}\n")
                return False
        else:
            log_file.write(f"Error semántico: {array_name} no es un array asociativo\n")
            return False
    else:
        log_file.write(f"Error semántico: {array_name} no es un array\n")
        return False

# Funciones de arrays
# Regla semántica: Solo se pueden indexar, añadir, modificar, 
# remover y contar elementos a variables que contengan un array.

def p_array_indexing(p):
    '''array_indexing : variable LEFT_BRACKET clave RIGHT_BRACKET'''
    p[0] = ('array_indexing', p[1], p[3])
    if not esArray(p, 1):
        log_file.write(f"Error semántico: {p[1]} no es un array, por lo que no se puede hacer indexing sobre ella\n")
    else:
        if isinstance(p[3], int):  # Si es índice numérico, validar límites
            if not validar_indice(p, p[1], p[3]):
                p[0] = None
        else:  # Si es clave asociativa, validar existencia de clave
            if not validar_clave(p, p[1], p[3]):
                p[0] = None

def p_array_add_element(p):
    '''array_add_element : variable LEFT_BRACKET RIGHT_BRACKET EQUALS argument'''
    p[0] = ('array_add_element', p[1], p[5])
    if not esArray(p, 1):
        log_file.write(f"Error semántico: {p[1]} no es un array, por lo que no se puede agregar elementos sobre ella\n")

def p_array_modify_element(p):
    '''array_modify_element : variable LEFT_BRACKET clave RIGHT_BRACKET EQUALS argument'''
    p[0] = ('array_modify_element', p[1], p[3], p[6])
    if not esArray(p, 1):
        log_file.write(f"Error semántico: {p[1]} no es un array, por lo que no se puede modificar elementos sobre ella\n")
    else:
        if isinstance(p[3], int):  # Si es índice numérico, validar límites
            if not validar_indice(p, p[1], p[3]):
                p[0] = None
        else:  # Si es clave asociativa, validar existencia de clave
            if not validar_clave(p, p[1], p[3]):
                p[0] = None

def p_array_remove_element(p):
    '''array_remove_element : UNSET LEFT_PAREN variable LEFT_BRACKET clave RIGHT_BRACKET RIGHT_PAREN'''
    p[0] = ('array_remove_element', p[3], p[5])
    if not esArray(p, 3):
        log_file.write(f"Error semántico: {p[3]} no es un array, por lo que no se puede eliminar elementos sobre ella\n")
    else:
        if isinstance(p[5], int):  # Si es índice numérico, validar límites
            if not validar_indice(p, p[3], p[5]):
                p[0] = None
        else:  # Si es clave asociativa, validar existencia de clave
            if not validar_clave(p, p[3], p[5]):
                p[0] = None

def p_array_count_elements(p):
    '''array_count_elements : COUNT LEFT_PAREN variable RIGHT_PAREN'''
    p[0] = ('array_count_elements', p[3])
    if not esArray(p, 3):
        log_file.write(f"Error semántico: {p[3]} no es un array, por lo que no se puede contar elementos sobre ella\n")

# Gramática para CLASES
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