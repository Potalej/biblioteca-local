import unidecode

def busca(arquivos:dict, palavras:list)->list:
    """
        Faz uma busca dentro dos arquivos a partir de lista de palavras.

        Quando se passar mais de uma palavra, o rankeamento será feito com base na quantidade de resultados por palavra mas também na quantidade de palavras por resultado. Assim, caso se pesquise por "Cálculo Diferencial" dentro de uma lista com os seguintes arquivos:
            
            - Cálculo Integral;
            - Cálculo Diferencial I;
            - Geometria Diferencial;
            - Cálculo Matricial.

        É natural que "Cálculo" receba a lista:
            
            [ Cálculo Integral, Cálculo Diferencial I, Cálculo Matricial ]
        
        enquanto que "Diferencial" deve receber a lista:
            
            [ Cálculo Diferencial I, Geometria Diferencial ]
        
        Porém, "Cálculo Diferencial I" tem as duas palavras, então tem inicialmente pontuação +2. Os resultados da lista de "Cálculo" recebem pontuação +3 (tamanho da lista) enquanto que os da "Diferencial" recebem +2 (tamanho da lista).

        A pontuação fica então:

            3 Cálculo Integral;
            7 Cálculo Diferencial I;
            2 Geometria Diferencial;
            3 Cálculo Matricial.
        
        Assim sendo, os arquivos retornados terão a seguinte ordem:

            i. Cálculo Diferencial I
            ii. Cálculo Integral
            iii. Cálculo Matricial
            iv. Geometria Diferencial
    """
    # retira acentuação das palavras
    palavras = [
        unidecode.unidecode(palavra).upper() for palavra in palavras
    ]

    # retira a acentuação dos arquivos
    arquivosUNI = [
        unidecode.unidecode(arquivo).upper() for arquivo in arquivos   
    ]

    # dict onde ficarão as quantidades de arquivos por palavra
    porPalavra = {palavra: [] for palavra in palavras}

    # pontuação
    pontuacao = {}

    # percorre os nomes dos arquivos
    for nomeArquivo in arquivosUNI:
        # verifica quais palavras correspondem
        correspondentes = [palavra for palavra in palavras if palavra in nomeArquivo]
        # e adiciona em cada palavra 1
        for palavra in correspondentes:
            porPalavra[palavra].append(nomeArquivo)

    # tendo feito tudo isso, agora é preciso verificar a quantidade de ocorrências das palavras
    for nomeArquivo in arquivos:
        uni = unidecode.unidecode(nomeArquivo).upper()
        pontos = 0
        for palavra in palavras:
            if uni in porPalavra[palavra]:
                pontos += 1 + len(porPalavra[palavra])
        pontuacao[nomeArquivo] = pontos

    # agora, ordena a pontuação em ordem decrescente
    ordenado = dict(sorted(pontuacao.items(), key = lambda x: pontuacao[x[0]], reverse=True))

    return [valor for valor in ordenado if ordenado[valor] > 0]        