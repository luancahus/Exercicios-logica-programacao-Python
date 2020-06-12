#Bissexto

Bi = int(input('Digite um ano '))

if bi% 4 == 0 and (bi % 100 != 0 or bi % 400 == 0):
print(f'o ano {bi} é bissexto')
else:
print(f'o ano {bi} não é bissexto')
