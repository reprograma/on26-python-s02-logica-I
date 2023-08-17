print("Olá! Gostaria de calcular a quantidade de latas de tinta e o valor total? Você veio ao lugar certo!")

metragem = float(input("Insira a área a ser pintada em metros quadrados aqui: "))
litragem = metragem / 3
qLatas = litragem / 18
qLatasD = (litragem//18)+1
vT = qLatas * 80
vTD = (qLatasD)*80

if (metragem%54 == 0 and litragem//18 >=1):
    print("A quantidade de latas necessária é", qLatas, ". O valor da compra será de R$", vT)
else:
    print("A quantidade de latas necessária é", qLatasD, ". O valor da compra será de R$", vTD)
