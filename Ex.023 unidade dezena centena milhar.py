# Programa que leia um número entre 0 à 9999 e mostre na tela cada um dos dígitos separados:
# tente fazer como uma STRING e MATEMATICAMENTE

num = int(input('Digite um número qualquer entre 0 à 9999 ->  '))

# Matematicamente, ao invés de transformar em string:
# unidade = num dividão inteira por 1 o resto da divisão - ou módulo- por 10
u = num // 1 % 10
print(f'Unidade: {u}')

d = num // 10 % 10
print(f'Dezena: {d}')

c = num // 100 %10
print(f'Centena: {c}')

m = num // 1000 % 10
print(f'Milhar: {m}')

