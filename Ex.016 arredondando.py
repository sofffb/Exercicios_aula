# ler um número e arredondar para cima
from math import trunc
num = float(input('Digite um número: '))
print(f'O número que você digitou foi: {num}, sua porção inteira é {(trunc(num))}')
