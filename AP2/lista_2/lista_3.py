# coding: utf-8
"""
Estudante: Saulo Joab Penha Simplício
Semestre: 2º

Questão 3:
Escreva uma função do Python para verificar se um número é perfeito ou não.
De acordo com a Wikipedia: Na teoria dos números, um número perfeito é um inteiro positivo
que é igual à soma de seus divisores naturais/positivos, isto é, a soma de seus divisores
positivos excluindo o próprio número (também conhecido como sua soma de alíquotas).
Equivalentemente, um número perfeito é um número que é metade da soma de todos os seus
divisores positivos (incluindo ele próprio).

Exemplo: O primeiro número perfeito é 6, porque 1, 2 e 3 são seus divisores positivos
apropriados, e 1 + 2 + 3 = 6. Equivalente, o número 6 é igual a metade da soma de todos os
seus divisores positivos: (1 + 2 + 3 + 6) / 2 = 6. O próximo número perfeito é 28 = 1 + 2 + 4 + 7
+ 14. Isto é seguido pelos números perfeitos 496 e 8128.

Procure utilizar modularização. Inicialmente implemente a função completa, depois procure
modularizar. Ex.: faça uma subfunção que determine os divisores de um número, outra que
verifique se a soma dos divisores resulta no número perfeito, além de outras que você
conseguir pensar.
"""

def verificarDivisores(numero):
    listaDeDivisores = []

    for i in range(1, numero):
        if (numero % i == 0):
            listaDeDivisores.append(i);

    return listaDeDivisores;

def verificarPerfeito(numero):
    lista = verificarDivisores(numero);

    if (sum(lista) == numero):
        print "O número {} é perfeito!".format(numero);
        print "A soma de seus divisores é: {}".format(sum(lista));
    else:
        print "O número {} não é perfeito!".format(numero);
        print "A soma de seus divisores é: {}".format(sum(lista));

if __name__ == "__main__":
    verificarPerfeito(496);
