# programa que leia o cateto oposto e o adjacente e mostre a hipotenusa

import math
n1 = float(input('Digite o valor do cateto oposto: '))
n2 = float(input('Digite o valor do cateto adjacente: '))
h = math.hypot(n1, n2)
print(f'A hipotenusa é {h:.2f}')
