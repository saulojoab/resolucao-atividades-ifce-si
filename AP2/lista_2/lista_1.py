#coding: utf-8
"""
Estudante: Saulo Joab Penha Simplício
Semestre: 2º

Escreva uma função Python para encontrar o máximo de três números. Crie duas versões: uma
que use *args e outra que use *kwargs.
"""

def maiorNumeroArgs(*numeros):
    cont = 0;
    maiorNumero = 0;

    while (cont < numeros.__len__()):
        if (numeros[cont]> maiorNumero):
            maiorNumero = numeros[cont];
        cont = cont + 1;

    print "Maior número (arg): {}".format(maiorNumero);

def maiorNumeroKwarg(**numeros):
    maior = 0;

    for i in numeros.values():
        if (i > maior):
            maior = i;

    print "Maior número (kwarg): {}".format(maior);

if __name__ == "__main__":
    maiorNumeroArgs(1,2,3);
    maiorNumeroKwarg(primeiro=1,segundo=4,terceiro=3)