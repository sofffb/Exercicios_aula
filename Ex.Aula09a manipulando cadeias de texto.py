
print('  \n * Aula 09 - Prática de manipulação de texto  \n')


# FATIAMENTO DE TEXTO

print(' * Fatiamento do texto a seguir: \n')


frase = 'Curso em Vídeo Python'
print (frase , '\n')


print (' → A quarta letra da frase é: ')
print (frase[3] , ' \n ' )


print (' → Fatiamento da quarta letra até a décima terceira:')
print (frase[3:13] , ' \n ')


print (' → Fatiamento do início do texto até o 13 caractere:')
print (frase[:13] , ' \n' )


print(' → Fatiamento da décima terceira letra até o final da string:')
print(frase[13:] , ' \n ')


print(' → Fatiamento da 1 até 15 letra:')
print(frase[1:15] , ' \n ')


print(' → Leia a frase pulando de duas em duas letras:')
print(frase[::2] , ' \n ')


print(' * Print em texto longo:  \n ')

print('''Python é uma linguagem de programação usada para criar apps,
sites, ciência de dados, análise de dados e
automação de tarefas e muito mais.
É uma linguagem de alto nível, com sentaxe simples e legível.
Pode ser executada em várias plataformas, como Linux, Mac, e Microsoft.
É uma boa escolha para quem está iniciando na programação.  \n ''')



print(' * FUNÇÕES:  \n ')


#Análise len(frase) -> comprimento da frase -> 21 caracteres
print(' → Quantos caracteres tem na string?:')
print (len(frase) , ' \n ')


# frase.count('o') -> vai me dizer quantas letras 'o' aparecem na frase
print(' → Quantas vezes a letra "V" aparece na string?:')
print(frase.count('V') ,  ' \n ')


# buscar uma palavra dentro de um texto, como não tem, ele me retorna '-1'
print(' → Busque palavra "android" nesse texto:')
print(frase.find('android') , ' \n ')


# por exemplo, ele vai me dar um TRUE or FALSE por causa do operador: 'in'
print(' → Existe a palavra "android" nesse texto?:')
print('curso' in frase , ' \n ')


print('Transformando a frase em letras maiúsculas e procure uma letra "O" no texto:')
print(frase.upper().count('O') , ' \n ')

print(' * TRANSFORMAÇÃO:  \n ')


print(' → Substituição:  \n ' )
print(frase.replace('Python', 'Android') , ' \n ')


print(' → Colocando todas as letras em maiúsculo:  \n ')
print(frase.upper() , ' \n ')


print(' → Transformando todas as letras em minúsculo:')
print(frase.lower() , ' \n ')


print(' → Deixando somente a primeira letra da frase em maiúsculo:')
print(frase.capitalize() , ' \n ')

# para Deixar somente a primeira letra de cada palavra em maiúsculo
# ele quebra em cada espaço
print(frase.title())
