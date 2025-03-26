nome = input('Digite seu nome: ')
print(f'Prazer em te conhecer {nome:<20}!!!!')
print (f'Prazer em te conhecer {nome:^20}!!!!')
print (f'Prazer em te conhecer {nome:*^20}!!!!')


# alinhar à direita, esquerda e centralizar
nome1 = 'flor'
print (f'{nome1:>6}')
print(f'{nome1:<6}')
print(f'{nome1:^10}')


texto = 'python'
# .ljust
print(texto.ljust(10,'-'))
# .rjust
print(texto.rjust(10,'&'))
# .center
print(texto.center(15,'*'))
