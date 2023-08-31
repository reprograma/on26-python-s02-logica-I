# Imagine que você é um professor e deve calcular a média dos alunos. 
# Para facilitar, você quer escrever um código que calcule as notas pra ti. Vamos criar uma função para isso.
# Mas em cada semestre, os pesos das notas são diferentes. 
# Para seus alunos do primeiro semestre, os pesos são iguais em todas as provas.
# Já no segundo semestre, a primeira prova vale 50% da nota, e a segunda e terceira valem somente 25%. 
# Já no terceiro semestre, a primeira prova vale somente 10%, a segunda vale 35% e a última 55%. 

# definindo a função
def calcula_media_ponderada(nota1, nota2, nota3, peso1, peso2, peso3):
    media = (nota1*peso1 + nota2*peso2 + nota3*peso3)/(peso1 + peso2 + peso3)
    return media

# definindo as variáveis
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
peso1, peso2, peso3 = float(input("Digite peso 1: ")), float(input("Digite peso 2: ")), float(input("Digite peso 3: "))     # maneira de encurtar o código

# chamando a função
media = calcula_media_ponderada(nota1, nota2, nota3, peso1, peso2, peso3)

print(media)