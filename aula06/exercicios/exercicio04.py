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

tela.title("Calculando preços")
tela.configure(background='#c0c0c0')
tela.geometry("380x550")
tela.resizable(False,False)

Label(tela, font="Arial 24 bold", text="Calculando", fg='#000', bg='#c0c0c0').place(x=100,y=20)

nome = Label(tela, font="Arial 14", text="Qual o nome do produto? ", fg='#000', bg='#c0c0c0').place(x=20,y=100)
txtNome = Entry(tela, width=55, borderwidth=0, fg="black")
txtNome.place(x=20, y=133)

quantidade = Label(tela, font="Arial 14", text="E a quantidade comprada? ", fg='#000', bg='#c0c0c0').place(x=20,y=155)
txtQuantidade = Entry(tela, width=55, borderwidth=0, fg="black")
txtQuantidade.place(x=20, y=188)

preco = Label(tela, font="Arial 14", text="Por fim, qual o preço do produto? ", fg='#000', bg='#c0c0c0').place(x=20,y=210)
txtPreco = Entry(tela, width=55, borderwidth=0, fg="black")
txtPreco.place(x=20, y=243)

def mostrarDados():
     txtValorTotal.config(state="normal")
     
     valorTotalCompra = float(txtPreco.get()) * int(txtQuantidade.get()) 

     lblTitulo = Label(tela, text="Dados cadastrados:", font="Arial 18 bold", bg='#c0c0c0')
     lblTitulo.place(x=18, y=380)

     lblNome = Label(tela, text="Nome: " + txtNome.get() + ".", bg='#fff')
     lblNome.place(x=20, y=420)
     lblQuantidade = Label(tela, text="Quantidade: " + txtQuantidade.get() + ".", bg='#fff')
     lblQuantidade.place(x=20, y=440)
     lblPreco = Label(tela, text="Preço: " + txtPreco.get() + ".", bg='#fff')
     lblPreco.place(x=20, y=460)

     txtValorTotal.insert(0, str(valorTotalCompra))

     lblValorDaCompra = Label(tela, text="Valor da sua compra: " + str(valorTotalCompra) + ".", bg='#fff')
     lblValorDaCompra.place(x=20, y=480)
     txtValorTotal.config(state="disabled")

btnCadastrar = Button(tela, text="Calcular valor da compra", font="Arial 10 bold", bg="#fff", fg='#000', command=mostrarDados, width=40)
btnCadastrar.place(x=20, y=280)

valorTotal = Label(tela, font="Arial 14", text="Valor final da compra: ", fg='#000', bg='#c0c0c0').place(x=20,y=322)
txtValorTotal = Entry(tela, width=55, borderwidth=0, fg="black", state="disabled")
txtValorTotal.place(x=20, y=355)

tela.mainloop()