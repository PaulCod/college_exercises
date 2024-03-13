# Exercicio 1
import json
import os


# def somente_positivo(numero):
#     if numero < 0:
#         return False
#     return True
#
#
# def calcula_fatorial():
#     """
#     Calcula o fatorial de um numero inteiro fornecido pelo usuario
#     """
#
#     while True:
#         try:
#             resultado = 1
#             numero = int(input("Digite um numero inteiro: "))
#             if not somente_positivo(numero):
#                 print("Somente numero inteiro!!!")
#                 continue
#
#             if numero == 0:
#                 print(resultado)
#                 break
#
#             for i in range(numero, 1, -1):
#                 resultado *= i
#
#             print(f"O fatorial de {numero} é {resultado}")
#
#         except ValueError:
#             print("Numero invalido, Tente novamente")
#
#         except:
#             print("Ocorreu um erro, Tente novamente")
#
#
# help(calcula_fatorial)

# calcula_fatorial()



# Exercicio 2

def inicio():
    print("BEM VINDO")
    print("Temos as seguintes opções: \nC(Cadastrar novo item)\nL(Listar tudo cadastrado)")

    while True:
        try:
            opcao = menu_options()
            if opcao.strip().lower() == "c":
                cadastrar_item("dados.json")
                continue

            if opcao.strip().lower() == "l":
                listar_items("dados.json")

            if opcao.strip().lower() == "s":
                print("Saindo...")
                break

        except ValueError:
            print("Opção invalida")


def menu_options():
    opcao = input("Escolha uma opção: ")
    return opcao


def cadastrar_item(nome_arquivo):
    nome = input("Digite o nome do jogo: ")
    videogame = input("Digite a qual videogame pertence: ")

    dados = {
        "nome": nome,
        "videogame": videogame
    }
    try:
        with open(nome_arquivo, "a") as arquivo:
            if arquivo.tell() != 0:
                arquivo.write(",\n")
            json.dump(dados, arquivo, indent=2)
        print("Cadastrado com sucesso!!!")
        return

    except:
        print("Erro ao cadastrar jogo ")
        return

def listar_items(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            print("Itens cadastrados:")
            print("[")
            print(arquivo.read().strip())
            print("]")
    except FileNotFoundError:
        print("O arquivo '{}' não foi encontrado.".format(nome_arquivo))
    except Exception as e:
        print("Erro ao listar os itens:", e)

inicio()






