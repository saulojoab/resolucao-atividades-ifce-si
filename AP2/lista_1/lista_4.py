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
    """
    Essa função verifica se um determinado número está contido num intervalo de dois números.
    Primeiramente, são informado o número a ser verificado, o inicio e o fim do intervalo.
    Após isso, percorremos esse intervalo verificando cada número e averiguando se ele é igual ao número informado.
    Finalmente, informamos o resultado ao usuário.
    :param numero:
    :param inicio:
    :param fim:
    :return:
    """
    # Inicializando a variável.
    estaContido = False;

    # Pra cada número no intervalo que foi inserido.
    for i in range(inicio, fim):
        # Se o número atual for igual ao número informado pelo usuário.
        if (i == numero):
            estaContido = True;

    # Se o número informado pelo usuário estiver contido no intervalo.
    if (estaContido):
        print "O número {} está contido no intervalo [{},{}]".format(numero, inicio, fim);
    # Se o número informado não estiver no intervalo.
    else:
        print "O número {} não está contido no intervalo [{},{}]".format(numero, inicio, fim);

if __name__ == "__main__":
    # Recebendo os valores do usuário.
    numeroTeste = input("Insira o número a ser verificado no intervalo: ");
    inicioTeste = input("Insira o primeiro número do intervalo: ");
    fimTeste = input("Insira o último número do intervalo: ");

    # Chamando a função com os valores informados.
    verificarNumeroNoIntervalo(numeroTeste, inicioTeste, fimTeste);
