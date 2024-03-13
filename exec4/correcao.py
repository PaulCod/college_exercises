def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x


def cria_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, "wt+")
        a.close()
    except:
        print("Erro na criação do arquivo")
    else:
        print(f"Arquivo {nome_arquivo} foi criado com sucesso")


def existe_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, "at")
    except:
        print("Erro ao abrir o arquivo")
    else:
        a.write(f'{nomeJogo};{nomeVideogame}\n')
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, "rt")
    except:
        print("Erro ao ler arquivo")
    else:
        print(a.read())
    finally:
        a.close()


arquivo = "games.txt"
if existe_arquivo(arquivo):
    print("Arquivo localizado no computador")
else:
    print("Arquivo inexistente")
    cria_arquivo(arquivo)

while True:
    print("MENU")
    print("1 - Cadastrar novo item")
    print("2 - Listar cadastros")
    print("3 - Sair")

    op = valida_int("Escolha a opção desejada: ", 1, 3)
    match op:
        case 1:
            print("Cadastrar")
            nomeJogo = input("Nome do jogo: ")
            nomeVideogame = input("Nome do videogame: ")
            cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
        case 2:
            print("Listar")
            listarArquivo(arquivo)
        case 3:
            print("Encerrando o programa...")
            break


