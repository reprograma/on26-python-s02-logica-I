def calcula_media_poderada(nota1, nota2, nota3, peso1, peso2, peso3):
    media = (nota1*peso1 + nota2*peso2 + nota3*peso3)/(peso1+peso2+peso3)
    return media

nota1 = 15
nota2 = 98
nota3 = 19 
peso1, peso2, peso3 =  float(input("peso1: ")), float(input("peso2: ")), float(input("peso3: "))

print(calcula_media_poderada(nota1, nota2, nota3, peso1, peso2, peso3))
