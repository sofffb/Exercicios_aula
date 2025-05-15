# Programa que leia o nome completo de uma pessoa, mostrando o nome separadamente

nomecompleto = input('Digite seu nome e sobrenome: ')
divisao = nomecompleto.split()

print(f'Seu nome é: ' , divisao[0])
print(f'E o seu sobrenome é: ' , divisao[-1] )