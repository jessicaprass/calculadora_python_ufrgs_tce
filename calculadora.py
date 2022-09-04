# Programa calculadora
# Requisitos: Este programa calcula as operações matemáticas: soma, subtração, divisão e
# multiplicação, de dois números digitados pelo usuário e imprime o resultado na tela.
# Autora: Jessica Caroline Prass
# Versão: 0.0.1
# Data: 29/08/2022

# Entrada de dados
numero_1 = float(input("\nDigite o primeiro número para calcular: "))
numero_2 = float(input("\nDigite o segundo número para calcular: "))
operacao = input("\nDigite a operação desejada, sendo + para somar, - para subtrair, / para dividir, * para multiplicar: ")

# Processa dados
if (operacao == "+"):
    resultado = int(numero_1) + int(numero_2)
elif (operacao == "-"):
    resultado = int(numero_1) - int(numero_2)
elif (operacao == "/"):
    resultado = int(numero_1) / int(numero_2)
elif (operacao == "*"):
    resultado = int(numero_1) * int(numero_2)
else:
    print(f"\nOpção inválida.")

# Saída de dados
print(f"\nO resultado da operação {numero_1} {operacao} {numero_2} é igual {resultado}.")
