#Damaris Santos Teles Brito
"Resolução exercício 17 python"
"Casa de Tintas"

area = float(input("Entre com o tamanho da área (m²): "))

litros = (area / 6) * 1.1
latas = litros / 18

if latas % 18 != 0:
    latas += 1
preco = latas * 80

galoes = litros / 3.6
if galoes % 3.6 != 0:
    galoes += 1
preco2 = galoes * 25

# mistura de latas e galoes
mistura_lata = int(litros / 18.0)
mistura_galao = int((litros - (mistura_lata * 18)) / 3.6)

if (litros - (mistura_lata * 18) % 3.6 != 0):
    mistura_galao += 1
    total = (mistura_lata * 80) + (mistura_galao * 25)

print("Apenas latas de 18 litros: %d" % latas, "Valor R$: %d" % preco)
print("Apenas galões de 3.6 litros: %d" % galoes, "Valor R$: %d" % preco2)
print("Mix de latas e galões: %d latas e %d galoes = %.2f" % (
    mistura_lata, mistura_galao, ((mistura_lata * 80) + (mistura_galao * 25))))
