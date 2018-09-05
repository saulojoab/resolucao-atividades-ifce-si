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
    """
    Essa função verifica se uma string é palíndroma (igual de trás pra frente).
    Inicialmente, invertemos a string.
    Depois, verificamos se ela é igual à original mesmo estando invertida.
    Finalmente, informamos ao usuário.
    :param string:
    :return:
    """
    # Inicializando as variáveis.
    stringInvertida = "";
    cont = string.__len__();

    # Enquanto o tamanho da string original (contador) for maior que 0.
    while(cont > 0):
        # Adicionando os caracteres na string ao contrário.
        stringInvertida = stringInvertida + string[cont - 1];
        # Diminuindo o tamanho da string original (contador).
        cont = cont - 1;

    # Retirando os espaços em branco e verificando se a string invertida é igual à original.
    if (stringInvertida.replace(" ", "").lower() == string.replace(" ", "").lower()):
        print "{} e {} são palíndromos!".format(stringInvertida, string);
    # Caso ela não seja.
    else:
        print "{} e {} não são palíndromos!".format(stringInvertida, string);

if __name__ == "__main__":
    # Recebendo a entrada do usuário.
    string = raw_input("Insira a frase a ser verificada: ");
    # Chamando a função para verificar.
    verificarPalindromo(string);