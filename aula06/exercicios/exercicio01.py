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

tela.title("Cadastro de Clientes")
tela.configure(background='#c0c0c0')
tela.geometry("380x500")
tela.resizable(False,False)

Label(tela, font="Arial 24 bold", text="Cadastro", fg='#000', bg='#c0c0c0').place(x=115,y=20)

nome = Label(tela, font="Arial 14", text="Nome: ", fg='#000', bg='#c0c0c0').place(x=20,y=100)
txtNome = Entry(tela, width=43, borderwidth=0, fg="black")
txtNome.place(x=90, y=108)

email = Label(tela, font="Arial 14", text="Email: ", fg='#000', bg='#c0c0c0').place(x=20,y=140)
txtEmail = Entry(tela, width=43, borderwidth=0, fg="black")
txtEmail.place(x=90, y=148)

telefone = Label(tela, font="Arial 14", text="Telefone: ", fg='#000', bg='#c0c0c0').place(x=20,y=180)
txtTelefone = Entry(tela, width=38, borderwidth=0, fg="black")
txtTelefone.place(x=120, y=188)

endereco = Label(tela, font="Arial 14", text="Endereço: ", fg='#000', bg='#c0c0c0').place(x=20,y=220)
txtEndereco = Entry(tela, width=37, borderwidth=0, fg="black")
txtEndereco.place(x=125, y=228)

def mostrarDados():
     lblTitulo = Label(tela, text="Dados cadastrados:", font="Arial 18 bold", bg='#c0c0c0')
     lblTitulo.place(x=18, y=340)

     lblNome = Label(tela, text="Nome: " + txtNome.get() + ".", bg='#fff')
     lblNome.place(x=20, y=380)
     lblEmail = Label(tela, text="Email: " + txtEmail.get() + ".", bg='#fff')
     lblEmail.place(x=20, y=400)
     lblTelefone = Label(tela, text="Telefone: " + txtTelefone.get() + ".", bg='#fff')
     lblTelefone.place(x=20, y=420)
     lblEndereco = Label(tela, text="Endereço: " + txtEndereco.get() + ".", bg='#fff')
     lblEndereco.place(x=20, y=440)

btnCadastrar = Button(tela, text="Cadastrar", font="Arial 10 bold", bg="#fff", fg='#000', command=mostrarDados, width=40)
btnCadastrar.place(x=20, y=280)

tela.mainloop()