
print('Vamos calcular sua média e saber se foi aprovado(a)!')
aluno = str(input('Digite seu nome: ')) .title()
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'{aluno}, sua média foi: {m}')
print('PARABÉNS você passou! 😄' if m >=6 else 'Você está na recuperação 😥')
