#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
#que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

#Raciocínio = "Uma lata de tinta, contendo 18L, é capaz de cobrir uma área de 54m², já que 18x3 = 54, então 54/3=18. Para descobrirmos a quantidade de litros
#necessários, precisamos dividir a area informada por 3. Para sabermos a quantidade de lata, precisamos dividir esses litros necessários por 18
#que equivale a uma lata. E o preço vai ser a quantidade de lata x 80 reais.


metrosPorLitro = 3
litrosLata = 18
preco = 80
apresentacao = "Olá,! Boas vindas a loja Cores e Colorir, qual o seu nome?"
print(apresentacao)
nomeCliente = input()
apresentacao2 = print("Olá, " + nomeCliente + "! É um prazer receber você aqui, esperamos que tenha uma ótima experiência com nossos serviços!")
cont_apresentacao2 = print("Para iniciarmos, por favor, informe o tamanho da área a ser pintada em metros quadrados. ")
area = float(input("insira apenas o tamanho em m² "))

litros = (area/metrosPorLitro)
latas = int((litros//litrosLata))
precoFinal = preco*latas
print("A quantidade de latas necessárias é:") 
print(latas)
print("O preço final da sua compra em reais é:") 
print(precoFinal)
