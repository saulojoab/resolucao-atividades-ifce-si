# coding:utf-8

def maiorElementoArray(array, maiorElementoAtual, cont):
    """
    Essa função verifica qual o maior elemento de um array.
    :param array:
    :param maiorElementoAtual:
    :param cont:
    :return:
    """

    # A frase seguinte é muito confusa mas faz sentido (espero, eu to com sono):
    # Se o elemento da posição do número atual for maior que o maior número atual.
    if (array[cont] > maiorElementoAtual):
        # O elemento atual se torna o maior número.
        maiorElementoAtual = array[cont];

    # Se o contador somado com dois (devido às posições do array) for maior que o número de elementos do array.
    if (cont + 2 > array.__len__()):
        # Printamos o resultado.
        print maiorElementoAtual;
    # Caso não seja.
    else:
        # Chamamos a função e incrementamos o contador.
        maiorElementoArray(array, maiorElementoAtual, cont + 1);

if __name__ == "__main__":
    array = [1,2,3]
    maiorElementoArray(array, array[0], 0);
