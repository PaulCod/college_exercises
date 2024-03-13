# 1 - Tuplas

# mochila = ("Machado", "Camisa", "Bacon", "Abacate")
# print(mochila[0])
# print(mochila[1:2])
#
#
# # mochila[2] = "ovos"
#
# for item in mochila:
#     print(f"Na minha mochila tem {item}")
#
# tam = len(mochila)
#
# for i in range(0, tam, 1):
#     print(mochila[i])
#
# upgrade = ("Queijo", "Canivete")
#
# mochila_grande = mochila + upgrade
# print(mochila_grande)
#
# def soma(*num):
#     soma = 0
#     print(f"Tupla: {num}")
#     for i in num:
#         soma += i
#     return soma
#
#
# print(f"Resultado: {soma(1, 2)}\n")
# print(f"Resultado: {soma(1, 2, 3, 4, 5, 6, 7, 8, 9)}")


# 2 - Lista

# mochila = ["Machado", "Camisa", "Bacon", "Abacate"]
# print("Lista: ", mochila)
#
# mochila[2] = "Laranja"
# print("Lista: ", mochila)
#
# mochila.append("Ovos")
# print(mochila)
#
# mochila.insert(0, "Canivete" )
# print(mochila)
#
# del mochila[1]
# print("mochila: ", mochila)
# mochila.remove("Ovos")
# print(mochila)

# x = [5, 6, 7, 8, 9]
# y = x
# print(x)
# print(y)
#
# y[0] = 2
# print(x)
# print(y)

# x = [5, 6, 7, 8, 9]
# y = x[:]
# y[0] = 2
# print(x)
# print(y)


# 3 - String e listas dentro de listas

# mochila = ["Machado", "Camisa", "Bacon", "Abacate"]
# print(mochila[0][2])
# print(mochila[2][1])

# mochila = ["Machado", "Camisa", "Bacon", "Abacate", ["Escova", "Pasta"]]
# print(mochila[4][1][2])
#
# for item in mochila:
#     for letras in item:
#         print(letras, end="")
#     print()

# for i in range(0, len(mochila), 1):
#     for j in range(0, len(mochila[i]), 1):
#         print(mochila[i][j], end="")
#     print()

# mochila = [["Cebola", 0.39], ["Tomate", 0.49], ["Maça", 0.89]]
# print(mochila[0][1])

# items = []
# mercado = []
#
# for i in range(3):
#     items.append(input("Digite o nome do item: "))
#     items.append(int(input("Digite a quantidade: ")))
#     items.append(float(input("Digite o valor: ")))
#     mercado.append(items[:])
#     items.clear()
# # print(mercado)
#
# soma = 0
# # print(mercado)
# print("-"*25)
# print("Item | Quantidade | Valor unitario | Total de item")
#
# for item in mercado:
#     print(f"{item[0]} | {item[1]} | {item[2]} | {item[1] * item[2]}")
#     soma += item[1] * item[2]
# print("-"*25)
# print(f"Total a ser pago: {soma}")


# 4 - Dicionarios

# game = {
#     "nome": "Super mario",
#     "desenvolvedora": "Nintendo",
#     "ano": 1990
# }
# print(game)
#
# for i in game.values():
#     print(i)
#
# print(game["nome"])
# print(game["desenvolvedora"])
# print(game["ano"])
#
# print(game.values())
# print(game.keys())
# print(game.items())

# games = []
#
# game = {
#     "nome": "Super mario",
#     "videogame": "Super Nintendo",
#     "ano": 1990
# }
# game2 = {
#     "nome": "Pokemon Scarlet e Violet",
#     "videogame": "Nintendo",
#     "ano": 2019
# }
#
# games = [game, game2]
# print(games)

# game = {}
# games = []
#
# for i in range(2):
#     game["nome"] = input("Digite o nome do game: ")
#     game["videogame"] = input("Digite o videogame: ")
#     game["ano"] = int(input("Digite o ano de lancamento: "))
#
#     games.append(game.copy())
# print("-" * 35)
# for e in games:
#     print(e.items())
#     for i, j in e.items():
#         print(f"O campo {i} tem o valor {j}")



# Metodos em string

# s1 = "Algoritmos"
# print(s1)
# s1[0] = "a"

# s1 = list("Algoritimos")
# print(s1)
# print("".join(s1))
#
# s1[0] = 'a'
# print("".join(s1))

# s1 = "Lógica de programação e Algoritmos"
# print(s1.startswith("Lógica"))
# print(s1.endswith("Algoritmos"))
# s1.lower().endswith("algoritmos")
# print(s1.count("a"))
# print(s1.split(" "))
# print(s1.replace("a", "mafagafo"))




