#Módulo entra
#Requisitos: Este módulo apresenta função que lê dois números digitados pelo usuário.
#Autor: Jessica Prass
#Versão: 0.9.0
#Data: 31/08/2022

def entrada_numeros():
    numero_1 = float(input("\nDigite o primeiro número: "))
    numero_2 = float(input("\nDigite o segundo número: "))
    return [numero_1, numero_2]

def operacao():
    operacao = input("\nDigite a operação desejada, sendo + para somar, - para subtrair, / para dividir, * para multiplicar: ")
    return operacao
