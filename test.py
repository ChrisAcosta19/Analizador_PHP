# Ejemplo de prueba
data = '''
<?php
$var1 + 1;
$var2 = "Hola";
$var2 += 2;
$var2 += "mundo";
$var2++;
"cadena" + 3;
$var2[1];
$var2[] = 6;
$var2[1] = 7;
unset($var2[1]);
count($var2);
echo saludar();
function saludar() {
    return "Hola";
}
function saludar() {
    return "Hola mundo";
}
echo saludar(5);
?>
'''