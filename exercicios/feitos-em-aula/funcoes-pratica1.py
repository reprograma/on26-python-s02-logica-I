# Vamos pensar num exemplo. Imagine que você é um professor 
# e deve calcular a média das notas dos alunos em três provas. 
# Para facilitar, você quer escrever um código que calcule as 
# notas pra ti. Vamos criar uma função para isso e nós só 
# precisamos chamar essa função com as notas dos alunos! 

# solução sem utilização de função:

nota1 = float(input("Digite a nota 1: "))   # como a entrada do input é sempre uma string é necessário realizar a conversão para número
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3)/3
print(media)

# solução utilizando função:

# definindo as variáveis
nota1 = 8   
nota2 = 7
nota3 = 9.5

# definindo a função
def calcula_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media

# chamando a função
print(calcula_media(nota1, nota2, nota3))