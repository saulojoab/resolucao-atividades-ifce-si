# coding: utf-8

def somaUmAteN(n, nInicial, soma):
    """
    Essa função mostra a soma de todos os números de 1 até n.
    :param n:
    :param nInicial:
    :param soma:
    :return:
    """
    # Incrementando a soma com o número atual.
    soma += nInicial;

    # Se o número atual somado com 1 for maior que o número limite.
    if (nInicial + 1 > n):
        # Printamos o resultado da soma.
        print soma;
    # Se o número atual somado com 1 for menor que o número limite.
    else:
        # Chamamos a função novamente e incrementamos o número atual.
        somaUmAteN(n, nInicial + 1, soma);


if __name__ == "__main__":
    somaUmAteN(3, 1, 0);