# Ejemplo de prueba
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