import os
from tkinter import *

os.system('cls')

tela = Tk()

tela.title("The Last of Us")
tela.configure(background='#000')
tela.geometry("500x500")
tela.resizable(True,True)
tela.maxsize(width=700,height=600)
tela.minsize(width=500,height=500)
tela.iconbitmap('C:/Users/fatec-dsm3/Downloads/chama.ico')

nome = Label(tela, font="Arial 14 bold", text="Nome: ", fg='#fff', bg='#000').place(x=20,y=20)

txtNome = Entry(tela, width=60, borderwidth=3, fg="black")
txtNome.place(x=100, y=25)
txtNome.insert(0, "Digite seu nome: ")

cpf = Label(tela, font="Arial 14 bold", text="Cpf: ", fg='#fff', bg='#000').place(x=20,y=65)

txtCpf = Entry(tela, width=63, borderwidth=3, fg="black")
txtCpf.place(x=80, y=70)
txtCpf.insert(0, "Digite seu cpf: ")

tela.mainloop()