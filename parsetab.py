
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT AND ARRAY AS ASYNC AWAIT BOOL BREAK CALL CALLABLE CASE CATCH CLASS CLONE CLOSE_TAG COLON COMMA CONST CONTINUE DECLARE DEFAULT DIE DIFFERENT DIVIDE DIVIDE_EQUALS DO DOT ECHO ELSE ELSEIF EMPTY ENDDECLARE ENDFOR ENDFOREACH ENDIF ENDSWITCH ENDWHILE ENUM EQUALS EQUAL_TO EVAL EXIT EXTENDS FALSE FGETS FINAL FINALLY FLOAT FN FOR FOREACH FSCANF FUNCTION GLOBAL GOTO GREATER_EQUAL GREATER_THAN HALT_COMPILER ID IDENTICAL_TO IF IMPLEMENTS INCLUDE INCLUDE_ONCE INSTANCEOF INSTEADOF INTEGER INTERFACE ISSET ITERABLE KEY_VALUE LEFT_BRACE LEFT_BRACKET LEFT_PAREN LESS_EQUAL LESS_THAN LIST LOGICAL_AND LOGICAL_NOT LOGICAL_OR LOGICAL_XOR LPAREN MATCH MINUS MINUS_EQUALS MINUS_MINUS MIXED MOD MOD_EQUALS MULTI_LINE_COMMENT NAME NAMESPACE NEW NOT_EQUAL_TO NOT_IDENTICAL_TO NULL OBJECT ONE_LINE_COMMENT OPEN_TAG OR PLUS PLUS_EQUALS PLUS_PLUS POWER PRINT PRIVATE PROTECTED PUBLIC REQUIRE REQUIRE_ONCE RETURN RIGHT_BRACE RIGHT_BRACKET RIGHT_PAREN RPAREN SELF SEMICOLON STATIC STDIN STRING SWITCH THROW TIMES TIMES_EQUALS TRAIT TRUE TRY UNSET USE VAR VOID WHILE XOR YIELD YIELD_FROMprogram : OPEN_TAG statements CLOSE_TAGstatements : statement2\n                  | statements statement2statement2 : statement SEMICOLON\n                  | if_statement\n                  | while_statement\n                  | for_statement\n                  | ONE_LINE_COMMENT\n                  | MULTI_LINE_COMMENTstatement : print_statement\n                 | fscanf_statement\n                 | fgets_statement\n                 | assignment_statement\n                 | array_declaration_statement\n                 | BREAK\n                 | CONTINUEfgets_statement : FGETS LEFT_PAREN STDIN RIGHT_PARENfscanf_statement : FSCANF LEFT_PAREN STDIN COMMA STRING COMMA variable_list RIGHT_PARENvariable_list : variable\n                     | variable_list COMMA variablevariable : IDassignment_operator : EQUALS\n                           | PLUS_EQUALS\n                           | MINUS_EQUALS\n                           | TIMES_EQUALS\n                           | DIVIDE_EQUALS\n                           | MOD_EQUALSassignment_statement : variable assignment_operator argument\n                             | variable PLUS_PLUS\n                             | variable MINUS_MINUSprint_statement : print_function LEFT_PAREN arguments RIGHT_PAREN\n                       | print_function argumentsprint_function : PRINT\n                      | ECHOarguments : argument\n                 | arguments DOT argumentargument : INTEGER\n                | FLOAT\n                | STRING\n                | variable                \n                | expression\n                | condition\n                | assignment_statementexpression : expression PLUS term\n                  | expression MINUS term\n                  | termterm : term TIMES factor\n            | term DIVIDE factor\n            | factorfactor : INTEGER\n              | FLOAT\n              | variable\n              | LEFT_PAREN expression RIGHT_PARENif_statement : IF LEFT_PAREN condition RIGHT_PAREN block\n                    | IF LEFT_PAREN condition RIGHT_PAREN block ELSE blockwhile_statement : WHILE LEFT_PAREN condition RIGHT_PAREN blockfor_part1 : FOR LEFT_PAREN assignment_list SEMICOLON\n                 | FOR LEFT_PAREN SEMICOLONfor_statement : for_part1 condition for_part3\n                     | for_part1 for_part3for_part3 : SEMICOLON statement_list RIGHT_PAREN for_part4\n                 | SEMICOLON RIGHT_PAREN for_part4for_part4 : block\n                 | SEMICOLONassignment_list : assignment_statement\n                       | assignment_list COMMA assignment_statementstatement_list : statement\n                      | statement_list COMMA statementblock : LEFT_BRACE statements RIGHT_BRACE\n             | LEFT_BRACE RIGHT_BRACEcondition : TRUE\n                 | FALSE\n                 | expression relational_operator expression\n                 | condition logical_operator condition\n                 | LOGICAL_NOT condition\n                 | LEFT_PAREN condition RIGHT_PARENrelational_operator : EQUAL_TO\n                           | NOT_EQUAL_TO\n                           | LESS_THAN\n                           | GREATER_THAN\n                           | LESS_EQUAL\n                           | GREATER_EQUAL\n                           | IDENTICAL_TO\n                           | NOT_IDENTICAL_TO\n                           | DIFFERENTlogical_operator : LOGICAL_AND\n                        | LOGICAL_OR\n                        | LOGICAL_XORarray_declaration_statement : variable EQUALS arrayarray : ARRAY LEFT_PAREN array_elements RIGHT_PAREN\n             | LEFT_BRACKET array_elements RIGHT_BRACKETarray_elements : argument\n                      | array_elements COMMA argument'
    
