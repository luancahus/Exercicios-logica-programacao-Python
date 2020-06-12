Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
#Multa
peso = int(input('Digite o peso do peixe em kg (apenas num inteiros) '))
excesso = peso - 50

if excesso > 0:
multa = excesso * 4
print(f'Excesso: {excesso}kg ')
print(f'multa: R$ {multa}')
else:
multa = 0
excesso = 0
print(f'Excesso: {excesso}kg ')
print(f'multa: R$ {multa}')
