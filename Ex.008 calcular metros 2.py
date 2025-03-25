# calcular km, hec, dam, m , dm, cm e mm

num = float(input('Digite um valor em metros: '))
km = num / 1000
hm = num / 100
dam = num / 10
dm = num * 10
cm = num * 100
mm = num * 1000

print(f'Você digitou a medida {num} em metros, ficaria:')
print(f'Em Kilômetros: {km}')
print(f'Em Hectômetros: {hm}')
print(f'Em Decâmetro: {dam}')
print(f'Em decímetros: {dm}')
print(f'Em cntímetros: {cm}')
print(f'Em milímetros: {mm}')
