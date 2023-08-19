
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



