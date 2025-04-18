# Programa que leia um número entre 0 à 9999 e mostre na tela cada um dos dígitos separados:
# tente fazer como uma STRING e MATEMATICAMENTE

num = str(input('Digite um número qualquer entre 0 à 9999 ->  '))

print(f'Unidade: {num[3]}')
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')
print(f'Milhar: {num[0]}')

