print('  ')
print(' * Aula 09 - Prática de manipulação de texto')

print('  ')
# FATIAMENTO DE TEXTO

print(' * Fatiamento do texto a seguir:')
print('  ')

frase = 'Curso em Vídeo Python'
print (frase)
print('  ')

print (' → A quarta letra da frase é:')
print (frase[3])
print('  ')

print (' → Fatiamento da quarta letra até a décima terceira:')
print (frase[3:13])
print('  ')

print (' → Fatiamento do início do texto até o 13 caractere:')
print (frase[:13])
print('  ')

print(' → Fatiamento da décima terceira letra até o final da string:')
print(frase[13:])
print('  ')

print(' → Fatiamento da 1 até 15 letra:')
print(frase[1:15])
print('  ')

print(' → Leia a frase pulando de duas em duas letras:')
print(frase[::2])
print('  ')

print(' * Print em texto longo:')

print('''Python é uma linguagem de programação usada para criar apps,
sites, ciência de dados, análise de dados e
automação de tarefas e muito mais.
É uma linguagem de alto nível, com sentaxe simples e legível.
Pode ser executada em várias plataformas, como Linux, Mac, e Microsoft.
É uma boa escolha para quem está iniciando na programação.''')

print('  ')

print(' * FUNÇÕES:')
print('  ')

#Análise len(frase) -> comprimento da frase -> 21 caracteres
print(' → Quantos caracteres tem na string?:')
print (len(frase))
print('  ')

# frase.count('o') -> vai me dizer quantas letras 'o' aparecem na frase
print(' → Quantas vezes a letra "V" aparece na string?:')
print((frase.count('V')))
print('  ')

# buscar uma palavra dentro de um texto, como não tem, ele me retorna '-1'
print(' → Busque palavra "android" nesse texto:')
print(frase.find('android'))
print('  ')

# por exemplo, ele vai me dar um TRUE or FALSE por causa do operador: 'in'
print(' → Existe a palavra "android" nesse texto?:')
print('curso' in frase)
print('  ')

print('Transformando a frase em letras maiúsculas e procure uma letra "O" no texto:')
print(frase.upper().count('O'))
print('  ')

print(' * TRANSFORMAÇÃO:')
print('  ')

print(' → Substituição:')
print(frase.replace('Python', 'Android'))
print('  ')

print(' → Colocando todas as letras em maiúsculo:')
print(frase.upper())
print('  ')

print(' → Transformando todas as letras em minúsculo:')
print(frase.lower())
print('  ')

print(' → Deixando somente a primeira letra da frase em maiúsculo:')
print(frase.capitalize())
print('  ')

# para Deixar somente a primeira letra de cada palavra em maiúsculo
# ele quebra em cada espaço
print(frase.title())
