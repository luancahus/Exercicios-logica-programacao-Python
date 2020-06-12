Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Q6: calculo de salario descontando impostos
horaTrab = int(input('Quantas horas foram trabalhadas nesse mês? '))
valHora = float(input('Quanto vale a hora trabalhada? '))
salBruto = horaTrab * valHora
salLiq = salBruto * 0.76
INSS = salBruto * 0.08
sindicato = salBruto * 0.05
leao = salBruto * 0.11
os.system('cls')

print('Salário Bruto = R$', salBruto)
print('Salário Liquido = R$', salLiq)
print('desconto INSS = R$', INSS)
print('desconto sindicato = R$', sindicato)
print('desconto Imposto de renda = R$', leao)
