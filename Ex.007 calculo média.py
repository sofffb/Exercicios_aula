# Programa que leia duas notas e calcule a média

print('Olá! Calcule sua média: ')
nome = (input('Digite seu nome: '))
n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))
s = n1 + n2
print (f' {nome}, Sua média é -> {s / 2 :.1f}')
