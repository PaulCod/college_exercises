# inicio = int(input("Digite o valor inicial: "))
# fim = int(input("Digite o valor final: "))
#
# valor = inicio
# if valor > fim:
#     while valor > fim:
#         if valor % 2 == 0:
#             print(valor)
#         valor -= 1
# else:
#     while valor <= fim:
#         if valor % 2 == 0:
#             print(valor)
#         valor += 1

## 2

# soma = 0.0
# count = 1
#
# while count <= 5:
#     nota = float(input(f"Digite {count}° nota: "))
#     if nota > 10 or nota < 0:
#         print("Digite uma nota valida")
#         continue
#     soma += nota
#     count += 1
#
# media = soma / 5
# if media > 7:
#     print(f"Media: {media} Aluno passou")
# else:
#     print(f"Media: {media} Aluno reprovou")

## 3
# while True:
#     valor = int(input("Digite um valor inteiro: "))
#     if valor <= 0:
#         print("Valor deve ser maior que zero")
#         continue
#
#     print(f"Valor digitado foi {valor}, encerrando o programa")
#     break


## 4

# nome = ""
# while not nome:
#     nome = input("Digite um nome: ")
#

## 5
# somador = 0
# count = 0
# for i in range(1, 101, 1):
#     if (i % 2 ==0):
#         somador += i
#         count += 1
#     continue
#
# print(somador/count)

## 6
for i in range(1, 11):
    print("#" * 10)
    print(f"TABOADA DO {i}")
    for f in range(1, 11):
        print(f"{i} X {f} = {i * f}")
