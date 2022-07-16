import subprocess

def abrirArquivo(dir:str)->None:
    """
        Abre um arquivo em determinado diretório.
    """
    # abre o arquivo
    subprocess.Popen([dir],shell=True)

def abrirPasta(dir:str)->None:
    """
        Abre uma pasta no explorer.
    """
    # precisa inverter as barras
    dir = dir.replace('/', '\\')
    # abre a apsta
    subprocess.Popen(f'explorer "{dir}"')

