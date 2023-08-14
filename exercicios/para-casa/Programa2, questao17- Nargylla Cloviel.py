# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
#que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Raciocínio = uma lata de tinta(18L) cobre uma área de 108m²(18x6), um galão de tinta cobre uma área de 21,6m²(6x3,6). Primeiro, precisaremos
# dividir a area por 6, para descobrir a quantidade de litros. Depois, precisaremos dividir esses litros necessários por 18(1 Lata) e por 3,6(galão).
# para descobrir a quantidade de latas e de galões. Após isso, precisaremos calcular o preço final, sendo o de lata (quantidade de latas x 80,0) 
# e o de galões (quantidade de galoes x 25,00). Para calcular o suficiente, precisaremos dividir a quantidade de litros por 18 e depois dividir
# o resto dessa conta por 3,6.

lata_litro = 18
galao_litro = 3.6
preco_lata = 80
preco_galao = 25
metro_por_litro = 6

saudacao = print("Olá, cliente! Boas vindas a loja Cores e Colorir! Como podemos lhe chamar?")
nome = input()
apresentacao = print("Olá, "+nome + "!"+  " Para começarmos, por favor, informe o tamanho da área, em metros quadrados ")
area = float(input("insira o tamanho em m² "))

especificacao = print("Você prefere que a quantidade seja dada apenas em galões, apenas em latas ou a mistura dos dois?")
escolha_info = print("Se sua preferencia for apenas galões, digite: galão. Se for apenas em latas, digite: lata. Se for a mistura de ambos, digite: mistura")
escolha = input()

quant_litros = area/metro_por_litro

#calculando galão
quant_galao = quant_litros//galao_litro
preco_final_Galao = quant_galao*preco_galao

#calculando lata
quant_latas = quant_litros//lata_litro
preco_final_Lata = quant_latas*preco_lata

#calculando mistura
folga = int(quant_litros*10/100)
quant_certa_soma = quant_litros + folga
num_de_latas = quant_certa_soma//lata_litro
num_de_galão = (quant_certa_soma%lata_litro)//3.6
preco_mistura = (num_de_latas*preco_lata)+(num_de_galão*preco_galao)

#aplicando o conhecimento da oficina

if escolha == "galão":
    print("A quantidade de galões necessárias é: ")
    print(quant_galao)
    print("O preço correspondente a essa quantidade é: ")
    print(preco_final_Galao)

elif escolha == "lata":
    print("A quantidade de latas necessárias é: ")
    print(quant_latas)
    print("O preço correspodente a essa quantidade é: ")
    print(preco_final_Lata)

elif escolha == "mistura":
    print("a quantidade que você precisa de latas é:")
    print(num_de_latas)
    print("A quantidade que você precisa de galões é")
    print(num_de_galão)
    print("O preço final dessa compra será de")
    print(preco_mistura)
else:
    print("Desculpe, não consigo encontrar o que você digitou, verifique novamente!")

#Para o melhor funcionamento desse código, seria interessante que, após finalizar uma escolha, ter a opção de testar outra alternativa sem 
# passar por toda aquela introdução. Melhorias a serem aplicadas a medida que o conhecimento se expande!!



