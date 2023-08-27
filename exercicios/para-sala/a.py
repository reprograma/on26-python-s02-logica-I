#Vamos pensar num excemplo.
#Imagine que você é um professor e deve calcular a média das notas dos alunos



def calcular_media(n1, n2):
    media_da_aluna = (n1 + n2)/2
    return media_da_aluna


nota1 = 10
nota2 = 9

media_da_aluna = (calcular_media(nota1, nota2))
print(media_da_aluna)

media_de_aprovação = 5
media_de_recuperação = 3

if type(media_da_aluna) == float:
    media_da_aluna = round(media_da_aluna)

    
if media_da_aluna >= media_de_aprovação:
    print("aprovação")
elif media_da_aluna >= media_de_recuperação:
    print("recuperação")   
else: 
    print("Reprovada")

    print("fim do programa")

