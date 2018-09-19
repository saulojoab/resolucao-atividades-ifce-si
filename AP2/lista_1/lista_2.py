#coding: utf-8
"""
Estudante: Saulo Joab Penha Simplício
Semestre: 2º

Questão 2:
Escreva uma função em Python para reverter uma string.
Exemplo de cadeia de string: "1234abcd"
Saída esperada: "dcba4321"
"""

def invertendoString (stringParaInverter):
    """
    Essa função printa uma string de forma invertida.
    Primeiramente, o tamanho da string é armazenado em uma variável.
    A partir disso, percorremos a string começando pela última posição dela (que é o valor do tamanho da string) até a primeira.
    Finalmente, ao adicionar os caracteres em uma variável, retornamos a string invertida.
    :param stringParaInverter:
    :return:
    """
    # Armazenando o tamanho da string em uma variável.
    tamanhoDaString = stringParaInverter.__len__();
    string = "";

    # Enquanto a variável de tamanho da string for maior que 0.
    while (tamanhoDaString > 0):
        # Printamos os caracteres da string de forma invertida (do final para o começo).
        string += str(stringParaInverter[tamanhoDaString - 1]);
        # Subtraimos 1 da variável de tamanho da string.
        tamanhoDaString = tamanhoDaString - 1;

    return string;

if __name__ == "__main__":
    # Recebendo a string do usuário.
    stringTeste = raw_input("Insira a string para ser invertida: ");

    # Chamando a função e inserindo a string como parâmetro.
    print invertendoString(stringTeste);

