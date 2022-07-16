from src.python.busca import busca
from src.python.abrir import abrirArquivo, abrirPasta

def acao_buscar(geral:dict)->list:
    """
        Vai fazer a busca bonitinho.
    """
    entrada, arquivos = geral["entrada"], geral["arquivos"]

    # formata a entrada, separando em palavras-chave
    palavrasChave = entrada.split(":")[1].split(" ")
    # remove os vazios
    palavrasChave = [p for p in palavrasChave if len(p.replace(" ", ""))>0]

    print("\nBuscando pelas palavras-chave:", ", ".join(palavrasChave))

    # faz a busca
    resultadosBusca = busca(arquivos, palavrasChave)

    # exibe os resultados em ordem
    for idx, resultado in enumerate(resultadosBusca):
        print(f"{idx}. {resultado}")

    print("\n")

    return resultadosBusca

def acao_abrir(geral:dict)->list:
    """
        Abre arquivos informados pelos índices.
    """
    entrada, resultado, dir = geral["entrada"], geral["resultado"], geral["dir"]

    print("\nAbrindo arquivos...\n")

    # captura os números dos arquivos
    indices = entrada.split(":")[1].split(" ")
    # remove os vazios
    indices = [int(p) for p in indices if len(p.replace(" ", ""))>0]

    # abre os arquivos
    for ind in indices:
        # captura o diretório do arquivo
        abrirArquivo(geral["arquivos"][resultado[ind]])
    
    return resultado

def acao_pasta(geral:dict)->list:
    """
        Abre as pastas de arquivos informados pelos índices.
    """
    entrada, resultado, dir = geral["entrada"], geral["resultado"], geral["dir"]

    print("\nAbrindo pastas...\n")

    # captura os números dos arquivos
    indices = entrada.split(":")[1].split(" ")
    # remove os vazios
    indices = [int(p) for p in indices if len(p.replace(" ", ""))>0]

    # abre as pastas
    for ind in indices:
        # captura o diretório do arquivo
        diretorio = geral["arquivos"][resultado[ind]].replace(resultado[ind], "")
        abrirPasta(diretorio)
    
    return resultado

# DICT COM AS AÇÕES
acoes = {
    "buscar": acao_buscar,
    "abrir": acao_abrir,
    "pasta": acao_pasta
}