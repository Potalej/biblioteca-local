from os import listdir
from os.path import isfile, join

def listarGeral(dir:str)->list:
    """
        Lista os arquivos e pastas de um determinado diretório.
    """
    arquivos = [ f for f in listdir(dir) if isfile(join(dir, f))]
    pastas = [ f for f in listdir(dir) if f not in arquivos]
    return arquivos, pastas

def listarArvore(dir:str)->list:
    """
        A partir de um diretório inicial, cria uma árvore em um dict encadeando todas os arquivos dentro das pastas.
    """
    # a pasta será vista como um dict
    pasta = {"./":[]}
    # captura a primeira leva de arquivos
    arquivos, pastas = listarGeral(dir)
    # adiciona os arquivos ao "./" no dict
    pasta["./"] = arquivos

    # percorre a lista de pastas fazendo a mesma coisa
    for subpasta in pastas:
        # retorna um dicionário
        dict_subpasta = listarArvore(dir+"/"+subpasta)
        # adiciona o dicionário ao arquivo
        pasta[subpasta] = dict_subpasta

    return pasta

def listarArquivos(pasta:dict, dir:str)->list:
    """
        Recebe um dicionário fornecido pela `listarArvore` e cria uma lista única com todos os arquivos.
    """
    # vai ser um dict, onde a chave é o nome do arquivo e o valor é seu diretório
    arquivos = {}
    # primeiramente, adiciona os arquivos da própria pasta ("./")
    for arq in pasta["./"]:
        arquivos[arq] = dir + "/" + arq
    
    # percorre a lista de subpastas, fazendo a mesma coisa
    for subpasta in pasta:
        if subpasta == "./": continue
        # retorna o dict de arquivos
        arq_subpasta = listarArquivos(pasta[subpasta], dir + "/" + subpasta)
        # une os arquivos
        arquivos = dict(arquivos, **arq_subpasta)

    return arquivos