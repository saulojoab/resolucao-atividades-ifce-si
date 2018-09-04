#coding: utf-8
"""
Estudante: Saulo Joab Penha Simplício
Semestre: 2º

Questão 4:
Escreva uma função Python para verificar se um número está em um determinado intervalo. A
função deve receber 3 valores como argumento: o primeiro deve ser o número a ser testado, o
segundo indica o começo do intervalo e o terceiro indica o final do intervalo.
"""

def verificarNumeroNoIntervalo(numero, inicio, fim):
    estaContido = False;

    for i in range(inicio, fim):
        if (i == numero):
            estaContido = True;

    if (estaContido):
        print "O número {} está contido no intervalo [{},{}]".format(numero, inicio, fim);
    else:
        print "O número {} não está contido no intervalo [{},{}]".format(numero, inicio, fim);

if __name__ == "__main__":
    numeroTeste = input("Insira o número a ser verificado no intervalo: ");
    inicioTeste = input("Insira o primeiro número do intervalo: ");
    fimTeste = input("Insira o último número do intervalo: ");

    verificarNumeroNoIntervalo(numeroTeste, inicioTeste, fimTeste);
