# coding:utf-8

def conversaoDecimalBinario(numero, binario):
    """
    Essa função converte um número decimal em um número binário em forma de string.
    :param numero:
    :param binario:
    :return:
    """

    # Concatenando o resto da divisão do número por dois com a string do número binário.
    binario = str(numero % 2)+ binario;

    # Se o número dividido por 2 (divisão inteira) não for 0.
    if (numero / 2 != 0):
        # Chamamos a função novamente com o número dividido por 2.
        conversaoDecimalBinario(numero/2, binario);
    # Se o número dividido por 2 (divisão inteira) for 0.
    else:
        # Printamos o resultado.
        print binario;

if __name__ == "__main__":
    conversaoDecimalBinario(156, "");