
num1 = float(input("Ingresa tu primer numero: "))
op = input("Ingresa tu operador:\nLista de operadores disponibles: "
           "\n + = suma \n - = resta \n / = division \n * = multiplicacion\n: ")
num2 = float(input("Ingresa tu segundo numero: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Error: Operador ingresado no valido")