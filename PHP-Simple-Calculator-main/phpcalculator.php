<?php

echo "Enter the first number: ";
$num1 = trim(fgets(STDIN));   

echo "Enter the second number: ";
$num2 = trim(fgets(STDIN));  

echo "Enter the operator (+, -, *, /): ";
$operator = trim(fgets(STDIN));  


switch ($operator) {
    case '+':
        $result = $num1 + $num2;
        break;
    case '-':
        $result = $num1 - $num2;
        break;
    case '*':
        $result = $num1 * $num2;
        break;
    case '/':
        if ($num2 != 0) {
            $result = $num1 / $num2;
        } else {
            echo "Error: Division by zero is not allowed!\n";
            exit;
        }
        break;
    default:
        echo "Error: Invalid operator!\n";
        exit;
}


echo "Result: " . $result . "\n";
?>
