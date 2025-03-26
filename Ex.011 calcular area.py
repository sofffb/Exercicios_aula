#programa que leia a área de um muro e diga quantos litros de tinta vai precisar
larg = float(input('Qual a largura do seu muro?: '))
alt = float(input('Qual a altura do seu muro?: '))
area = larg * alt
tinta = area / 2

print(f'Seu muro tem: {larg} de largura, {alt} de altura, com área de {area}m²')
print(f'Portanto você precisará de {tinta:.1f} litros de tinta.')
