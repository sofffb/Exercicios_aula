# Calcule o valor a ser pago após o aluguel
d = int(input('Quantos dias foi o aluguel?: '))
km = float(input('Quantos kilômetros foram rodados?:'))

print('Sabendo que -> Valor diária: R$ 60,00 e R$ 0,15 por km rodado')

pagar = (d * 60) + (km * 0.15)
print(f'Valor total: R$ {pagar}')
