# coding:utf-8


def naturais(n):
    """
    Essa função imprime todos os números de n até 50.
    :param n:
    :return:
    """
    # Printando o número atual.
    print n;

    # Caso o número atual não seja 50.
    if (n != 50):
        # Chamando a função novamente, mas incrementando o número atual.
        naturais(n + 1);

if __name__ == "__main__":
    naturais(0);