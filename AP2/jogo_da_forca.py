#coding: utf-8
import random

def tamanhoString(palavra):
    """
    Essa função retorna um int com o número de caracteres em uma palavra.
    :param palavra:
    :return:
    """
    # Essa variável irá armazenar o tamanho da string.
    tamanho = 0;

    # Enquanto houverem caracteres na string.
    while(True):
        try:
            # Se a letra não for vazia, incrementamos a variável de tamanho.
            if (palavra[tamanho] != None):
                tamanho = tamanho + 1;
        # Caso não tenha mais nenhuma letra pra percorrer.
        except IndexError:
            break;

    # Retornamos a variável do tamanho.
    return tamanho;

def tamanhoLista(lista):
    """
    Essa função retorna o número de elementos em uma lista.
    :param lista:
    :return:
    """

    # Essa variável vai armazenar o número de elementos na lista.
    cont = 0;

    # Pra cada elemento na lista.
    for i in lista:
        # Incrementamos o contador.
        cont = cont + 1;

    # Retornando o tamanho da lista.
    return cont;

def sortearPalavra(lista):
    """
    Essa função retorna uma palavra aleatória de dentro de uma lista.
    :return:
    """
    # Acessando uma posição aleatória da lista e armazenando ela em uma variável.
    palavraSorteada = lista[random.randint(0, tamanhoLista(lista))];

    # Retornando a palavra.
    return palavraSorteada;

def ocultarString(palavra):
    """
    Essa função transforma todas as letras de uma palavra em hífens.
    :param palavra:
    :return:
    """
    # Essa variável irá armazenar a palavra oculta.
    palavraOculta = "";

    # Pra cada letra na palavra informada.
    for l in palavra:
        # Adicionamos um hífen à palavra oculta.
        palavraOculta = palavraOculta + "-"

    # Retornando a palavra oculta.
    return palavraOculta;

def contemLetra(string, letra):
    """
    Essa função verifica se uma string contém uma determinada letra e conta quantas vezes ela se repete.
    :param string:
    :param letra:
    :return:
    """
    # Essa variável vai armazenar quantas vezes a letra se repete.
    contador = 0;

    # Pra cada letra na string.
    for i in string:
        # Se a letra atual da string for igual à letra informada.
        if (i == letra):
            # Retorna verdadeiro.
            contador = contador + 1;

    # Caso a string não conter a letra, retorna falso.
    return contador;

def listaContem(lista, valor):
    """
    Essa função verifica se uma lista contém um determinado valor.
    :param lista:
    :param valor:
    :return:
    """
    # Para cada valor na lista.
    for i in lista:
        # Se o valor atual for igual ao valor informado.
        if (i == valor):
            # Retornamos verdadeiro.
            return True;

    # Caso a lista não conter o valor, retorna falso.
    return False;

def limparConsole():
    """
    Essa função printa 30 linhas vazias no console.
    :return:
    """
    print "\n" * 30;

def transformarStringLista():
    """
    Essa função transforma uma string com várias palavras em uma lista de palavras.
    :return:
    """
    # Variaveis.
    start = 0;
    lista = [];
    palavra = "";
    palavras = "fato amor vies brio esmo apos mito acao apto ermo sede area crer puta vide alem mote pois onus ruim suma tolo veio ente soar cedo gozo cota coxo urge sela vida caos cela meio numa medo pose fase pude zelo cujo como alva face sera asco nexo agir alvo nojo onde base voce ater teve rege rude vovo agil sina teor ocio alta tras casa jugo traz auto peco voga tudo idem ante vale mais joia deus auge prol todo quao orla doce alto rima mero seio util rito frio evoe amar novo logo algo lume pneu tese coca embuste conjuge excecao empatia prolixo efemero estoria pesames analogo idilico sublime sucinto cinismo genuino estavel audacia recesso prodigo carater refutar astucia inferir aurelio cordial exortar apatico emergir escoria litigio acepcao isencao imputar trivial excesso fomento conciso candura aspecto atraves excerto frivolo sintese morbido austero anatema padecer ambiguo exilado estirpe oriundo empafia auferir verbete virtude salutar inercia ambicao alcunha ansioso incauto alegria contudo parcial despota notorio mitigar ademais almejar limpido assento intuito hesitar preciso sensato intenso indagar familia iconico mancebo colosso difusao deferir escasso espurio afeccao definir relacao volupia neofito desidia deleite vigente sentido imersao varonil integro aptidao bizarro afeicao volatil sagaz algoz exito amago mexer senso porra termo afeto sutil inato nobre desde cerne porem audaz secao vigor fazer ideia mutuo anexo aquem lapso mutua seria etica torpe poder gleba impio genro razao detem justo sanar honra posse ardil expor muito habil futil digno atroz negro tenaz moral assim coser dizer prole ansia avido egide corja cozer plena brado reves tange pesar pifio animo vicio obice comum causa nenem ceder pleno dever censo denso tenro culto ontem atras fugaz ebrio louco afago clava fluir impor tenue saber seara entao cisma apice pudor regra jeito fosse serio gesto haver sinto gerar";

    # Para cada caractere na string.
    for e in range(0, tamanhoString(palavras)):
        # Caso o caractere atual seja um espaço, tudo o que tiver antes dele será uma palavra.
        if (palavras[e] == " "):
            # Para cada caractere da última posição inicial até o espaço.
            for i in range(start, e):
                # Pegamos cada caractere e formamos uma nova palavra.
                palavra = palavra + palavras[i];

            # Adicionamos a palavra formada em uma lista.
            lista.append(palavra);
            # Esvaziamos a variavél de palavra para gerar a próxima e evitar repetições.
            palavra = "";
            # Na próxima vez que o FOR for executado, ele irá iniciar da posição após o espaço.
            start = e + 1;

    # Retornando a lista de palavras.
    return lista;

