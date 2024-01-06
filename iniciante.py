#def calculadora(number1, number2, operador):
#    resultado = 0
#    match operador:
#        case "-":
#            resultado = number1 - number2
#        case "+":
#           resultado = number1 + number2
#        case "*":
#          resultado =  number1 * number2
#        case "/":
#           resultado = number1 / number2
#        case _:
#            'nao identifiquei'
#    return resultado



def calculadora(number1, number2, operador):
    resultado = 0
    if operador == "-":
        resultado = number1 - number2
    elif operador == "+":
        resultado = number1 + number2
    elif operador == "*":
        resultado = number1 * number2
    elif operador == "/":
        resultado = number1 / number2
    else:
        "não identifiquei"
    return resultado

number1 = input("insira o primeiro numero: ")
number2 = input("insira o segundo numero: ")
operador = input("Qual operacao deseja fazer? ")

print(calculadora(int(number1), int(number2), operador))