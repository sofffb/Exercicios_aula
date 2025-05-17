# Programa que leia 3 números e diga qual o menor e maior.
# A função ->    min()   retorna o menor valor entre os argumentos
# A função ->    max()   retorna o maior valor entre os argumentos

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

menor = min(n1, n2, n3)
maior = max(n1, n2, n3)

print(f' O MENOR número é: {menor}  \n  &  \n o MAIOR número é: {maior}')
