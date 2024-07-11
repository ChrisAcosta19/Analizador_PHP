info = '''
Reglas sintácticas implementadas:
1. Inicio y fin de un bloque de código PHP.
2. Declaración de variables.
3. Asignación de valores a variables.
4. Incremento y decremento de variables.
5. Condicionales if, else if, else.
6. Bucles while y for.
7. Operaciones aritméticas y relacionales.
8. Condiciones simples, negadas, complejas y entre paréntesis.
9. Declaración de funciones básicas, con valores por defecto y anónimas.
10. Retorno de valores en funciones.
11. Llamada a funciones.
12. Solicitud de entrada por teclado con fscanf y fgets.
13. Impresión de valores por pantalla con echo y print.
14. Declaración de arrays indexados y asociativos.
15. Adición, indexación, modificación, eliminación y conteo de elementos en arrays.
16. Conversión de tipos de datos (casting).
17. Declaración de clases con atributos y métodos.
18. Creación de objetos y llamada a métodos y atributos de una clase.

Reglas semánticas implementadas:
1. Una variable debe ser inicializada antes de ser usada.
2. Solo se puede usar +=, -=, *=, /=, %= con números.
3. La variable a hacerle +=, -=, *=, /=, %= debe ser un número.
4. La variable a hacerle incremento o decremento debe ser un número.
5. Convertir un string a número cuando sea posible en una expresión aritmética.
6. Convertir un booleano a entero en una expresión aritmética.
7. No se pueden hacer operaciones aritméticas con strings que no sean números.
8. Una variable debe contener un número o un string que sea un número para ser usada en una expresión
   aritmética. Una expresión aritmética o condición se consideran números por el cálculo de su resultado.
9. Solo se pueden indexar, añadir, modificar, remover y contar elementos a variables que contengan un array.
10. Una función debe ser declarada antes de ser llamada.
11. Una función solo puede ser declarada una vez.
12. En una llamada a una función, se debe pasar un número de argumentos igual al número de parámetros
    definidos en su declaración.
13. En arreglos indexados, para indexar, modificar o remover un elemento se debe usar un índice que se
    encuentre dentro de los límites del tamaño del arreglo.
14. En arreglos asociativos, para indexar, modificar o remover un elemento se debe usar una clave que
    exista entre los elementos del arreglo.
'''