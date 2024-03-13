import random
from datetime import datetime

# 1
# notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
# print(f"{notas.count(7)} alunos tiram a nota 7")
#
# notas.pop()
# notas.append(4)
# print(notas)
#
# print(max(notas))
#
# sorted_num = sorted(notas)
# print(sorted_num)
#
# print(f"A media dos numeros da lista é {round(sum(notas) / len(notas), 2)}")


# 2
# vogais = ["a", "e", "i", "o", "u"]
# palavras = ("Madeira", "Planta", "Arroz", "Teste", "Cadeira", "Controle", "Pedra", "Fone", "Notebook", "Caneta")
# for palavra in palavras:
#     listVogais = [letra for letra in palavra.lower() if letra in vogais]  # Convertendo a palavra para minúsculas para tornar a comparação de vogais case-insensitive
#     print(f"A palavra {palavra} possui as vogais {listVogais}")


#3

# escolhas = {
#     1: "Pedra",
#     2: "Papel",
#     3: "Tesoura"
# }
#
# historicoResult = {
#     "vitoria": 0,
#     "derrota": 0
# }
#
# resultados = {
#     ("Pedra", "Tesoura"): "Você ganhou!",
#     ("Papel", "Pedra"): "Você ganhou!",
#     ("Tesoura", "Papel"): "Você ganhou!",
#     ("Pedra", "Papel"): "Você perdeu!",
#     ("Papel", "Tesoura"): "Você perdeu!",
#     ("Tesoura", "Pedra"): "Você perdeu!",
#     ("Pedra", "Pedra"): "Empate!",
#     ("Papel", "Papel"): "Empate!",
#     ("Tesoura", "Tesoura"): "Empate!",
# }
#
# def gera_numero_aleatorio():
#     return random.randint(1, 3)
#
#
def printPainel(message):
    print("-"*30)
    print(message)
    print("-"*30)
#
#
# def print_regras():
#     print("0 - Sair")
#     print("1 - Pedra")
#     print("2 - Papel")
#     print("3 - Tesoura")
#
# # Pedra1 < Papel2 && Pedra1 > Tesoura3 && Tesoura3 > Papel2
#
#
# def resultado(escolhaUsuario, escolhaMaquina):
#     eu = escolhas[escolhaUsuario]
#     em = escolhas[escolhaMaquina]
#     if eu == em:
#         print("Empate!!!")
#     elif (eu == "Pedra" and em == "Tesoura") or (eu == "Papel" and em == "Pedra") or (eu == "Tesoura" and em == "Papel"):
#         print(f"Voce ganhou!! {eu} vence {em}")
#         historicoResult["vitoria"] += 1
#     else:
#         print(f"Você perdeu! {em} vence {eu}")
#         historicoResult["derrota"] += 1
# printPainel("BEM VINDO!!")
# print_regras()
# while True:
#
#     try:
#         num_user = int(input("Escolha uma opção: "))
#
#         if num_user == 0:
#             print(f'Voce ganhou {historicoResult["vitoria"]} e perdeu {historicoResult["derrota"]}')
#             print("Encerrando o programa...")
#             break
#         elif num_user in (1, 2, 3):
#             resultado(num_user, gera_numero_aleatorio())
#         else:
#             print("Escolha uma opção valida")
#
#     except ValueError:
#         print("Digite uma opção valida")
#         continue


# 4
pessoas = []

def calculaMedia(pessoas):
    somatorio = 0
    ano_atual = datetime.now().year
    for pessoa in pessoas:
        idade = ano_atual - pessoa["ano_nascimento"]
        somatorio += idade
    return somatorio / len(pessoas)

def total_cadastro(pessoas):
    return len(pessoas)

def f_menos_30(pessoas):
    pessoa_menos = []
    ano_atual = datetime.now().year
    for pessoa in pessoas:
        idade = ano_atual - pessoa["ano_nascimento"]
        if pessoa["sexo"] == "f" and idade < 30:
            pessoa_menos.append({"nome": pessoa["nome"], "idade": idade})

    return pessoa_menos


def h_idade_acima(pessoas):
    ac = 0
    count = 0
    pessoa_mais = []
    ano_atual = datetime.now().year

    for pessoa in pessoas:
        idade = ano_atual - pessoa["ano_nascimento"]
        if pessoa["sexo"] == "m":
            ac += idade
            count += 1

    media_idade = ac / count
    for pessoa in pessoas:
        idade = ano_atual - pessoa["ano_nascimento"]
        if idade > media_idade:
            pessoa_mais.append({"nome": pessoa["nome"], "idade": idade})

    return pessoa_mais


printPainel("BEM VINDO!!")
while True:
    try:
        for _ in range(0, 8, 1):
            nome = input("Digite seu nome: ")
            sexo = input("Digite seu sexo (m/f): ").lower()
            if sexo not in ("f", "m"):
                print("Por Favor, digite 'm' para masculino ou 'f' para feminino")
                continue
            anoNasc = int(input("Digite o ano de seu nascimento: "))

            pessoas.append({"nome": nome, "sexo": sexo, "ano_nascimento": anoNasc})
        print(f"Total de cadastros: {len(pessoas)}")
        print(f"Media de idade das pessoas: {calculaMedia(pessoas)}")
        print(f"Mulheres com menos de 30 anos: {f_menos_30(pessoas)}")
        print(f"homens com idade acima da media: {h_idade_acima(pessoas)}")
        break

    except ValueError:
        print("insira uma ano de nascimento valido")
        continue

    finally:
        print(pessoas)


