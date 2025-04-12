# prática de manipulação de texto

# FATIAMENTO DE TEXTO

frase = 'Curso em Vídeo Python'
print (frase)
# a quarta letra da frase:
print (frase[3])
# fatiar da quarta letra até a décima terceira:
print (frase[3:13])
# do início até o 13:
print (frase[:13])
# da décima terceira letra até o final:
print(frase[13:])
# da 1 até 15
print(frase[1:15])
# ler a frase e pular de duas em duas letras:
print(frase[::2])

# FUNÇÕES

#Análise len(frase) -> comprimento da frase -> 21 caracteres
print (len(frase))
# frase.count('o') -> vai me dizer quantas letras 'o' aparecem na frase
print((frase.count('V')))
# buscar uma palavra dentro de um texto, como não tem, ele me retorna '-1'
print(frase.find('android'))
# por exemplo, ele vai me dar um TRUE or FALSE por causa do operador: 'in'
print('curso' in frase)
# transformar a frase em letras maiúsculas e procurar uma letra maiúscula
print(frase.upper().count('O'))

# TRANSFORMAÇÃO

# substituir
print(frase.replace('Python', 'Android'))
# para colocar todas as letras em maiúsculo
print(frase.upper())
# para trasnformar todas as letras em minúsculo
print(frase.lower())
# para Deixar somente a primeira letra da frase em maiúsculo
print(frase.capitalize())
# para Deixar somente a primeira letra de cada palavra em maiúsculo
# ele quebra em cada espaço
print(frase.title())
