# programa que leia o valor de um produto e mostre um desconto de 5%
prod = float(input('Digite o valor do produto: R$'))
np = prod - (prod * 5 / 100)
print(f'O seu novo preço é de R$ {np}')
