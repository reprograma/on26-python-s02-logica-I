metros = float(input("Quantos metros quadrados deseja pintar?", ))

latas = (metros)/54


def verificar_numero(numero):
    if numero % 1 == 0:
        print("Você irá utilizar:", int(numero), "latas e pagará R$", int(numero)*80,".")
    else:
        print("Você irá utilizar:", int(numero) + 1, "latas e pagará R$", (int(numero)+1)*80,".")

numero = float(latas)
verificar_numero(numero)

