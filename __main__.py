#Programa __main__
#Requisitos: Este programa importa os módulos entra, aritmetico e saida, após ler dois números e a operação matemárica digitado pelo usuário, calcula e imprime na tela o resultado.
#Autor: Jessica Prass
#Versão: 1.0.0
#Data: 31/08/2022

import entra
import aritmetico
import saida

def main():
    lista_numeros = entra.entrada_numeros()
    operacao = input("\nDigite a operação desejada, sendo + para somar, - para subtrair, / para dividir, * para multiplicar: ")
    
    resultado = aritmetico.calcula(lista_numeros, operacao)

    if resultado != None:
        saida.imprime(lista_numeros, operacao, resultado)
    
if __name__ == "__main__":
    main()

