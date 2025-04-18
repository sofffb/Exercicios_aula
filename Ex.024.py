# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "SANTO"

cidade = input('Digite aqui o nome da sua cidade: ')
divida = cidade.split()
print(divida)
separado = (divida[0])
print('A primeira palavra da cidade começa com "Santo"?: ')
print('Santo' in separado)