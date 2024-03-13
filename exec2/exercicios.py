### Exercicios
import calendar

## Expreções booleanas

# a) O Somatório de 2 com 2 é menor do que 4
# print( 2 + 2 < 4)

# b) O valor 7 // 3 é igual a 1+1
# print( 7 // 3 == 1+1)

# c) A soma de 3 elevado ao quadrado com 4 elevado ao qudrado é igual a 25
# print(3**2 + 4**2 == 25)

# d) A soma de 2, 4, 6 é maior do que 12
# print( 2 + 4 + 6 > 12)

# e) 1387 é divisivel por 19
# print(1387 % 19 == 0)

# b) 31 é par
# print(31 % 2 == 0)

# c) O menor valor entre: 34, 29, 31 é menor do que 30
# print(min(34, 29, 31) < 30)

## Condicionais simples

# a) Se idade é maior que 60, escreva: "Vocẽ tem direitos aos beneficios"
# idade = 70
# if idade > 60:
#     print("Vocẽ tem direitos aos beneficios")

# b) Se dano é maior do que 10 e escudo é igual a 0, escrever: "Vocẽ está morto"
# dano = 11
# escudo = 0
# if dano > 10 and escudo == 0:
#     print("Voce esta morto")

# c) Se pelo menos uma das variaveis booleanas norte, sul, leste e oeste resultarem
# em True, escreva: "Você escapou!"
# norte = False
# sul = False
# oeste = True
# leste = False
# if norte or leste or oeste or sul:
#     print("Você escapou")

## Codicionais Compostas

# a) Se ano é divisivel por 4, escreva: "Poder ser um ano bissexto". Caso contrário
# escreva: "Definitivamente não é um ano bissexto"

# if calendar.isleap(2024):
#     print("Ano pode ser bissexto")
# else:
#     print("Definitivamente não é um ano bissexto")

# b) Se ambas as variaveis cima e baixo forem True, escreva: "Decida-se",
# Caso contrario, escreva: "Você escolheu um caminho"
# cima = True
# baixo = False
# if cima and baixo:
#     print("Decida-se!")
# else:
#     print("Você escolheu um caminho!")


### Exercicios reais

# 1
# while True:
#     lado_1 = int(input("Digite o valor do primeiro lado do triangulo: "))
#     lado_2 = int(input("Digite o valor do segundo lado do triangulo: "))
#     lado_3 = int(input("Digite o valor do terceiro lado do triangulo: "))
#
#     if min(lado_1, lado_2, lado_3) == 0:
#         print("Nenhum lado pode ser igual a 0")
#         continue

#     if lado_1 >= lado_2 + lado_3 or lado_2 >= lado_1 + lado_3 or lado_3 >= lado_1 + lado_2:
#         print("Um lado não pode ser maior que a soma dos outros dois lados")
#         continue

#     if lado_1 == lado_3 == lado_2:
#         print("O trianglo é um Equilátero")
#         break
#     elif lado_1 == lado_2 or lado_1 == lado_3 or lado_3 == lado_2:
#         print("o tringulo é um Isósceles")
#         break
#     else:
#         print("O triangulo é um Escaleno")
#         break

# 2
# operacoes = {"+": lambda x, y: x+y, "-": lambda x, y: x-y, "*": lambda x, y: x*y, "/": lambda x, y: x/y, "**": lambda x, y: x**y}
# while True:
#     numero = int(input("Digite um valor numerico inteiro: "))
#     numero2 = int(input("Digite um segundo valor numerico inteiro: "))
#     op = input("Digite a operação que deseja realizar (+, -, *, /, **): ")
#     op = op.strip()
#     if op not in operacoes:
#         print("Operação invalida")
#         continue
#
#     print(operacoes[op](numero, numero2))
#     break

# 3

# inst = {
#     "R": lambda kw: kw * 0.40 if kw <= 500 else kw * 0.65,
#     "C": lambda kw: kw * 0.55 if kw <= 1000 else kw * 0.60,
#     "I": lambda kw: kw * 0.55 if kw <= 5000 else kw * 0.60
# }

# while True:
#     kwh = int(input("Quantidade de kWh consumida: "))
#     instalaca = input("Digite o tipo de instalação R(Residencial), I(Industrial) e C(Comercial): ")
#     instalaca = instalaca.upper()
#
#     if instalaca not in inst:
#         print("Escolha um tipo de instalação valida")
#         continue
#     elif kwh < 0:
#         print("O kWh não pode ser negativo!")
#         continue
#     else:
#         print(f"O preco a pagar é de {inst[instalaca](kwh)}")
#         break
