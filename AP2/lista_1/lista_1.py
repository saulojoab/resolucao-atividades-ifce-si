#coding: utf-8
"""
Estudante: Saulo Joab Penha Simplício
Semestre: 2º

Questão 1:
Escreva uma função Python para somar todos os números em uma lista passada como
parâmetro..
Lista de amostras: (8, 2, 3, 0, 7)
Saída esperada: 20
"""

def somarElementosDaLista(lista):
    """
    Essa função recebe uma lista como parâmetro.
    Inicialmente, criamos uma variável "soma" que recebe o valor zero.
    Após isso, percorremos a lista que foi utilizada como parâmetro.
    Para cada elemento dessa lista, somamos esse elemento à nossa variável "soma".
    No final, printamos o resultado da soma.
    :param lista:
    :return:
    """
    # Inicializando a variável de soma.
    soma = 0;

    # Para cada elemento na lista.
    for i in lista:
        # Somamos esse elemento com nossa variável soma.
        soma = soma + i;

    # Printando o resultado.
    print soma;

if __name__ == "__main__":
    # Criando uma lista de exemplo.
    listaDeExemplo = [8, 2, 3, 0, 7];

    # Chamando a função e inserindo nossa lista de exemplo como parâmetro.
    somarElementosDaLista(listaDeExemplo);
