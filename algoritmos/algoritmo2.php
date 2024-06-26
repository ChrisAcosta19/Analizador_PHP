<?php
// Declaración de variables
$name = "Juan";
$age = 20;
$isStudent = true;
// Función simple
function greet($name) {
 return "Hola, " . $name . "!";
}
// Llamada a la función
echo greet($name) . "\n";
// Condicional
if ($age >= 18) {
 echo $name . " es mayor de edad.\n";
} else {
 echo $name . " es menor de edad.\n";
}
// Bucle for
for ($i = 0; $i < 5; $i++) {
 echo "Número: " . $i . "\n";
}
// Declaración de Array
$fruits = array("manzana", "naranja", "plátano");
// Clase y objeto
class Person {
 public $name;
 public $age;
 // Constructor
 public function __construct($name, $age) {
 $this->name = $name;
 $this->age = $age;
 }
 // Método
 public function introduce() {
 return "Me llamo " . $this->name . " y tengo " . $this->age . " años.";
 }
}
// Creación de un objeto
$person = new Person("Ana", 25);
echo $person->introduce() . "\n";
// Declaración de array asociativo
$grades = array(
 "math" => 90,
 "science" => 85,
 "literature" => 88
);
// Función con parámetros numéricos
function calculateArea($length, $width) {
 return $length * $width;
}
echo "Área: " . calculateArea(5, 4) . "\n";
?>