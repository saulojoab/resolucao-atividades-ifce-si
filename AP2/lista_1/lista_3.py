#coding: utf-8
"""
Estudante: Saulo Joab Penha Simplício
Semestre: 2º

Questão 3:
Escreva uma função Python para calcular o fatorial de um número (um inteiro não negativo). A
função aceita o número como um argumento.
"""

def calcularFatorial(numero):
    """
    Essa função calcula o fatorial de um número inteiro positivo.
    Inicialmente, criamos uma variável resultado que recebe o valor 1.
    Após isso, enquanto o número inserido como parâmetro for maior que 1, multiplicamos ele pela variável "resultado"
    e subtraimos 1 do número.
    Finalmente, printamos o resultado na tela.
    :param numero:
    :return:
    """
    # Inicializando a variável resultado.
    resultado = 1;

    # Enquanto o número inserido for maior que 1.
    while (numero > 1):
        # Multiplicamos ele pela variável resultado (que inicialmente é 1).
        resultado = resultado * numero;
        # Subtraimos 1 do número inserido.
        numero = numero - 1;

    # Printando o resultado final.
    print resultado;

if __name__ == "__main__":
    # Chamando a função.
    calcularFatorial(4);