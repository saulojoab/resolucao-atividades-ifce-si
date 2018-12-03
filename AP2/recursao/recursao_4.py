# coding: utf-8

def checarPrimo (n, listaPrimos, nInicial):
    """
    Essa função verifica se um determinado número n é primo.
    :param n:
    :param listaPrimos:
    :param nInicial:
    :return:
    """

    # Se o resto da divisão do número n pelo número atual for 0.
    if (n % nInicial == 0):
        # Adicionamos o número atual na lista.
        listaPrimos.append(nInicial);

    # Se o número atual for igual ao número n.
    if (nInicial == n):
        # Verificamos se a lista contém apenas 2 números (1 e o número n).
        # Caso isso ocorra.
        if(listaPrimos.__len__() == 2):
            # Printamos que o número é primo.
            print "Primo";
        # Caso isso não ocorra.
        else:
            # Printamos que o número não é primo.
            print "Não é primo";
    # Se o número atual não for igual ao número n.
    else:
        # Chamamos a função novamente incrementando o número atual.
        checarPrimo(n, listaPrimos, nInicial + 1);

if __name__ == "__main__":
    checarPrimo(5, [], 1);