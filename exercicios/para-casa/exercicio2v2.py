#Este é um Programa para uma loja de tintas. O programa pede o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados.
#A tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços na seguinte situação:
#Misturar latas e galões, de forma que o desperdício de tinta seja menor. 
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

#Informações iniciais:
area = 1.1 * float(input("Qual a área a ser pintada? "))
areaPorLitro = 6
litroPorLata = 18
litroPorGalao = 3.6
precoPorLata = 80
precoPorGalao = 25

#Identificar o número máximo de latas a serem compradas. O que faltar, deverá ser comprado em galões.
litro = area / areaPorLitro
lata = litro / litroPorLata
restoLitroLata = litroPorLata - (litro % litroPorLata)
lataInt = litro // litroPorLata
restoLitroGalao = litroPorGalao - (restoLitroLata % litroPorGalao)

#Se o número de latas for não inteiro, testar se o resto é maior do que os litros da lata / litros do galão menos 1. 
if not isinstance(lata, int):
    if restoLitroGalao >= restoLitroLata:
        lata = lataInt + 1
        galao = 0
    else:
        lata = lataInt
        galao = ((litro - (lata * litroPorLata)) // litroPorGalao) + 1
else:
    galao = 0


#Cálculo do preço total de latas e galões.
preco = (lata * precoPorLata) + (galao * precoPorGalao)

print(f"Quantidade de lata: {lata}\nQuantidade de galão: {galao}")
print(f"O preço total é: R${preco:,.2f}")