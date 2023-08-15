ter o hábito de usar o git, para ter um histórico de todos os códigos;
-  anotações sobre o caminho: abrir o vscode > na aba esquerda lá em cima, clica no 'File' > para criar um novo arquivo, voce clica no  'New File' > digita seu código >  após finalizar seu código você salva, para isso clica novamente no 'File' lá em cima no cantinho esquerdo, clica na opção 'Save' que irá aparecer no menu > vai abrir uma nova caixinha onde você vai colocar o nome do seu arquivo e no tipo seleciona o 'python'.
______________

<b>Slide</b>

#como descobrir o tipo va variavel
num_1 = -5
print(type(num_1))

num_2 = 1.5555
print(type(num_2))

#soma

soma = num_1 + num_2
print("Tipo da variável soma: ", type(soma))

#numero complexo

num_complexo = complex(1,-2)
print

#booleano

a = True
print(type(a))

b = False
print(type(b))

#strings

texto = "Hi, It's a text!"
print(texto)


######Parte_2
#variaveis

num_3 = 25
print(num_3)

num_4 = 2.5
print(num_4)

soma = num_3 + num_4
print(soma)

#input

entrada = input()

print("O valor digitado é: " + entrada)


#exercicio

num_1 = input()
num_2 = input()

concat = (num_1 + num_2)
print(concat)


#exponenciação

num_3 = 5
num_4 = 6

exp = pow(num_3, num_4)
print(exp)
exp_2 = num_4 ** num_3
print(exp_2)


# o piso eu quando fizemos uma divisão e no caso 17/3
o resultado dá 5,666
o piso ele semrpe arredonda para baixo então seria 5;
17//3
e o restante ele mostra o resto 
17%3

#concatenação

text_1 = "Oi, pessoal! "
text_2 = "tudo bem? "
text_3 = "O Reprograma é muito ..."

text_int = text_1 + text_2 + text_3

print(text_int)

# só pode concatenar no python duas strings. 

#identação

    #texto identado
        #texto identado 2
um tab tem o tamanho de 4 espaços;


# exercico:

#funções
# escrevemos funções para tentar não ter rescrita de código. 

def cal_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media

nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = cal_media(nota1, nota2, nota3)
print("a média é : ", media)


#def cal_media(nota1, nota2, nota3):
# ali estão os parametros 

def cal_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media

nota1 = 8.5
nota2 = 6.7
nota3 = 4.5

media = cal_media(nota1, nota2, nota3)
print("a média é : ", media)


#funções
# mudar os valores 

def cal_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media

nota1 = 8.5
nota2 = 6.7
nota3 = 4.5

media = cal_media(nota2=nota1, nota1=nota2, nota3)
print("a média é : ", media)



#funções
# passar um parametro que não é obrigatorio, 
#quando colocamos no nome e que se ele não tive um valor dele vai receber o valor 15

def cal_media(nota1, nota2, nota3=None):
    if not nota3:
        nota3 = 15
    media = (nota1 + nota2 + nota3)/3
    return media

nota1 = 8.5
nota2 = 6.7
nota3 = 4.5

media = cal_media(nota2=nota1, nota1=nota2)
print("a média é : ", media)


##exercicios 16 e 17

o exercicio 3 em função 
 
 metro_quadrado = float(input("Quantos metros quadrados tem a sua casa? "))
cobertura_tinta = metro_quadrado * 6
lata_de_tinta_litros = 18
valor_da_lata_tinta_reais = 80
galao_de_tintas_litros = 3.6
valor_galao_de_tinta_reais = 25

# Comprar apenas latas de 18 litros
quantidade_latas = int(cobertura_tinta / lata_de_tinta_litros)
if cobertura_tinta % lata_de_tinta_litros != 0:
    quantidade_latas += 1
preco_latas = quantidade_latas * valor_da_lata_tinta_reais
print(f"Você irá comprar {quantidade_latas} latas de tinta de 18 litros, e custará {preco_latas:.2f} reais.")

# Comprar apenas galões de 3,6 litros
quantidade_galoes = int(cobertura_tinta / galao_de_tintas_litros)
if cobertura_tinta % galao_de_tintas_litros != 0:
    quantidade_galoes += 1
preco_galoes = quantidade_galoes * valor_galao_de_tinta_reais
print(f"Você irá comprar {quantidade_galoes} galões de tinta de 3,6 litros, e custará {preco_galoes:.2f} reais.")

# Misturar latas e galões
quantidade_latas_mistura = int(cobertura_tinta / lata_de_tinta_litros)
quantidade_galoes_mistura = int((cobertura_tinta - quantidade_latas_mistura * lata_de_tinta_litros) / galao_de_tintas_litros)
if (cobertura_tinta - quantidade_latas_mistura * lata_de_tinta_litros) % galao_de_tintas_litros != 0:
    quantidade_galoes_mistura += 1
preco_mistura = (quantidade_latas_mistura * valor_da_lata_tinta_reais) + (quantidade_galoes_mistura * valor_galao_de_tinta_reais)
print(f"Você irá comprar {quantidade_latas_mistura} latas de 18 litros e {quantidade_galoes_mistura} galões de 3,6 litros, e custará {preco_mistura:.2f} reais.")
