#coding: utf-8
import random;


# Pilhagem de métodos.
def metodo_1():
    print "Começo do método 1...";
    metodo_2();
    print "Fim do método 1...";

def metodo_2():
    print "Começo do método 2...";
    metodo_3();
    print "Fim do método 2...";

def metodo_3():
    print "Começo do método 3...";
    print "Fim do método 3...";

# ===========================================
# Não é recursiva de fato, era só um exemplo.
def recursiva_1():
    for i in range(5, 0, -1):
        print i

def recursiva_2(num):
    print num;
    if (num > 0):
        recursiva_2(num - 1);

def potencia_0(a, b):
    resultado = 1;
    for i in range(b):
        resultado = resultado * a;
    return resultado;

# BICHO ESSE FOI LOCO.
def potencia_1(a, b):
    if (b == 0):
        return 1;
    elif (b == 1):
        return a;
    elif (b > 1):
        return a * potencia_1(a, b - 1);

def adivinharNumero(rnd):
    if (25 + rnd == 100):
        return rnd;
    else:
        return adivinharNumero(random.randint(1, 100))

def fatorial0(num):
    resultado = 1;
    for i in range(1, num + 1):
        resultado = resultado * i;
    return resultado;

def fatorial1(num):
    if (num == 1 or num == 0):
        return 1;
    else:
        return num * fatorial1(num - 1);

def mdc(a, b):
    if (a % b == 0):
        return a;
    else:
        #bleg


if __name__ == "__main__":
    print "O número que somado mais 4 é 8 é:", adivinharNumero(random.randint(1, 100));