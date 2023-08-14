#Damaris Santos Teles Brito
"Resolução exercício 16 python"
"Casa de tintas"

area = float(input("Digite a área do local (m²) ")) 
litros = area / 3
latas = int(litros / 18)
if litros % 18 != 0:
    latas += 1

print("Voce deverá comprar", latas , "latas.")
print("O valor total é: R$", latas * 80.0)
