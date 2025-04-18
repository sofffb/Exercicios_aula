# Programa que leia um número entre 0 à 9999 e mostre na tela cada um dos dígitos separados:
# tente fazer como uma STRING e MATEMATICAMENTE

num = int(input('Digite um número qualquer entre 0 à 9999 ->  '))
# transformando número em texto
n = str(num)
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')