_lr_action_items = {'OPEN_TAG':([0,],[2,]),'$end':([1,29,],[0,-1,]),'ONE_LINE_COMMENT':([2,3,4,6,7,8,9,10,30,31,35,71,122,123,124,125,137,138,140,142,143,150,154,],[9,9,-2,-5,-6,-7,-8,-9,-3,-4,-60,-59,-64,-62,-63,9,-54,-56,-61,9,-70,-69,-55,]),'MULTI_LINE_COMMENT':([2,3,4,6,7,8,9,10,30,31,35,71,122,123,124,125,137,138,140,142,143,150,154,],[10,10,-2,-5,-6,-7,-8,-9,-3,-4,-60,-59,-64,-62,-63,10,-54,-56,-61,10,-70,-69,-55,]),'BREAK':([2,3,4,6,7,8,9,10,30,31,35,41,71,121,122,123,124,125,137,138,140,142,143,150,154,],[16,16,-2,-5,-6,-7,-8,-9,-3,-4,-60,16,-59,16,-64,-62,-63,16,-54,-56,-61,16,-70,-69,-55,]),'CONTINUE':([2,3,4,6,7,8,9,10,30,31,35,41,71,121,122,123,124,125,137,138,140,142,143,150,154,],[17,17,-2,-5,-6,-7,-8,-9,-3,-4,-60,17,-59,17,-64,-62,-63,17,-54,-56,-61,17,-70,-69,-55,]),'IF':([2,3,4,6,7,8,9,10,30,31,35,71,122,123,124,125,137,138,140,142,143,150,154,],[18,18,-2,-5,-6,-7,-8,-9,-3,-4,-60,-59,-64,-62,-63,18,-54,-56,-61,18,-70,-69,-55,]),'WHILE':([2,3,4,6,7,8,9,10,30,31,35,71,122,123,124,125,137,138,140,142,143,150,154,],[19,19,-2,-5,-6,-7,-8,-9,-3,-4,-60,-59,-64,-62,-63,19,-54,-56,-61,19,-70,-69,-55,]),'FSCANF':([2,3,4,6,7,8,9,10,30,31,35,41,71,121,122,123,124,125,137,138,140,142,143,150,154,],[22,22,-2,-5,-6,-7,-8,-9,-3,-4,-60,22,-59,22,-64,-62,-63,22,-54,-56,-61,22,-70,-69,-55,]),'FGETS':([2,3,4,6,7,8,9,10,30,31,35,41,71,121,122,123,124,125,137,138,140,142,143,150,154,],[23,23,-2,-5,-6,-7,-8,-9,-3,-4,-60,23,-59,23,-64,-62,-63,23,-54,-56,-61,23,-70,-69,-55,]),'FOR':([2,3,4,6,7,8,9,10,30,31,35,71,122,123,124,125,137,138,140,142,143,150,154,],[25,25,-2,-5,-6,-7,-8,-9,-3,-4,-60,-59,-64,-62,-63,25,-54,-56,-61,25,-70,-69,-55,]),'PRINT':([2,3,4,6,7,8,9,10,30,31,35,41,71,121,122,123,124,125,137,138,140,142,143,150,154,],[26,26,-2,-5,-6,-7,-8,-9,-3,-4,-60,26,-59,26,-64,-62,-63,26,-54,-56,-61,26,-70,-69,-55,]),'ECHO':([2,3,4,6,7,8,9,10,30,31,35,41,71,121,122,123,124,125,137,138,140,142,143,150,154,],[27,27,-2,-5,-6,-7,-8,-9,-3,-4,-60,27,-59,27,-64,-62,-63,27,-54,-56,-61,27,-70,-69,-55,]),'ID':([2,3,4,6,7,8,9,10,20,21,26,27,30,31,32,33,35,39,40,41,47,59,62,63,64,65,66,67,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,94,95,99,100,106,108,115,121,122,123,124,125,132,135,136,137,138,140,142,143,147,150,151,154,157,],[28,28,-2,-5,-6,-7,-8,-9,28,28,-33,-34,-3,-4,28,28,-60,28,28,28,28,28,-22,-23,-24,-25,-26,-27,28,-59,28,-86,-87,-88,28,28,28,-77,-78,-79,-80,-81,-82,-83,-84,-85,28,28,28,-22,28,-58,28,28,-64,-62,-63,28,28,-57,28,-54,-56,-61,28,-70,28,-69,28,-55,28,]),'CLOSE_TAG':([3,4,6,7,8,9,10,30,31,35,71,122,123,124,137,138,140,143,150,154,],[29,-2,-5,-6,-7,-8,-9,-3,-4,-60,-59,-64,-62,-63,-54,-56,-61,-70,-69,-55,]),'RIGHT_BRACE':([4,6,7,8,9,10,30,31,35,71,122,123,124,125,137,138,140,142,143,150,154,],[-2,-5,-6,-7,-8,-9,-3,-4,-60,-59,-64,-62,-63,143,-54,-56,-61,150,-70,-69,-55,]),'SEMICOLON':([5,11,12,13,14,15,16,17,20,28,34,36,37,42,43,44,45,46,48,49,50,51,52,53,54,55,56,60,61,68,88,92,103,104,107,108,109,113,114,116,117,118,119,120,126,127,128,129,131,135,146,148,152,158,],[31,-10,-11,-12,-13,-14,-15,-16,41,-21,41,-71,-72,-46,-49,-50,-51,-52,-32,-35,-37,-38,-39,-40,-41,-42,-43,-29,-30,108,-75,122,-28,-89,135,-58,-65,-74,-73,-44,-45,-76,-53,122,-47,-48,-31,-36,-17,-57,-91,-66,-90,-18,]),'RIGHT_PAREN':([11,12,13,14,15,16,17,28,36,37,41,42,43,44,45,46,48,49,50,51,52,53,54,55,56,60,61,69,70,88,89,90,91,93,96,97,98,102,103,104,113,114,116,117,118,119,126,127,128,129,131,134,139,141,145,146,152,153,155,156,158,159,],[-10,-11,-12,-13,-14,-15,-16,-21,-71,-72,92,-46,-49,-50,-51,-52,-32,-35,-37,-38,-39,-40,-41,-42,-43,-29,-30,111,112,-75,118,119,120,-67,128,118,119,131,-28,-89,-74,-73,-44,-45,-76,-53,-47,-48,-31,-36,-17,-92,119,-68,152,-91,-90,-93,158,-19,-18,-20,]),'COMMA':([11,12,13,14,15,16,17,28,36,37,42,43,44,45,46,48,49,50,51,52,53,54,55,56,60,61,88,91,93,101,103,104,107,109,113,114,116,117,118,119,126,127,128,129,131,133,134,141,144,145,146,148,152,153,155,156,158,159,],[-10,-11,-12,-13,-14,-15,-16,-21,-71,-72,-46,-49,-50,-51,-52,-32,-35,-37,-38,-39,-40,-41,-42,-43,-29,-30,-75,121,-67,130,-28,-89,136,-65,-74,-73,-44,-45,-76,-53,-47,-48,-31,-36,-17,147,-92,-68,151,147,-91,-66,-90,-93,157,-19,-18,-20,]),'LEFT_PAREN':([18,19,20,21,22,23,25,26,27,32,33,39,40,47,59,62,63,64,65,66,67,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,94,95,99,100,105,106,108,115,132,135,147,],[32,33,40,47,57,58,68,-33,-34,40,40,40,40,40,40,-22,-23,-24,-25,-26,-27,40,-86,-87,-88,115,115,115,-77,-78,-79,-80,-81,-82,-83,-84,-85,115,115,40,-22,132,40,-58,115,40,-57,40,]),'TRUE':([20,21,26,27,32,33,39,40,47,59,62,63,64,65,66,67,72,73,74,75,99,100,106,108,132,135,147,],[36,36,-33,-34,36,36,36,36,36,36,-22,-23,-24,-25,-26,-27,36,-86,-87,-88,36,-22,36,-58,36,-57,36,]),'FALSE':([20,21,26,27,32,33,39,40,47,59,62,63,64,65,66,67,72,73,74,75,99,100,106,108,132,135,147,],[37,37,-33,-34,37,37,37,37,37,37,-22,-23,-24,-25,-26,-27,37,-86,-87,-88,37,-22,37,-58,37,-57,37,]),'LOGICAL_NOT':([20,21,26,27,32,33,39,40,47,59,62,63,64,65,66,67,72,73,74,75,99,100,106,108,132,135,147,],[39,39,-33,-34,39,39,39,39,39,39,-22,-23,-24,-25,-26,-27,39,-86,-87,-88,39,-22,39,-58,39,-57,39,]),'INTEGER':([20,21,26,27,32,33,39,40,47,59,62,63,64,65,66,67,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,94,95,99,100,106,108,115,132,135,147,],[44,50,-33,-34,44,44,44,44,50,50,-22,-23,-24,-25,-26,-27,44,-86,-87,-88,44,44,44,-77,-78,-79,-80,-81,-82,-83,-84,-85,44,44,50,-22,50,-58,44,50,-57,50,]),'FLOAT':([20,21,26,27,32,33,39,40,47,59,62,63,64,65,66,67,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,94,95,99,100,106,108,115,132,135,147,],[45,51,-33,-34,45,45,45,45,51,51,-22,-23,-24,-25,-26,-27,45,-86,-87,-88,45,45,45,-77,-78,-79,-80,-81,-82,-83,-84,-85,45,45,51,-22,51,-58,45,51,-57,51,]),'STRING':([21,26,27,47,59,62,63,64,65,66,67,99,100,106,130,132,147,],[52,-33,-34,52,52,-22,-23,-24,-25,-26,-27,52,-22,52,144,52,52,]),'PLUS_PLUS':([24,28,53,110,],[60,-21,60,60,]),'MINUS_MINUS':([24,28,53,110,],[61,-21,61,61,]),'EQUALS':([24,28,53,110,],[62,-21,100,100,]),'PLUS_EQUALS':([24,28,53,110,],[63,-21,63,63,]),'MINUS_EQUALS':([24,28,53,110,],[64,-21,64,64,]),'TIMES_EQUALS':([24,28,53,110,],[65,-21,65,65,]),'DIVIDE_EQUALS':([24,28,53,110,],[66,-21,66,66,]),'MOD_EQUALS':([24,28,53,110,],[67,-21,67,67,]),'TIMES':([28,42,43,44,45,46,50,51,53,116,117,119,126,127,],[-21,94,-49,-50,-51,-52,-50,-51,-52,94,94,-53,-47,-48,]),'DIVIDE':([28,42,43,44,45,46,50,51,53,116,117,119,126,127,],[-21,95,-49,-50,-51,-52,-50,-51,-52,95,95,-53,-47,-48,]),'PLUS':([28,38,42,43,44,45,46,50,51,53,54,90,98,114,116,117,119,126,127,139,],[-21,77,-46,-49,-50,-51,-52,-50,-51,-52,77,77,77,77,-44,-45,-53,-47,-48,77,]),'MINUS':([28,38,42,43,44,45,46,50,51,53,54,90,98,114,116,117,119,126,127,139,],[-21,78,-46,-49,-50,-51,-52,-50,-51,-52,78,78,78,78,-44,-45,-53,-47,-48,78,]),'EQUAL_TO':([28,38,42,43,44,45,46,50,51,53,54,90,98,116,117,119,126,127,],[-21,79,-46,-49,-50,-51,-52,-50,-51,-52,79,79,79,-44,-45,-53,-47,-48,]),'NOT_EQUAL_TO':([28,38,42,43,44,45,46,50,51,53,54,90,98,116,117,119,126,127,],[-21,80,-46,-49,-50,-51,-52,-50,-51,-52,80,80,80,-44,-45,-53,-47,-48,]),'LESS_THAN':([28,38,42,43,44,45,46,50,51,53,54,90,98,116,117,119,126,127,],[-21,81,-46,-49,-50,-51,-52,-50,-51,-52,81,81,81,-44,-45,-53,-47,-48,]),'GREATER_THAN':([28,38,42,43,44,45,46,50,51,53,54,90,98,116,117,119,126,127,],[-21,82,-46,-49,-50,-51,-52,-50,-51,-52,82,82,82,-44,-45,-53,-47,-48,]),'LESS_EQUAL':([28,38,42,43,44,45,46,50,51,53,54,90,98,116,117,119,126,127,],[-21,83,-46,-49,-50,-51,-52,-50,-51,-52,83,83,83,-44,-45,-53,-47,-48,]),'GREATER_EQUAL':([28,38,42,43,44,45,46,50,51,53,54,90,98,116,117,119,126,127,],[-21,84,-46,-49,-50,-51,-52,-50,-51,-52,84,84,84,-44,-45,-53,-47,-48,]),'IDENTICAL_TO':([28,38,42,43,44,45,46,50,51,53,54,90,98,116,117,119,126,127,],[-21,85,-46,-49,-50,-51,-52,-50,-51,-52,85,85,85,-44,-45,-53,-47,-48,]),'NOT_IDENTICAL_TO':([28,38,42,43,44,45,46,50,51,53,54,90,98,116,117,119,126,127,],[-21,86,-46,-49,-50,-51,-52,-50,-51,-52,86,86,86,-44,-45,-53,-47,-48,]),'DIFFERENT':([28,38,42,43,44,45,46,50,51,53,54,90,98,116,117,119,126,127,],[-21,87,-46,-49,-50,-51,-52,-50,-51,-52,87,87,87,-44,-45,-53,-47,-48,]),'DOT':([28,36,37,42,43,44,45,46,48,49,50,51,52,53,54,55,56,60,61,88,96,97,98,103,113,114,116,117,118,119,126,127,129,],[-21,-71,-72,-46,-49,-50,-51,-52,99,-35,-37,-38,-39,-40,-41,-42,-43,-29,-30,-75,99,-42,-41,-28,-74,-73,-44,-45,-76,-53,-47,-48,-36,]),'RIGHT_BRACKET':([28,36,37,42,43,44,45,46,50,51,52,53,54,55,56,60,61,88,103,113,114,116,117,118,119,126,127,133,134,153,],[-21,-71,-72,-46,-49,-50,-51,-52,-37,-38,-39,-40,-41,-42,-43,-29,-30,-75,-28,-74,-73,-44,-45,-76,-53,-47,-48,146,-92,-93,]),'LOGICAL_AND':([28,34,36,37,42,43,44,45,46,55,69,70,88,89,97,113,114,116,117,118,119,126,127,],[-21,73,-71,-72,-46,-49,-50,-51,-52,73,73,73,73,73,73,73,-73,-44,-45,-76,-53,-47,-48,]),'LOGICAL_OR':([28,34,36,37,42,43,44,45,46,55,69,70,88,89,97,113,114,116,117,118,119,126,127,],[-21,74,-71,-72,-46,-49,-50,-51,-52,74,74,74,74,74,74,74,-73,-44,-45,-76,-53,-47,-48,]),'LOGICAL_XOR':([28,34,36,37,42,43,44,45,46,55,69,70,88,89,97,113,114,116,117,118,119,126,127,],[-21,75,-71,-72,-46,-49,-50,-51,-52,75,75,75,75,75,75,75,-73,-44,-45,-76,-53,-47,-48,]),'STDIN':([57,58,],[101,102,]),'ARRAY':([62,],[105,]),'LEFT_BRACKET':([62,],[106,]),'LEFT_BRACE':([92,111,112,120,149,],[125,125,125,125,125,]),'ELSE':([137,143,150,],[149,-70,-69,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([2,125,],[3,142,]),'statement2':([2,3,125,142,],[4,30,4,30,]),'statement':([2,3,41,121,125,142,],[5,5,93,141,5,5,]),'if_statement':([2,3,125,142,],[6,6,6,6,]),'while_statement':([2,3,125,142,],[7,7,7,7,]),'for_statement':([2,3,125,142,],[8,8,8,8,]),'print_statement':([2,3,41,121,125,142,],[11,11,11,11,11,11,]),'fscanf_statement':([2,3,41,121,125,142,],[12,12,12,12,12,12,]),'fgets_statement':([2,3,41,121,125,142,],[13,13,13,13,13,13,]),'assignment_statement':([2,3,21,41,47,59,68,99,106,121,125,132,136,142,147,],[14,14,56,14,56,56,109,56,56,14,14,56,148,14,56,]),'array_declaration_statement':([2,3,41,121,125,142,],[15,15,15,15,15,15,]),'for_part1':([2,3,125,142,],[20,20,20,20,]),'print_function':([2,3,41,121,125,142,],[21,21,21,21,21,21,]),'variable':([2,3,20,21,32,33,39,40,41,47,59,68,72,76,77,78,94,95,99,106,115,121,125,132,136,142,147,151,157,],[24,24,46,53,46,46,46,46,24,53,53,110,46,46,46,46,46,46,53,53,46,24,24,53,110,24,53,156,159,]),'condition':([20,21,32,33,39,40,47,59,72,99,106,132,147,],[34,55,69,70,88,89,97,55,113,55,55,55,55,]),'for_part3':([20,34,],[35,71,]),'expression':([20,21,32,33,39,40,47,59,72,76,99,106,115,132,147,],[38,54,38,38,38,90,98,54,38,114,54,54,139,54,54,]),'term':([20,21,32,33,39,40,47,59,72,76,77,78,99,106,115,132,147,],[42,42,42,42,42,42,42,42,42,42,116,117,42,42,42,42,42,]),'factor':([20,21,32,33,39,40,47,59,72,76,77,78,94,95,99,106,115,132,147,],[43,43,43,43,43,43,43,43,43,43,43,43,126,127,43,43,43,43,43,]),'arguments':([21,47,],[48,96,]),'argument':([21,47,59,99,106,132,147,],[49,49,103,129,134,134,153,]),'assignment_operator':([24,53,110,],[59,59,59,]),'logical_operator':([34,55,69,70,88,89,97,113,],[72,72,72,72,72,72,72,72,]),'relational_operator':([38,54,90,98,],[76,76,76,76,]),'statement_list':([41,],[91,]),'array':([62,],[104,]),'assignment_list':([68,],[107,]),'for_part4':([92,120,],[123,140,]),'block':([92,111,112,120,149,],[124,137,138,124,154,]),'array_elements':([106,132,],[133,145,]),'variable_list':([151,],[155,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> OPEN_TAG statements CLOSE_TAG','program',3,'p_program','parser.py',8),
  ('statements -> statement2','statements',1,'p_statements','parser.py',12),
  ('statements -> statements statement2','statements',2,'p_statements','parser.py',13),
  ('statement2 -> statement SEMICOLON','statement2',2,'p_statement2','parser.py',21),
  ('statement2 -> if_statement','statement2',1,'p_statement2','parser.py',22),
  ('statement2 -> while_statement','statement2',1,'p_statement2','parser.py',23),
  ('statement2 -> for_statement','statement2',1,'p_statement2','parser.py',24),
  ('statement2 -> ONE_LINE_COMMENT','statement2',1,'p_statement2','parser.py',25),
  ('statement2 -> MULTI_LINE_COMMENT','statement2',1,'p_statement2','parser.py',26),
  ('statement -> print_statement','statement',1,'p_statement','parser.py',31),
  ('statement -> fscanf_statement','statement',1,'p_statement','parser.py',32),
  ('statement -> fgets_statement','statement',1,'p_statement','parser.py',33),
  ('statement -> assignment_statement','statement',1,'p_statement','parser.py',34),
  ('statement -> array_declaration_statement','statement',1,'p_statement','parser.py',35),
  ('statement -> BREAK','statement',1,'p_statement','parser.py',36),
  ('statement -> CONTINUE','statement',1,'p_statement','parser.py',37),
  ('fgets_statement -> FGETS LEFT_PAREN STDIN RIGHT_PAREN','fgets_statement',4,'p_fgets_statement','parser.py',43),
  ('fscanf_statement -> FSCANF LEFT_PAREN STDIN COMMA STRING COMMA variable_list RIGHT_PAREN','fscanf_statement',8,'p_fscanf_statement','parser.py',48),
  ('variable_list -> variable','variable_list',1,'p_variable_list','parser.py',52),
  ('variable_list -> variable_list COMMA variable','variable_list',3,'p_variable_list','parser.py',53),
  ('variable -> ID','variable',1,'p_variable','parser.py',61),
  ('assignment_operator -> EQUALS','assignment_operator',1,'p_assignment_operator','parser.py',65),
  ('assignment_operator -> PLUS_EQUALS','assignment_operator',1,'p_assignment_operator','parser.py',66),
  ('assignment_operator -> MINUS_EQUALS','assignment_operator',1,'p_assignment_operator','parser.py',67),
  ('assignment_operator -> TIMES_EQUALS','assignment_operator',1,'p_assignment_operator','parser.py',68),
  ('assignment_operator -> DIVIDE_EQUALS','assignment_operator',1,'p_assignment_operator','parser.py',69),
  ('assignment_operator -> MOD_EQUALS','assignment_operator',1,'p_assignment_operator','parser.py',70),
  ('assignment_statement -> variable assignment_operator argument','assignment_statement',3,'p_assignment_statement','parser.py',75),
  ('assignment_statement -> variable PLUS_PLUS','assignment_statement',2,'p_assignment_statement','parser.py',76),
  ('assignment_statement -> variable MINUS_MINUS','assignment_statement',2,'p_assignment_statement','parser.py',77),
  ('print_statement -> print_function LEFT_PAREN arguments RIGHT_PAREN','print_statement',4,'p_print_statement','parser.py',85),
  ('print_statement -> print_function arguments','print_statement',2,'p_print_statement','parser.py',86),
  ('print_function -> PRINT','print_function',1,'p_print_function','parser.py',93),
  ('print_function -> ECHO','print_function',1,'p_print_function','parser.py',94),
  ('arguments -> argument','arguments',1,'p_arguments','parser.py',98),
  ('arguments -> arguments DOT argument','arguments',3,'p_arguments','parser.py',99),
  ('argument -> INTEGER','argument',1,'p_argument','parser.py',107),
  ('argument -> FLOAT','argument',1,'p_argument','parser.py',108),
  ('argument -> STRING','argument',1,'p_argument','parser.py',109),
  ('argument -> variable','argument',1,'p_argument','parser.py',110),
  ('argument -> expression','argument',1,'p_argument','parser.py',111),
  ('argument -> condition','argument',1,'p_argument','parser.py',112),
  ('argument -> assignment_statement','argument',1,'p_argument','parser.py',113),
  ('expression -> expression PLUS term','expression',3,'p_expression_arithmetic','parser.py',118),
  ('expression -> expression MINUS term','expression',3,'p_expression_arithmetic','parser.py',119),
  ('expression -> term','expression',1,'p_expression_arithmetic','parser.py',120),
  ('term -> term TIMES factor','term',3,'p_term','parser.py',127),
  ('term -> term DIVIDE factor','term',3,'p_term','parser.py',128),
  ('term -> factor','term',1,'p_term','parser.py',129),
  ('factor -> INTEGER','factor',1,'p_factor','parser.py',136),
  ('factor -> FLOAT','factor',1,'p_factor','parser.py',137),
  ('factor -> variable','factor',1,'p_factor','parser.py',138),
  ('factor -> LEFT_PAREN expression RIGHT_PAREN','factor',3,'p_factor','parser.py',139),
  ('if_statement -> IF LEFT_PAREN condition RIGHT_PAREN block','if_statement',5,'p_if_statement','parser.py',151),
  ('if_statement -> IF LEFT_PAREN condition RIGHT_PAREN block ELSE block','if_statement',7,'p_if_statement','parser.py',152),
  ('while_statement -> WHILE LEFT_PAREN condition RIGHT_PAREN block','while_statement',5,'p_while_statement','parser.py',160),
  ('for_part1 -> FOR LEFT_PAREN assignment_list SEMICOLON','for_part1',4,'p_for_part1','parser.py',165),
  ('for_part1 -> FOR LEFT_PAREN SEMICOLON','for_part1',3,'p_for_part1','parser.py',166),
  ('for_statement -> for_part1 condition for_part3','for_statement',3,'p_for_part2','parser.py',173),
  ('for_statement -> for_part1 for_part3','for_statement',2,'p_for_part2','parser.py',174),
  ('for_part3 -> SEMICOLON statement_list RIGHT_PAREN for_part4','for_part3',4,'p_for_part3','parser.py',181),
  ('for_part3 -> SEMICOLON RIGHT_PAREN for_part4','for_part3',3,'p_for_part3','parser.py',182),
  ('for_part4 -> block','for_part4',1,'p_for_part4','parser.py',189),
  ('for_part4 -> SEMICOLON','for_part4',1,'p_for_part4','parser.py',190),
  ('assignment_list -> assignment_statement','assignment_list',1,'p_assignment_list','parser.py',194),
  ('assignment_list -> assignment_list COMMA assignment_statement','assignment_list',3,'p_assignment_list','parser.py',195),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parser.py',203),
  ('statement_list -> statement_list COMMA statement','statement_list',3,'p_statement_list','parser.py',204),
  ('block -> LEFT_BRACE statements RIGHT_BRACE','block',3,'p_block','parser.py',212),
  ('block -> LEFT_BRACE RIGHT_BRACE','block',2,'p_block','parser.py',213),
  ('condition -> TRUE','condition',1,'p_condition','parser.py',220),
  ('condition -> FALSE','condition',1,'p_condition','parser.py',221),
  ('condition -> expression relational_operator expression','condition',3,'p_condition','parser.py',222),
  ('condition -> condition logical_operator condition','condition',3,'p_condition','parser.py',223),
  ('condition -> LOGICAL_NOT condition','condition',2,'p_condition','parser.py',224),
  ('condition -> LEFT_PAREN condition RIGHT_PAREN','condition',3,'p_condition','parser.py',225),
  ('relational_operator -> EQUAL_TO','relational_operator',1,'p_relational_operator','parser.py',234),
  ('relational_operator -> NOT_EQUAL_TO','relational_operator',1,'p_relational_operator','parser.py',235),
  ('relational_operator -> LESS_THAN','relational_operator',1,'p_relational_operator','parser.py',236),
  ('relational_operator -> GREATER_THAN','relational_operator',1,'p_relational_operator','parser.py',237),
  ('relational_operator -> LESS_EQUAL','relational_operator',1,'p_relational_operator','parser.py',238),
  ('relational_operator -> GREATER_EQUAL','relational_operator',1,'p_relational_operator','parser.py',239),
  ('relational_operator -> IDENTICAL_TO','relational_operator',1,'p_relational_operator','parser.py',240),
  ('relational_operator -> NOT_IDENTICAL_TO','relational_operator',1,'p_relational_operator','parser.py',241),
  ('relational_operator -> DIFFERENT','relational_operator',1,'p_relational_operator','parser.py',242),
  ('logical_operator -> LOGICAL_AND','logical_operator',1,'p_logical_operator','parser.py',246),
  ('logical_operator -> LOGICAL_OR','logical_operator',1,'p_logical_operator','parser.py',247),
  ('logical_operator -> LOGICAL_XOR','logical_operator',1,'p_logical_operator','parser.py',248),
  ('array_declaration_statement -> variable EQUALS array','array_declaration_statement',3,'p_array_declaration_statement','parser.py',262),
  ('array -> ARRAY LEFT_PAREN array_elements RIGHT_PAREN','array',4,'p_array','parser.py',266),
  ('array -> LEFT_BRACKET array_elements RIGHT_BRACKET','array',3,'p_array','parser.py',267),
  ('array_elements -> argument','array_elements',1,'p_array_elements','parser.py',271),
  ('array_elements -> array_elements COMMA argument','array_elements',3,'p_array_elements','parser.py',272),
]
