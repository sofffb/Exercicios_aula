# prog que leia o salário com aumento de 15%

salario = float(input('Digite o valor do seu salário: R$ '))
novosal = salario + (salario * 15 / 100)

print(f'Seu salário com um aumento de 15% ficou: R${novosal:.2f}')