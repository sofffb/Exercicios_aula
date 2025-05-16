# programa que pergunte a distância de uma viagem por Km:
# até 200km cobre R$ 0,50
# acima de 200km cobre R$ 0,45

print('Calcule o valor da sua viagem:')
print('''Valor cobrado por Kilômetro:
Até 200km será cobrado R$ 0,50 e acima disso R$ 0,45''')

d = int(input('Digite a distância do percurso: '))

if d > 200:
    km = d * 0.50
    print(f' Acima de 200km de distância. Valor a ser pago: {km:.2f} ')

else:
    km2 = d * 0.45
    print(f' Abaixo de 200km. Valor a ser pago: {km2:.2f}')
