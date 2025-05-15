# Programa em que: o computador escolha um número e o usuário tenta adivinhar qual foi.
print('Vamos brincar?')
p = str(input('Primeiro, qual o seu nome?: '))
n = int(input('Escolhi um número entre 0 até 5. Adivinhe qual é o número: '))
print(f' {p}, você acertou! ' if n ==2 else f'{p}, você errou! Continue tentando!' )
print('Fim! 😊')