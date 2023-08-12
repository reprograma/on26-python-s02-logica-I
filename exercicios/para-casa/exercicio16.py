#Se 1 litro pinta 3 metros quadrados, então uma lata com 18litros vai pintar  54. 
# Logo, a cada x metros quadrados, você divide por 54. Por exemplo, se você tem 108 metros 
# quadrados, você vai dividir por 54, que dá 2, então você precisa de duas latas de tintas!
# Se você tiver 120, quando dividido por 54, 
# da aproximadamente 2,22 , então você vai precisar de 3 latas, já que 2 não será suficiente

print(" digite o tamanho da parede em m² a ser pintada")
litro = 3
lata = 18 * 3
tamanho = (float(input()) ) / lata
valor_lata = 80

quant_latas_comprar = ( (tamanho * litro) // 3) + 1

print( "A quantidade de latas para comprar é de:" , quant_latas_comprar)

valor_compra = quant_latas_comprar * valor_lata

print( "O valor a ser pago é de: $", valor_compra)

