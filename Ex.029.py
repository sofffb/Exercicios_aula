 # programa que leia a velocidade de um carro: Acima de 80km/h foi multado - valor da multa: R$ 7,00 por cada km acima do limite
print('Você recebeu uma multa? veja: ')
v = int(input('Digite a velocidade do veículo: '))
print(f' A velocidade foi de {v} km/h.')

if v > 80:
    print(' -> A multa custa R$7,00 por cada km acima do limite.')
    excesso = v - 80
    total = excesso * 7
    print(f' O valor a ser pago pela multa é de: R${total}')
else:
    print('Você está dentro do limite. Nenhuma multa será aplicada.')
