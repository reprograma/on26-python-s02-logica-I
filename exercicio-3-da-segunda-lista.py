def soma_plantas_com_flores(orquideas, rosas, margaridas):
    resultado = orquideas + rosas + margaridas
    return resultado

# Solicitando ao usuário três números
orquideas = int(input("Digite a quantidade de orquideas: "))
rosas = int(input("Digite a quantidade de rosas: "))
margaridas = int(input("Digite a quantidade de margaridas: "))

# Chamando a função e imprimindo o resultado
soma = soma_plantas_com_flores(orquideas, rosas, margaridas)
print(f"Há: {soma} plantas com flores na sua loja")

