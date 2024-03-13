### Exercicio

## Exercicio de fixação

# a) Inteiros de 3 até, com 12 incluso
# for i in range(3, 13):
#     print(i)

# b) Inteiros de 0 até 9, excluindo 9, com passo de 2
# for i in range(0, 10, 2):
#     print(i)

## Problemas

# 1
#
# def verifica_sair(palavra):
#     if palavra.strip().lower() == "sair":
#         print("Saindo")
#         return True
#     return False
#
#
# lista = {"+": lambda x, y: x+y, "-": lambda x, y: x-y, "*": lambda x, y: x*y, "/": lambda x, y: x/y}
# print("Digite sair a qualquer momento para sair")
# while True:
#     valor = input("Digite um numero: ")
#     if verifica_sair(valor):
#         break
#     valor2 = input("Digite outro numero: ")
#     if verifica_sair(valor2):
#         break
#     op = input("Digite um operador (+, -, *, /): ")
#     if verifica_sair(op):
#         break
#
#     if not valor.isdigit() or not valor2.isdigit():
#         print("Digite um numero valido")
#         continue
#     elif op.strip() not in lista:
#         print("Digite um operador valido")
#         continue
#     else:
#         print(f"{valor} {op} {valor2} = {lista[op](int(valor), int(valor2))}")

## Exercicio 2

# def contar_cedulas(valor):
#     cedulas = [100, 50, 20, 10, 5, 1]
#     qtd_cedulas = {}
#     for cedula in cedulas:
#         qtd = valor // cedula
#         valor %= cedula
#         qtd_cedulas[cedula] = qtd
#
#     return qtd_cedulas
#
#
# valor = int(input("digite o valor a pagar: "))
#
# res = contar_cedulas(valor)
#
# print("Quantidade de cedulas necessarias: ")
# for cedula in sorted(res.keys(), reverse=True):
#     quantidade = res[cedula]
#     print(f"Cédulas de R$ {cedula}: {quantidade}")


## Exercicio 3

# pessoas = 0
# acumuladorIdade = 0
# totalArrecadado = 0
# while True:
#     idade = input("Digite a idade da pessoa: ")
#     if verifica_sair(idade):
#         break
#
#     pessoas += 1
#     idade = int(idade)
#     acumuladorIdade += idade
#
#     if idade < 3:
#         continue
#     if idade >= 3 and idade <= 12:
#         print(f"Preço R$15")
#         totalArrecadado += 15
#     if idade > 12:
#         print(f"Preço R$30")
#         totalArrecadado += 30
#
# print(f"Total de pessoas: {pessoas}, Total arrecadado R${totalArrecadado}, Media de idade: {acumuladorIdade / pessoas}")

# def parangaricu():
#    palavra1 = 'parangaricu'
#    tirimirruaro(palavra1)
#
#
# def tirimirruaro (palavra):
#    palavra2 = palavra + 'tirimirruaro'
#    print(palavra2)
#
#
# parangaricu()
# print(palavra2)

def div2 (num , den):
   res = num / den
   print(res)

div2(3, 10)
