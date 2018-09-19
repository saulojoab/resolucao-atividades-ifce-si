# coding:utf-8
# DADOS DO ESTUDANTE:
# Nome: Saulo Joab Penha Simplício.
# Disciplina: AP2.
# Semestre: Segundo.
import random;

num = 0;

def  randomizing_dices():
    """
    Essa função serve pra randomizar dois dados e somar os seus resultados.
    O primeiro dado é sorteado de 1 à 6 e o resultado é mostrado no console.
    Igualmente, o segundo dado é sorteado de 1 à 6 e o resultado é mostrado no console.
    Finalmente, os dois resultados são somados e a função retorna o resultado da soma.

    DEV TALK: Como essa lógica vai ser repetida várias vezes, decidi colocar em uma função pra deixar o código mais limpo.
    :return:
    """
    dice1 = random.randint(1, 6);
    print "Dado 1:", dice1;

    dice2 = random.randint(1, 6);
    print "Dado 2:", dice2;

    result = dice1 + dice2;
    print "Soma dos dois dados:", result;
    return result;

def clear():
    """
    Essa função cria 30 linhas em branco no console.
    Ela é útil pra deixar o visual mais limpo.

    DEV TALK: Criei essa função pra evitar ter que repetir os prints diversas vezes, pois o código fica feio.
    :return:
    """
    print("*" * 30);

def dice_game(num):
    """
    Essa é a função principal do jogo de dados.
    O usuário tentará acertar o número da soma dos dados.
    A função retornará uma string com o resultado.
    :return:
    """

    # Se o número for maior que zero, e menor que 13.
    if (num > 0) and (num < 13):
        # Chamamos a função que retorna o valor da soma de dois dados aleatórios.
        result = randomizing_dices();
        # Caso a soma dos dados seja o número que o usuário informou, ele acertou.
        if (num == result):
            return "RESULTADO: Acertou, fuck yeah!";
        # Caso a soma dos dados não corresponda com o que o usuário informou, ele errou.
        else:
            return "RESULTADO: Opa, errou. Sorry.";

if __name__ == "__main__":
    print dice_game(int(input("Digite um número de 1 a 12: ")));