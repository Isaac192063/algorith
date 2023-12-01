<?php

$rango = 5;
$soluciones = [];

for ($i = 0; $i < 10; $i++) {
    $numeros = [];
    for ($j = 0; $j < $rango; $j++) {

        do {
            $num_aleatorio = rand(0, 4);
        } while (in_array($num_aleatorio, $numeros));

        $numeros[$j] = $num_aleatorio;
    }
    for ($j = 0; $j < $rango; $j++) {
        echo $numeros[$j];
    }
    echo '<br>';
    $soluciones[$i] = $numeros;
}
// ver informacion del array
print_r($soluciones);
echo '<br>';

var_dump($soluciones);


$sol = [
    [0,3,4,7,8],
    [2,0,5,6,7],
    [4,6,0,4,6],
    [5,7,3,0,5],
    [6,7,5,6,0],
];

$propuesta = [1,0,4,2,3,1];
$suma = 0;

for($i = 0; $i<count($propuesta)-1; $i++){
    echo '<h4>'.$sol[$propuesta[$i]][$propuesta[$i+1]].' <h4>';
    $suma += $sol[$propuesta[$i]][$propuesta[$i+1]];
}

echo '<h3>el resultado es '.$suma.'<h3>';