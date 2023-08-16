#Questão 17, feito em grupo.

import math 

area = float(input("Digite o tamanho em metros quadrados de área a ser pintada: "))
litros = area / 6 ##pq 6, pq a cada 1 litros é 6m2
litrosComFolga = litros * 1.1 ##1.1 é a porcentagem de 10%

latas = int(litrosComFolga/18) ##uma lata tem 18 litros
resto = litrosComFolga % 18 ## a % é o resto 
galoes = math.ceil(resto/3.6) ##vai ser o resto pois ele é menor que a lata, pois como vai faltar na lata um "restinho para completar", usamos o resto aqui em baixo. 

preco = (latas * 80) + (galoes * 25)

print(f"Você ira utlizar {latas} latas e {galoes} galões de tinta")
print(f"O preço total é de R$ {preco:.2f}")







 