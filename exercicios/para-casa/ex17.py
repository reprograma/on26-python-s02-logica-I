print("Seja bem-vindo(a) a Global Tintas")
area = int(input("Informe a tamanho em metros quadrados da área a ser pintada: "))

litros = int(area/6)
latas = int(litros/18)

if latas % 18 != 0:
    latas += 1
preco_l = latas*80

galoes = int(litros/3.6)
if galoes % 3.6 != 0:
    galoes += 1
preco_g = galoes*25

#compra de latas e galões
des_galoes = int((litros - (latas * 18)) / 3.6)

if litros - (latas * 18) % 3.6 != 0:
    des_galoes += 1
soma = ((latas * 80) + (des_galoes * 25))

print("A quantidade de latas de tintas necessárias são " + str(latas) + ", no valor de R$" + str(preco_l) + ".")
print("A quantidade de galões de tintas necessários são " + str(galoes) + ", no valor de R$" + str(preco_g) + ".")
print("A quantidade de latas e galões de tintas necessários, respectivamente, são " + str(latas) + " e " + str(des_galoes) + ", no valor de R$" + str(soma) + ".")