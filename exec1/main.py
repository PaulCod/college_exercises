# Exercicios Algebricos

# a) O somatório dos 5 primeiros números inteiros e positivos
# print(1+2+3+4+5)

# b) A média entre 23, 19 e 31
# print("A media é {:.2f}".format((23+19+31)/3))

# c) O número de vezes que 73 cabe em 403
# print(403//73)

# d) A sobra quando 403 é dividido por 73
# print(403%7)

# e) 2 elevado à 10ª potência
# print(2**10)

# f) O valor absoluto da diferença entre 54 e 57
# diff_abs = abs(57 - 54)
# print(diff_abs)

# g) O menor valor entre 34, 29 e 31
# print(min(34, 29, 31))

# Exercicios Atribuição

# a) Atribuir o valor inteiro 3 à variável a
# a = 3

# b) Atribuir o valor 4 à variável b
# b = 4

# c) Atribuir à variável c o valor da expressão a*a + b *b
# c = a*a + b*b
# print(c)

# Exercicios String
# s1 = 'ant'
# s2 = 'bat'
# s3 = "cod"

# a) ‘ant bat cod’
# print( "{} {} {}".format(s1, s2, s3))

# b) ‘ant ant ant ant ant ant ant ant ant ant’
# print("{} ".format(s1)*10)

# c) ‘ant bat bat cod cod cod’
# print("{}".format(s1), "{} ".format(s2)*2, "{} ".format(s3)*3)
# d) ‘ant bat ant bat ant bat ant bat ant bat ant bat ant bat ‘
# print(7 * (s1 + " " + s2 + " "))
# e) ‘batbatcod batbatcod batbatcod batbatcod batbatcod ’
# print(5 * (s2*2 + s3 + " "))

# Problemas
# price = float(input("Preco do produto: "))
# percent = float(input("Percentual de desconto (0-100)%: "))
#
# if percent < 0 or percent > 100:
#     print("Percentual deve ser maior ou igual a 0 e menor ou igual a 100")
# else:
#     discountPrice = price - (percent * price) / 100
#     print("{}".format(discountPrice))

# segundo
# precoDia = 60.0
# precokm = 0.15
# kmPercorrido = int(input("KMs percorridos: "))
# diasAlugado = int(input("Dias alugados: "))
#
# preco_total = (kmPercorrido * precokm) + (diasAlugado * precoDia)
#
# print("o total deu R${}".format(preco_total))

# terceiro
# frase = input("Digite uma frase: ")
# tamanho_frase = len(frase)
# metade_frase = frase[:tamanho_frase // 2]
#
# # Imprimindo os dois últimos caracteres da segunda variável
# dois_ultimos_caracteres = metade_frase[-2:]
# print("Os dois últimos caracteres da segunda variável são:", dois_ultimos_caracteres)