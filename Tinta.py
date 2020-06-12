Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
#Tinta
Pintar = float(input('Qual o tamnaho da área em m quadrados a ser pintada '))
Latas = math.ceil((Pintar/3)/18)
Preco = totalLatas * 80

print(f'Numero de Latas: {Latas}')
print(f'Preço total: R${Preco}')

