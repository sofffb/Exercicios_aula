# TRANSFORMAÇÃO - continuação:

frase = 'Curso em Vídeo Python'
# Divisão: ele refez os índices, ele gera uma lista
dividido = frase.split()
print(dividido)
# Com a frase segregada, quero apenas o índice 2:
print(dividido[2])
# Dentro da string dividida, no caso, a '2', quero a terceira letra:
# pegue o dividido '2'e me mostre a letra '3'
print(dividido[2][3])
# Junção:
print('-'.join(frase))
