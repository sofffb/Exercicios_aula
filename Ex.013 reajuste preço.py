# valor do produto com desconto e valor parcelado

prod = float(input('Digite o valor do produto: R$ '))
desc = prod - (prod * 5 / 100)
parc = prod + (prod * 5 / 100)
print(f'O produto com desconto de 5% a vista, fica: R$ {desc}')
print(f'O valor do produto parcelado com acréscimo de 5%, ficando: R$ {parc}')
