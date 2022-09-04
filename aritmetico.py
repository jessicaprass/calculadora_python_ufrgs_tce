#Módulo aritmetico
#Requisitos: Este módulo apresenta funções com as operações matemáticas.
#Autor: Jessica Prass
#Versão: 0.9.1
#Data: 31/08/2022

def calcula(lista_numeros, operacao):
    if operacao == "+":
        resultado = adicao(lista_numeros[0], lista_numeros[1])
    elif operacao == "-":
        resultado = subtracao(lista_numeros[0], lista_numeros[1])
    elif operacao == "/":
        resultado = divisao(lista_numeros[0], lista_numeros[1])
    elif operacao == "*":
        resultado = multiplicacao(lista_numeros[0], lista_numeros[1])
    else:
        print(f"\nOpção inválida.")
        return
    return resultado

def adicao(numero_1, numero_2):
    return int(numero_1) + int(numero_2)

def subtracao(numero_1, numero_2):
    return int(numero_1) - int(numero_2)

def divisao(numero_1, numero_2):
    if numero_2 == 0:
        return "Não se pode dividir por zero."
    return int(numero_1) / int(numero_2)

def multiplicacao(numero_1, numero_2):
    return int(numero_1) * int(numero_2)
