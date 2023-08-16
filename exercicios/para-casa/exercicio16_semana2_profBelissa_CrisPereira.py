# Semana 2 - prof Belissa curso Python - estudante Cris Pereira
# Exercicio 16 - Estrutura Sequencial
import math

def casaCor(area, rendimento, tam_recipiente):
    tinta_necessaria = area/rendimento
    qtde_recipientes = math.ceil(tinta_necessaria/tam_recipiente)
    return qtde_recipientes

tamanho_parede = float(input("Digite a área a ser pintada em m2: "))
rendimento = 3
tam_lata = 18
preco = 80
qtde_latas = casaCor(tamanho_parede, rendimento, tam_lata)

print("Você irá precisar de", qtde_latas,"latas para pintar", tamanho_parede,"de parede. O preço total é: R$",qtde_latas*preco)