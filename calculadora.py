print("\nBienvenidos a la calculadora.\n")

valor_1 = input("Introduzca el primer valor: ")
valor_1 = int(valor_1)
valor_2 = input("Introduzca el segundo valor: ")
valor_2 = int(valor_2)

print("Elija una operación:\n1. Suma\n2. Resta\n3. Multiplicación\n4. División")
operacion = input()
operacion = int(operacion)

if operacion == 1:
    print(f"El resultado de la suma es {valor_1+valor_2}.")
elif operacion == 2:
    print(f"El resultado de la resta es {valor_1-valor_2}.")
elif operacion == 3:
    print(f"El resultado de la multiplicación es {valor_1*valor_2}.")
elif operacion == 4:
    print(f"El cociente de la división es {valor_1//valor_2} y el resto es {valor_1%valor_2}.")
else:
    print("Introduzca un valor válido.")
