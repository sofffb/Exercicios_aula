# Programa que leia o nome de uma pessoa e mostre:
import emoji
print(emoji.emojize(':beaming_face_with_smiling_eyes:'))
nome = input(str('Ola! Digite o seu nome: '))

# O nome com todas as letras em MAIÚSCULO:
print('  -> O nome todo em letras maiúsculas fica:')
print(nome.upper())
# O nome com todas as letras em MINÚSCULO:
print('  -> O nome todo em letras minúsculas fica:')
print(nome.lower())

# Quantas letras ao total:
print('  -> Quantos caracteres tem neste nome: ')
print(len(nome))
# Quantas letras ao total SEM CONSIDERAR ESPAÇOS:
nomesemespaco = nome.replace(' ', '')
print('  -> O nome sem espaçamentos: ')
print(nomesemespaco)

print('  -> Quantos caracteres tem o nome, sem contar os espaços:')
print(len(nomesemespaco))

print('''  -> Para conseguir contabilizar os caracteres, primeiro divido para usar a função len 
- Nome dividido: ''')
nomediv = nome.split()
print(nomediv)

print('  -> Quantas letras tem o primeiro nome e o segundo nome, respectivamente:')
print(len(nomediv[0]))
print(len(nomediv[1]))

print('  -> Mostre o primeiro nome e segundo nome separadamente:')
print(nomediv[0])
print(nomediv[1])

nomecasada = input('  -> Digite o sobrenome de casado(a): ')

# incluir  na lista
print('  -> Adicionando o sobrenome:')
nomediv.append(nomecasada)
print(nomediv)

# remover da lista - em standby
print('  -> Removendo o sobrenome:')
nomediv.pop(2)
print(nomediv)
print('  ')
print(' Fim do programa! ')
print(emoji.emojize(':beaming_face_with_smiling_eyes:'))