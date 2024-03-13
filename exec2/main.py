# Tema 1
# number1 = int(input("Digite o primeiro valor: "))
# number2 = int(input("Digite o segundo valor valor: "))
# if number1 > number2:
#     print("O primeiro valor é maior do que o segundo")
# elif number1 < number2:
#     print("O segundo valor é maior do que o primeiro valor")
# else:
#     print("os valores são iguais")

# Tema 2
# x = int(input("Digite um valor inteiro: "))
# if x % 2 == 0:
#     print("O valor é par")
# else:
#     print("o valor é impar")

# Tema 3
# x = True
# y = False
# print(not x)
# print(x and y)
# print(x or y)
#
# nota1 = float(input("Nota da primeira materia: "))
# nota2 = float(input("Nota da segunda materia: "))
# nota3 = float(input("Nota da terceira materia: "))
#
# if nota1 > 7 and nota2 > 7 and nota3 > 7:
#     print("aluno passou de ano")
# elif:
#     print("aluno reprovou de ano")

# Tema 4
precoB = 1.85
precoM = 2.30
precoL = 3.60
d = {
    1: {"nome": "Maçã", "preco": precoM},
    2: {"nome": "Laranja", "preco": precoL},
    3: {"nome": "Banana", "preco": precoB}
}

print("_"*35)
print(" "*9 + "Frutas Disponiveis")
print("-"*35)
for chave, valor in d.items():
    print(f"{chave} - {valor['nome']}")
print("_"*35)

while True:
    fruta = int(input("Digite o numero da fruta: "))
    if fruta in d:
        break
    else:
        print("Escolha uma fruta valida")
        print("_" * 35)

qtd = int(input("Digite a quantidade: "))
print("-"*35)


def calcula_preco(qtd, valor):
    return qtd * valor


if 1 <= fruta <= 3:
    precoFinal = calcula_preco(qtd, d[fruta - 1]["preco"])
    print(f"Produto: {d[fruta]["nome"]}, Quantidade: {qtd}, Total: {precoFinal:.2f}")
else:
    print("Numero invalido")



