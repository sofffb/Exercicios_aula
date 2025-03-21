# Programa que leia algo e mostre seu tipo primitivo e todas as infomações
x = input('Digite algo:  ')

classe = ( type(x))
print (f' O tipo primitivo de {x} é:  {classe}')
espaço = (x.isspace())
print (f'{x} contém apenas espaços? {espaço}')
numérico =  (x.isnumeric())
print (f'{x} Contém apenas números? {numérico}')
maiúsculo =  (x.isupper())
print (f' {x} Contém apenas letras maiúsculas? {maiúsculo}')
