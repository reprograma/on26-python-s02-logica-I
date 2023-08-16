# Semana 2 - prof Belissa curso Python - estudante Cris Pereira
# Exercicio 17 - Estrutura Sequencial
import math

def casaCor(area,rendimento,tam_recipiente1,tam_recipiente2=None):
        tinta_necessaria = area/rendimento + area/rendimento*0.1

        if not tam_recipiente2:
            qtde_compra = math.ceil(tinta_necessaria/tam_recipiente1)        
            return qtde_compra
        else:
            qtde_tinta_recipiente1 = math.ceil(tinta_necessaria/tam_recipiente1)
            qtde_tinta_recipiente2 = math.ceil(tinta_necessaria/tam_recipiente2)
            sobra_recipiente1 = qtde_tinta_recipiente1*tam_recipiente1 - tinta_necessaria 
            sobra_recipiente2 = qtde_tinta_recipiente2*tam_recipiente2 - tinta_necessaria
            qtde_compra1 = 0
            qtde_compra2 = 0

            if sobra_recipiente1 == sobra_recipiente2:
                if tam_recipiente1 > tam_recipiente2:
                      qtde_compra1 = math.ceil(tinta_necessaria/tam_recipiente1)
                      qtde_compra2 = 0
                else:
                     qtde_compra2 = math.ceil(tinta_necessaria/tam_recipiente2)
                     qtde_compra1 = 0

            elif sobra_recipiente1 < sobra_recipiente2:
                if sobra_recipiente1 == 0:
                     qtde_compra1 = math.ceil(tinta_necessaria/tam_recipiente1)
                
                elif tam_recipiente1 < tam_recipiente2:
                     relacao_recipientes = tam_recipiente2 // tam_recipiente1
                     if relacao_recipientes >= 1:
                          qtde_compra2 = math.ceil(qtde_compra1/relacao_recipientes)
                          qtde_tinta_faltante = tinta_necessaria - (qtde_compra2*tam_recipiente2)
                          qtde_compra1 = math.ceil(qtde_tinta_faltante/tam_recipiente1)
                        
            else:
                if sobra_recipiente2 == 0:
                    qtde_compra2 = math.ceil(tinta_necessaria/tam_recipiente2)

                elif tam_recipiente2 < tam_recipiente1:
                     relacao_recipientes = tam_recipiente1 // tam_recipiente2 #verificar essa linha depois, acho que pode dar xabu
                     if relacao_recipientes >= 1:
                        qtde_compra1 = qtde_compra2 // relacao_recipientes
                        qtde_tinta_faltante = tinta_necessaria - (qtde_compra1*tam_recipiente1)
                        qtde_compra2 = math.ceil(qtde_tinta_faltante/tam_recipiente2)
                                                
            return [qtde_compra1, qtde_compra2]                 

tamanho_parede = float(input("Digite a área a ser pintada em m2: "))
rendimento = 6
tam_latas = 18
preco_latas = 80
tam_galoes = 3.6
preco_galoes = 25

print("Para pintar",tamanho_parede,"m2 você pode:")
print("Comprar", casaCor(tamanho_parede,rendimento,tam_latas), "latas e o valor a ser pago será: R$", casaCor(tamanho_parede,rendimento,tam_latas)*preco_latas)
print("Comprar", casaCor(tamanho_parede,rendimento,tam_galoes), "galões e o valor a ser pago será: R$", casaCor(tamanho_parede,rendimento,tam_galoes)*preco_galoes)

qtde_eficiente_latas, qtde_eficiente_galoes = casaCor(tamanho_parede,rendimento,tam_latas,tam_galoes) 
print("Para menor desperdício de tinta, compre",qtde_eficiente_latas,"latas e",qtde_eficiente_galoes,"galões")
print("O valor total do orçamento com menor desperdício de tinta é: R$",qtde_eficiente_latas*preco_latas+qtde_eficiente_galoes*preco_galoes)