#coding:utf-8

lista = [1, 2, 57, 68, 51, 628, 563];

numero = 34;
cont = 0;
numeroDaMenorDiferenca = 0;
listaMenorDiferenca = [];

# Enquanto a lista tiver valores.
while (lista.__len__() > 0):
    # Pra cada valor da lista.
    for i in lista:
        # Se for o primeiro valor, setamos ele como a menor diferença.
        if (cont == 0):
            numeroDaMenorDiferenca = i;
            menorDiferenca = abs(34 - i);
        # Se não for o primeiro valor.
        else:
            # Se a diferença do numero com o valor for menor que a menor diferença atual.
            if (abs(34 - i) < menorDiferenca):
                # Setamos ele como a menor diferença.
                numeroDaMenorDiferenca = i;
                menorDiferenca = abs(34 - i);
        # Incrementando o cont.
        cont += 1;


    cont = 0;
    # Removendo o menor numero da lista.
    lista.remove(numeroDaMenorDiferenca);
    # Adicionando ele na lista de menor diferença.
    listaMenorDiferenca.append(numeroDaMenorDiferenca);

for i in listaMenorDiferenca:
    print i;