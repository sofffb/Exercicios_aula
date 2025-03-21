# importar a biblioteca math
import math
n1 =int(input('digite um número: '))
n2 =int(input('Digite outro número: '))

# posso fazer ações como por exemplo, multiplicar dentro dos colchetes
print (f'o dobro de {n1} é {n1 * 2} \n  e a raiz é {math.sqrt(n1)}')

# formatar o número para deixar apenas duas casas decimais -> :.2f
print (f'A divisão entre {n1} e {n2} é: {n1 / n2:.2f}')

# fazer quebra de linha usando -> \n
print ('este é um exemplo de como quebrar esta frase aqui \n e ela continuar abaixo desa forma')

# fazer com que a frase seja estendida, sem quebra -> , end='  '
print(' este é um exemplo de como posso' , end=' ')
print('colocar duas frases em apena uma')


