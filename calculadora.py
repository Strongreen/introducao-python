def calculadora(number1, number2, operador):
    resultado = 0
    match operador:
        case "-":
            resultado = int(number1) - int(number2)
        case "+":
            resultado = int(number1) + int(number2)
        case "*":
            resultado = int(number1) * int(number2)
        case "/":
            resultado = int(number1) / int(number2)
        case _:
            'operador não identificado'
    return resultado

number1 = input('digite o primeiro numero: ')
number2 = input('digite o segundo numero: ')
operador = input('digite o operador: ')

print(calculadora(number1, number2, operador))
        
