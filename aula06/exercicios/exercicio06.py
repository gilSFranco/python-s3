import os
from tkinter import *

os.system('cls')

tela = Tk()

largura = 380
altura = 600

largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

print(largura_screen,altura_screen)

tela.geometry("%dx%d+%d+%d"%(largura,altura,posx,posy))

tela.title("Calculando a velocidade")
tela.configure(background='#c0c0c0')
tela.geometry("380x600")
tela.resizable(False,False)

Label(tela, font="Arial 24 bold", text="Calculando", fg='#000', bg='#c0c0c0').place(x=100,y=20)

nome = Label(tela, font="Arial 14", text="Qual o nome do carro? ", fg='#000', bg='#c0c0c0').place(x=20,y=100)
txtNome = Entry(tela, width=55, borderwidth=0, fg="black")
txtNome.place(x=20, y=133)

distancia = Label(tela, font="Arial 14", text="Distancia percorrida (em metros): ", fg='#000', bg='#c0c0c0').place(x=20,y=155)
txtDistancia = Entry(tela, width=55, borderwidth=0, fg="black")
txtDistancia.place(x=20, y=188)

tempo = Label(tela, font="Arial 14", text="Tempo (em m/s): ", fg='#000', bg='#c0c0c0').place(x=20,y=210)
txtTempo = Entry(tela, width=55, borderwidth=0, fg="black")
txtTempo.place(x=20, y=243)

def mostrarDados(): 
     txtVelocidade.config(state="normal")
     lblTitulo = Label(tela, text="Dados cadastrados:", font="Arial 18 bold", bg='#c0c0c0')
     lblTitulo.place(x=18, y=435)

     velocidade = (float(txtDistancia.get()) * 1000) / (float(txtTempo.get()) * 60)

     lblNome = Label(tela, text="Nome: " + txtNome.get() + ".", bg='#fff')
     lblNome.place(x=20, y=475)
     lblTelefone = Label(tela, text="Distancia: " + txtDistancia.get() + ".", bg='#fff')
     lblTelefone.place(x=20, y=495)
     lblEndereco = Label(tela, text="Tempo: " + txtTempo.get() + ".", bg='#fff')
     lblEndereco.place(x=20, y=515)
     lblCidade = Label(tela, text="Velocidade: " + str(round(velocidade, 2)) + ".", bg='#fff')
     lblCidade.place(x=20, y=535)

     txtVelocidade.insert(0, str(round(velocidade, 2)))
     txtVelocidade.config(state="disabled")

btnCadastrar = Button(tela, text="Calculando a velocidade", font="Arial 10 bold", bg="#fff", fg='#000', command=mostrarDados, width=40)
btnCadastrar.place(x=20, y=335)

velocidade = Label(tela, font="Arial 14", text="Velocidade do carro: ", fg='#000', bg='#c0c0c0').place(x=20,y=377)
txtVelocidade = Entry(tela, width=55, borderwidth=0, fg="black", state="disabled")
txtVelocidade.place(x=20, y=410)

tela.mainloop()