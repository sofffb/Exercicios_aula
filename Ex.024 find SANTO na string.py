# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "SANTO"

cidade = str(input('Digite aqui o nome da sua cidade: ')) .strip()

cid = cidade.capitalize()
divida = cid.split()
separado = (divida[0])
print(divida)
print('A primeira palavra da cidade começa com "Santo"?: ')
print('Santo' in separado)