# coding: utf-8
"""
Estudante: Saulo Joab Penha Simplício
Semestre: 2º

Questão 2:
Escreva uma função Python que verifique se uma string (não necessariamente uma palavra) é
palíndromo ou não.
Nota: Um palíndromo é uma palavra, frase ou sequência que lê o mesmo para trás, por
exemplo, “Hannah”, “Subi no ônibus” entre outros.

https://www.megacurioso.com.br/comunicacao/99015-subi-no-onibus-20-palindromos-que-voce
-gostaria-de-ter-imaginado.htm
"""

# DISCLAIMER: A lógica em si funciona, porém, por algum motivo, ele não aceita acentos e coisas do tipo.
# Eu tentei verificar se era alguma coisa na codificação mas não encontrei nenhuma solução.

def verificarPalindromo(string):
    stringInvertida = "";
    cont = string.__len__();

    while(cont > 0):
        stringInvertida = stringInvertida + string[cont - 1];
        cont = cont - 1;

    if (stringInvertida.replace(" ", "").lower() == string.replace(" ", "").lower()):
        print "{} e {} são palíndromos!".format(stringInvertida, string);
    else:
        print "{} e {} não são palíndromos!".format(stringInvertida, string);

if __name__ == "__main__":
    string = "Subi no onibus";

    verificarPalindromo(string);