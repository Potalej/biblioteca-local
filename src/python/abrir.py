import subprocess

def abrirArquivo(dir:str)->None:
    """
        Abre um arquivo em determinado diretório.
    """
    subprocess.Popen([dir],shell=True)