def mainJogo(modo):
    """
    Esse é o procedimento principal. Basicamente, é a lógica do jogo.
    :param modo:
    :return:
    """
    # Essa lista irá armazenar as letras que o usuário acertar.
    listaDeLetrasCertas = [];

    # Se o usuário escolher jogar Singleplayer.
    if (modo == 1):
        # Sorteamos a palavra aleatória.
        palavraRandom = sortearPalavra(transformarStringLista());
    # Se o usuário escolher jogar Multiplayer.
    else:
        # O usuário insere a palavra pra tentar adivinhar.
        palavraRandom = raw_input("Insira a palavra pro seu amigo jogar: ");

    # O número de tentativas será igual ao número de caracteres na palavra.
    tentativas = tamanhoString(palavraRandom);
    # Essa variável irá armazenar a tentativa atual do usuário.
    tentativaAtual = tentativas;

    # Limpando o console.
    limparConsole();

    print "== Palavra atual:", ocultarString(palavraRandom);

    # Isso irá repetir de acordo com a quantidade de tentativas.
    for i in range(0, tentativas):
        # Essa variável irá armazenar a tentativa do usuário de acertar a palavra.
        letra = raw_input("Insira uma letra da palavra: ");

        # Se a palavra aleatória não contem a letra que o usuário tentou adivinhar.
        if (contemLetra(palavraRandom, letra) == 0):
            limparConsole();
            print "Errou!";
        # Se a palavra aleatória contem a letra que o usuário tentou adivinhar e essa letra se repete.
        elif (contemLetra(palavraRandom, letra) > 1):
            limparConsole();
            print "Acertou! Essa letra se repete",contemLetra(palavraRandom, letra), "vezes.";
            # Adicionando a letra à lista de letras certas.
            listaDeLetrasCertas.append(letra);
        # Se a palavra aleatória contem a letra que o usuário tentou adivinhar e essa letra não se repete.
        elif (contemLetra(palavraRandom, letra) == 1):
            limparConsole();
            print "Acertou! Essa letra não se repete..";
            # Adicionando a letra à lista de letras certas.
            listaDeLetrasCertas.append(letra);

        # Decrescendo a tentativa atual.
        tentativaAtual = tentativaAtual - 1;

        # Se as tentativas acabarem.
        if (tentativaAtual == 0):
            limparConsole();
            print "Ok, chegou a reta final. Tente adivinhar a palavra."
            print "Palavra oculta:", ocultarString(palavraRandom);
            # Listando as letras que o usuário acertou.
            print "- Letras certas:",
            # Caso ele tenha acertado alguma letra.
            if (listaDeLetrasCertas):
                for i in listaDeLetrasCertas:
                    print i,
            # Caso ele não tenha acertado nenhuma letra.
            else:
                print "Nenhuma!",
            print " ";

            # Recebendo a tentativa final do usuário.
            adivinhacao = raw_input("\nInsira o que você acha que é: ");

            print "E a palavra é...", palavraRandom, "!";

            # Se o usuário acertou a palavra.
            if (adivinhacao == palavraRandom):
                print "Parabéns, você ganhou!";
            # Caso ele tenha errado.
            else:
                print "Você errou..."
            # Saindo do FOR.
            break;

        # Se o usuário inserir uma palavra ao invés de uma letra.
        elif (tamanhoString(letra) > 1):
            print "= VOCÊ INSERIU UM PALPITE DE PALAVRA =";
            print "E a resposta é...", palavraRandom, "!";

            # Se o usuário acertou o palpite.
            if (letra == palavraRandom):
                print "Parabéns, você ganhou!";
            # Se ele errou.
            else:
                print "Você errou..."
            break;

        print "== Palavra atual:", ocultarString(palavraRandom);
        # Listando as letras que ele acertou até agora.
        print "- Letras certas até agora:",
        for i in listaDeLetrasCertas:
            print i,
        print " ";
        print "- Tentativas restantes:", tentativaAtual

if __name__ == "__main__":
    modo = input("Insira o modo de jogo (1 = Singleplayer | 2 = Multiplayer): ");
    mainJogo(modo);