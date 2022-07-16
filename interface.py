from acoes import acoes
from src.python.listar import listarArvore, listarArquivos

# diretório padrão em meu computador
dir="C:/Users/zmath/OneDrive/Documentos/Pastas/livros"

# faz o alistamento em árvore dos arquivos
arvore = listarArvore(dir)
# captura todos os arquivos num dict só
arquivos = listarArquivos(arvore, dir)

# dicionário com informações gerais
geral = {
    "dir": dir,
    "entrada": 0,
    "resultado": 0,
    "arquivos": arquivos,
    "arvore": arvore,
}

# divisor
div = 20*"="+"\n"

print(f"{div}  Biblioteca Local\n{div}")


# roda sempre
while True:
    # ação
    entrada = input(">>> ")
    # se falar "sair", encerra
    if entrada == "sair": break

    # a ação estará antes de um ":", então captura ela
    acao = entrada.split(":")[0].replace(" ", "")

    # verifica se a ação está na lista de ações
    if acao not in acoes:
        print("Ação não encontrada, tente novamente!\n")
        continue

    geral["entrada"] = entrada

    # roda a ação
    resultado = acoes[acao](geral)

    geral["resultado"] = resultado