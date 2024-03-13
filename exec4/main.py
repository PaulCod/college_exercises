# tes = "tes"
#
# def contorno(palavra):
#     print("+" + "-"*len(palavra) + "+")
#     print(f"|{palavra}|")
#     print("+" + "-"*len(palavra) + "+")
#     print(tes)
#
#
# palavra = input("digite uma palavra: ")
# contorno(palavra)

# 2


# def valida_string(pergunta, min, max):
#     s1 = ""
#     tam = 0
#     while ((tam < min) or (tam > max)):
#         s1 = input(pergunta)
#         tam = len(s1)
#     return s1
#
#
# x = valida_string("Digite uma string: ", 10, 20)
# print(f"Voce digitou a string: {x} \nDado Valido, ecerrando o programa...")

while True:
    try:
        x = int(input("Por favor digite um numero: "))
        break
    except ValueError:
        print("Numero invalido")
    except:
        print("Algo deu errrado")
    # finally:
    #     print("Final do Programa")

