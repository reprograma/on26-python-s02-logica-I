area = float(input("Qual a área a ser pintada? "))
areaPorLitro = 3
litroPorLata = 18
precoPorLata = 80

litro = area / areaPorLitro
lata = litro / litroPorLata

if not isinstance(lata, int):
    lata = (litro // litroPorLata) + 1
else:
    pass

preco = lata * precoPorLata

print(f"Aqui está o número de latas que você precisa comprar: {lata}")
print(f"O preço total é: R${preco:,.2f}")