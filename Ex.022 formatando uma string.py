# Programa que leia o nome de uma pessoa e mostre:
import emoji
print(emoji.emojize(':beaming_face_with_smiling_eyes:'))
nome = input(str( '  \n  Ola! Digite somente seu primeiro nome: '))

# O nome com todas as letras em MAIÚSCULO:

print(' \n -> O nome todo em letras maiúsculas fica:')
print(nome.upper() , ' \n ')

# O nome com todas as letras em MINÚSCULO:
print('  -> O nome todo em letras minúsculas fica:')
print(nome.lower() , ' \n ')

# Quantas letras ao total:
print('  -> Quantos caracteres tem neste nome: ')
print(len(nome) , ' \n ')

# Quantas letras ao total SEM CONSIDERAR ESPAÇOS:
nomesemespaco = nome.replace(' ', '')
print('  -> O nome sem espaçamentos: ')
print(nomesemespaco , ' \n ')

print('  -> Quantos caracteres tem o nome, sem contar os espaços:')
print(len(nomesemespaco) , ' \n ')

print('''  -> Para conseguir contabilizar os caracteres, primeiro divido para usar a função len 
- Nome dividido: ''')
nomediv = nome.split()
print(nomediv)

print('  \n  -> Quantas letras tem o primeiro nome e o segundo nome, respectivamente:')
print(len(nomediv[0]))
print(len(nomediv[1]))

print('  \n  -> Mostre o primeiro nome e segundo nome separadamente:')
print(nomediv[0])
print(nomediv[1])

nomecasada = input(str('  \n  -> Digite o sobrenome de casado(a): '))


# incluir  na lista

print('  \n  -> Adicionando o sobrenome:')
nomediv.append(nomecasada)
print(nomediv , ' \n ')

# remover da lista - em standby
print('  -> Removendo o sobrenome:')
nomediv.pop(2)
print(nomediv , ' \n ')

print(' Fim do programa! ')
print(emoji.emojize(':beaming_face_with_smiling_eyes:'))