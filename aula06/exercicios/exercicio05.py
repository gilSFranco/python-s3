import os
from tkinter import *

os.system('cls')

tela = Tk()

largura = 380
altura = 550

largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

print(largura_screen,altura_screen)

tela.geometry("%dx%d+%d+%d"%(largura,altura,posx,posy))

tela.title("Cadastrando contatos")
tela.configure(background='#c0c0c0')
tela.geometry("380x550")
tela.resizable(False,False)

Label(tela, font="Arial 24 bold", text="Cadastrando", fg='#000', bg='#c0c0c0').place(x=95,y=20)

nome = Label(tela, font="Arial 14", text="Qual o nome do contato? ", fg='#000', bg='#c0c0c0').place(x=20,y=100)
txtNome = Entry(tela, width=55, borderwidth=0, fg="black")
txtNome.place(x=20, y=133)

telefone = Label(tela, font="Arial 14", text="Telefone: ", fg='#000', bg='#c0c0c0').place(x=20,y=155)
txtTelefone = Entry(tela, width=55, borderwidth=0, fg="black")
txtTelefone.place(x=20, y=188)

endereco = Label(tela, font="Arial 14", text="Endereço: ", fg='#000', bg='#c0c0c0').place(x=20,y=210)
txtEndereco = Entry(tela, width=55, borderwidth=0, fg="black")
txtEndereco.place(x=20, y=243)

cidade = Label(tela, font="Arial 14", text="Cidade: ", fg='#000', bg='#c0c0c0').place(x=20,y=265)
txtCidade = Entry(tela, width=55, borderwidth=0, fg="black")
txtCidade.place(x=20, y=298)

def mostrarDados(): 
     lblTitulo = Label(tela, text="Dados cadastrados:", font="Arial 18 bold", bg='#c0c0c0')
     lblTitulo.place(x=18, y=380)

     lblNome = Label(tela, text="Nome: " + txtNome.get() + ".", bg='#fff')
     lblNome.place(x=20, y=420)
     lblTelefone = Label(tela, text="Telefone: " + txtTelefone.get() + ".", bg='#fff')
     lblTelefone.place(x=20, y=440)
     lblEndereco = Label(tela, text="Endereço: " + txtEndereco.get() + ".", bg='#fff')
     lblEndereco.place(x=20, y=460)
     lblCidade = Label(tela, text="Cidade: " + txtCidade.get() + ".", bg='#fff')
     lblCidade.place(x=20, y=480)

btnCadastrar = Button(tela, text="Cadastrar novo contato", font="Arial 10 bold", bg="#fff", fg='#000', command=mostrarDados, width=40)
btnCadastrar.place(x=20, y=335)

tela.mainloop()