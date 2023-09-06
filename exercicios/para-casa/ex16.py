print("Seja bem-vindo(a) a Global Tintas")
area = int(input("Informe a tamanho em metros quadrados da área a ser pintada: "))

litros = area/3
latas = int(litros/18)
if litros % 18 != 0:
    latas +=1

print("A quantidade de latas de tintas necessárias são " + str(latas) + ", no valor de R$" + str(latas*80) + ".")
