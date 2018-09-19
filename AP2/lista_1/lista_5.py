#coding: utf-8
"""
Estudante: Saulo Joab Penha Simplício
Semestre: 2º

Questão 5:
Escreva um programa em Python para verificar a validade da entrada de senha pelos usuários.
● Pelo menos 1 letra entre [a-z] e 1 letra entre [A-Z].
● Pelo menos 1 número entre [0-9].
● Pelo menos 1 caractere de [$ # @].
● Comprimento mínimo 6 caracteres.
● Comprimento máximo 16 caracteres.
"""

def verificaMaiusculasMinusculas(string):
    """
    Essa função verifica se uma string possui ao menos um algarismo maiúsculo e um minusculo.
    Ela retorna um boolean dependendo do resultado da verificação.
    :param string:
    :return:
    """
    # Inicializando as variáveis.
    maiuscula = False;
    minuscula = False;

    # Pra cada caractere na string.
    for i in string:
        # Verifica se ele é maiúsculo.
        if (str(i).isupper()):
            maiuscula = True;
        # Verifica se ele é minúsculo.
        elif (str(i).islower()):
            minuscula = True;

    # Caso exista um maiúsculo E um minúsculo.
    if (maiuscula and minuscula):
        return True;
    # Caso não exista nenhum maiúsculo e minúsculo.
    else:
        return False;

def verificaNumero(string):
    """
    Essa função verifica se existe algum número em uma string.
    Ela retorna um boolean com o resultado.
    :param string:
    :return:
    """
    # Iniciando a variável.
    numero = False;

    # Pra cada caractere na string.
    for i in string:
        # Verificando se o caractere é um número.
        if (str(i).isdigit()):
            numero = True;

    # Caso exista algum número.
    if (numero):
        return True;
    # Caso não exista nenhum número.
    else:
        return False;

def verificaCaracteresEspeciais(string):
    """
    Essa função verifica se a string possui algum caractere especial.
    Ela retorna um boolean com o resultado.
    :param string:
    :return:
    """
    # Inicializando a variável.
    caractereEspecial = False;

    # Caso a string contenha algum dos caracteres especiais da atividade.
    if string.__contains__("$") or string.__contains__("#") or string.__contains__("@"):
        caractereEspecial = True;

    # Caso exista algum caractere especial na string.
    if (caractereEspecial):
        return True;
    # Caso não tenha nenhum caractere especial na string.
    else:
        return False;

def verificaTamanho(string):
    """
    Essa função verifica o tamanho da string inserida.
    Ela retorna um boolean verdadeiro caso o tamanho estiver entre 6 e 16.
    :param string:
    :return:
    """
    # Caso o tamanho da string estiver entre 6 e 16 caracteres.
    if (6 <= len(string) <= 16):
        return True;
    # Caso não esteja.
    else:
        return False;

def verificaSenha(string):
    """
    Essa função é basicamente a união de todas as funções anteriores:
    (verificaMaiusculasMinusculas, verificaNumero, verificaCaracteresEspeciais, verificaTamanho).

    Ela verifica se a string inserida corresponde com o que foi requisitado na questão.
    :param string:
    :return:
    """
    # Verificando se todas as outras funções retornam um boolean verdadeiro. Caso sim, avisa ao usuário que a senha está válida.
    if (verificaCaracteresEspeciais(string) and verificaMaiusculasMinusculas(string) and verificaNumero(string) and verificaTamanho(string)):
        return "Sua senha é válida!";
    # Caso alguma das funções retorne falso.
    else:
        return "Sua senha é inválida!";

if __name__ == "__main__":
    # Verificando se a senha informada pelo usuário está nos conformes.
    print verificaSenha(raw_input("Insira sua senha: "));

