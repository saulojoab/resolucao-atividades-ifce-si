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
    maiuscula = False;
    minuscula = True;

    for i in string:
        if (str(i).isupper()):
            maiuscula = True;
        elif (str(i).islower()):
            minuscula = True;

    if (maiuscula and minuscula):
        return True;
    else:
        return False;

def verificaNumero(string):
    numero = False;

    for i in string:
        if (str(i).isdigit()):
            numero = True;

    if (numero):
        return True;
    else:
        return False;

def verificaCaracteresEspeciais(string):
    caractereEspecial = False;

    if string.__contains__("$") or string.__contains__("#") or string.__contains__("@"):
        caractereEspecial = True;

    if (caractereEspecial):
        return True;
    else:
        return False;

def verificaTamanho(string):
    if (6 <= len(string) <= 16):
        return True;
    else:
        return False;

def verificaSenha(string):
    if (verificaCaracteresEspeciais(string) and verificaMaiusculasMinusculas(string) and verificaNumero(string) and verificaTamanho(string)):
        print "Sua senha é válida!";
    else:
        print "Sua senha é inválida!";

if __name__ == "__main__":
    senha = raw_input("Insira sua senha: ");
    verificaSenha(senha);

