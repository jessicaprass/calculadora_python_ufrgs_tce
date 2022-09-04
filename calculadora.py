# Programa calculadora
# Requisitos: Este programa calcula as operações matemáticas: soma, subtração, divisão e
# multiplicação, de dois números digitados pelo usuário e imprime o resultado na tela.
# Autor: Jessica Caroline Prass
# Versão: 0.0.2
# Data: 24/08/2022

# Definição de funções
def entrada_dados():
    numero_1 = float(input("\nDigite o primeiro número: "))
    numero_2 = float(input("\nDigite o segundo número: "))
    operacao = input("\nDigite a operação desejada, sendo + para somar, - para subtrair, / para dividir, * para multiplicar: ")
    return numero_1, numero_2, operacao
    
def aritmetico(operacao, numero_1, numero_2):
    if operacao == "+":
        resultado = int(numero_1) + int(numero_2)
    elif operacao == "-":
        resultado = int(numero_1) - int(numero_2)
    elif operacao == "/":
        resultado = int(numero_1) / int(numero_2)
    elif operacao == "*":
        resultado = int(numero_1) * int(numero_2)
    else:
        print(f"\nOpção inválida.")
        return False
    return resultado
        
def imprime(operacao, numero_1, numero_2, resultado):
    print(f"\nO resultado da operação {numero_1} {operacao} {numero_2} é igual {resultado}.")

def main():
    #Entrada de dados
    numero_1, numero_2, operacao = entrada_dados()

    # Processa dados
    resultado = aritmetico(operacao, numero_1, numero_2)

    # Saída de dados
    if resultado != False:
        imprime(operacao, numero_1, numero_2, resultado)

# Execução do programa
main()
