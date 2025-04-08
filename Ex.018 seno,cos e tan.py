# programa que leia um ângulo qualquer e mostre o seno, cosseno e tangente
from math import radians, sin, cos, tan

n = int(input('Quantos graus tem o ângulo?: '))

s = sin(radians(n))
c = cos(radians(n))
t = tan(radians(n))

print(f'O valor de SENO: {s:.2f}, COSSENO: {c:.2f} e TANGENTE: {t:.2f}')
