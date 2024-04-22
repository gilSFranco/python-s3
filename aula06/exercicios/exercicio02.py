import os
from tkinter import *

os.system('cls')

tela = Tk()

largura = 380
altura = 500

largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

print(largura_screen,altura_screen)

tela.geometry("%dx%d+%d+%d"%(largura,altura,posx,posy))

tela.title("Fazendo calcúlos")
tela.configure(background='#c0c0c0')
tela.geometry("380x500")
tela.resizable(False,False)

Label(tela, font="Arial 24 bold", text="Somando", fg='#000', bg='#c0c0c0').place(x=115,y=20)

numero01 = Label(tela, font="Arial 14", text="Digite o primeiro número: ", fg='#000', bg='#c0c0c0').place(x=20,y=100)
txtNumero01 = Entry(tela, width=55, borderwidth=0, fg="black")
txtNumero01.place(x=20, y=133)

numero02 = Label(tela, font="Arial 14", text="Digite o segundo número: ", fg='#000', bg='#c0c0c0').place(x=20,y=155)
txtNumero02 = Entry(tela, width=55, borderwidth=0, fg="black")
txtNumero02.place(x=20, y=188)

soma = Label(tela, font="Arial 14", text="Soma dos números: ", fg='#000', bg='#c0c0c0').place(x=20,y=210)
txtSoma = Entry(tela, width=55, borderwidth=0, fg="black", state="disabled")
txtSoma.place(x=20, y=243)

def mostrarDados():
     txtSoma.config(state="normal")

     somando = int(txtNumero01.get()) + int(txtNumero02.get())

     lblTitulo = Label(tela, text="Dados cadastrados:", font="Arial 18 bold", bg='#c0c0c0')
     lblTitulo.place(x=18, y=340)

     lblNumero01 = Label(tela, text="Numero 01: " + txtNumero01.get() + ".", bg='#fff')
     lblNumero01.place(x=20, y=380)
     lblNumero02 = Label(tela, text="Numero 02: " + txtNumero02.get() + ".", bg='#fff')
     lblNumero02.place(x=20, y=400)

     txtSoma.insert(0, str(somando))
     lblSoma = Label(tela, text="Soma dos números: " + txtNumero01.get() + " + " + txtNumero02.get() + " = " + str(somando) + ".", bg='#fff')
     lblSoma.place(x=20, y=420)

     txtSoma.config(state="disabled")

btnCadastrar = Button(tela, text="Calcular soma", font="Arial 10 bold", bg="#fff", fg='#000', command=mostrarDados, width=40)
btnCadastrar.place(x=20, y=280)

tela.mainloop()