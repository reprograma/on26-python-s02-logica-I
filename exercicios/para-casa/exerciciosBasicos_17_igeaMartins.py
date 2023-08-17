print("Olá! Gostaria de calcular a quantidade de latas de tinta e o valor total? Você veio ao lugar certo!")

metragem = float(input("Insira a área a ser pintada em metros quadrados aqui: "))
litragem = int((metragem + 0.1 * metragem)/6+1)

#if
qLatas = int((litragem/18)+1)
vTL = qLatas * 80

#elif1
qGaloes = int((litragem/3.6)+1)
vTG = qGaloes * 25

#elif3
qLatas2 = #dúvida mortal
qGaloes2 = #dúvida mortal
vTLG = (qLatas2 * 80) + (qGaloes2 * 25)

if (metragem % 97.2 == 0):
    print("Você vai precisar de", qLatas, "latas e o valor da compra será de R$", vTL)
elif (metragem % 19.44 == 0):
    print("Você vai precisar de", (qGaloes), "galões e o valor da compra será de R$", vTG)
elif (metragem <= 19.44):
    print("Você vai precisar de 1 galão e o valor da compra será de R$ 25.0")
elif (litragem - (qLatas2 * 18) % 3.6 != 0):
    #dúvida mortal
    print("Vamos economizar! Você precisa de", qLatas2, "latas e", qGaloes2, "galoes, vai custar R$" (vTLG)".")
else:
    print("erro")