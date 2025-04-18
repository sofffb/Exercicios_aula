# Faça um programa que leia uma frase pelo teclado e mostre:

frase = input('Digite aqui uma frase: ')
primeira = frase.find('a')
primeira2 = frase.find('A')
ultima = frase.rfind('a')
ultima2 = frase.rfind('A')

print('Quantas vezes aparece a letra "A" nessa string?:\n ')

print(frase.count('A') + frase.count('a') , '\n ')

print('Em que posição ela aparece pela primeira vez?:\n ')

if 'a' in frase:
    print(f'A primeira letra aparece no índice: {primeira}\n ')
elif 'A' in frase:
    print(f'A primeira letra aparece no índice: {primeira2} \n')
else:
    print(f'Não tem "A" / "a" na frase: {frase}')

print('Em que posição ela aparece pela última vez?: \n ')

if 'a' in frase:
    print(f'a última letra  aparece no índice: {ultima} \n ')
elif 'A' in frase:
    print(f'A última letra aparece no índice: {ultima2} \n ')

import emoji
print( 'Fim do exercício' , emoji.emojize(':thumbs_up:'))