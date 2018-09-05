#coding: utf-8
"""
Estudante: Saulo Joab Penha Simplício
Semestre: 2º

Escreva uma função Python para encontrar o máximo de três números. Crie duas versões: uma
que use *args e outra que use *kwargs.
"""

def maiorNumeroArgs(*numeros):
    """
    Verificando o maior número dentre os números informados (por meio de *args).
    :param numeros:
    :return:
    """

    # Inicializando as variáveis.
    cont = 0;
    maiorNumero = 0;

    # Enquanto o contador for menor que a quantidade de numeros informados.
    while (cont < numeros.__len__()):
        # Verifica se o numero atual é maior do que o maior número anterior (iniciando do 0).
        if (numeros[cont]> maiorNumero):
            maiorNumero = numeros[cont];
        # Acrescentando +1 ao nosso contador.
        cont = cont + 1;

    # Mostrando o maior número ao usuário.
    print "Maior número (arg): {}".format(maiorNumero);

def maiorNumeroKwarg(**numeros):
    """
    Essa função verifica o maior número dentre os números informados (usando *kwargs).
    :param numeros:
    :return:
    """
    # Inicializando a variável.
    maior = 0;

    # Pra cada número informado.
    for i in numeros.values():
        # Se o número atual for maior que o maior número anterior (iniciando do 0).
        if (i > maior):
            maior = i;

    # Informando o maior número ao usuário.
    print "Maior número (kwarg): {}".format(maior);

if __name__ == "__main__":
    # Chamando as duas funções e informando seus valores.
    maiorNumeroArgs(1,2,3);
    maiorNumeroKwarg(primeiro=1,segundo=4,terceiro=3);