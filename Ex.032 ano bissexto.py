# Programa que leia se um ano é bissexto:
# Um ano é BISSEXTO quando é divisível por 4 ou 400
# quando for divisível por 100, não é BISSEXTO

print('Vamos descobrir se um ano é BISSEXTO?')
ano = int(input('Vamos lá! Digite um ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f' O ano {ano} é BISSEXTO.')
else:
    print(f' O ano {ano} NÃO É BISSEXTO.')
