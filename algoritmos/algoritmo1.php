<?php
// Declaración de variables
$variable1 = 10;
$variable2 = "Hola, mundo!";
$variable3 = true;
// Estructura condicional
if ($variable1 > 5) {
 echo "El número es mayor que 5";
} else {
 echo "El número es menor o igual que 5";
}
// Bucle
for ($i = 0; $i < 5; $i++) {
 echo "Iteración número: $i<br>";
}
// Operadores aritméticos
$resultado = $variable1 + 3;
echo "El resultado de la suma es: $resultado";
// Operadores lógicos
if ($variable3 && $variable1 == 10) {
 echo "La variable3 es verdadera y la variable1 es igual a 10";
}
// Asignación
$variable1 += 5;
echo "El valor de variable1 después de la suma es: $variable1";
// Arrays
$miArray = array("manzana", "banana", "naranja");
echo "El segundo elemento del array es: " . $miArray[1];
// Funciones
function miFuncion($parametro1, $parametro2) {
    return $parametro1 * $parametro2;
}
echo "El resultado de la función es: " . miFuncion(2, 3);
// While
while ($i < 10) {
    echo $i;
    $i++;
}
// Arrays
$lista = array(1, "hola", 3.14, true);
$lista[1];
$lista[1] = "mundo";
$lista[] = 42;
unset($lista[2]);
count($lista);
?>