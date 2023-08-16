#LOJA DE TINTAS:

tamanho = float(input("QUANTOS METROS QUADRADOS TEM A ÁREA A SER PINTADA? "))

metroQuadradoPorLitro = 3

litrosNecessarios = tamanho / metroQuadradoPorLitro

lataLitros = 18
lataPreco = 80

latasNecessarias = litrosNecessarios / lataLitros
precoNecessario = lataPreco * latasNecessarias

print("Latas necessárias abaixo.")
print(int(latasNecessarias))
print("Preço necessário abaixo.")
print(float(precoNecessario))
