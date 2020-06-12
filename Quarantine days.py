'''Programa para contar os dias que se passaram durante a quarentena !!'''

from tkinter import *
from datetime import date, datetime


Início = datetime.strptime('18/03/2020', '%d/%m/%Y').date()
hoje = date.today()
dias = (hoje - Início).days


window = Tk()
window.title('DIAS DA MALDITA QUARENTENA')
window.geometry('500x300+450+350')
window.configure(bg = 'black')


texto = Label(window,text = 'DIAS DA MALDITA QUARENTENA')
texto.place(x = 85, y= 90)
texto.configure(bg = 'red', font = 'Monaco 18', justify = CENTER)
dias_quarentena = Label(window, text = str(dias))
dias_quarentena.place(x=190, y=150)
dias_quarentena.config(bg='yellow', font = 'Monaco 20 bold', justify = CENTER)

window.mainloop()
