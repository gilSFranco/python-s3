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

tela.title("Calculando médias")
tela.configure(background='#c0c0c0')
tela.geometry("380x550")
tela.resizable(False,False)

Label(tela, font="Arial 24 bold", text="Calculando", fg='#000', bg='#c0c0c0').place(x=100,y=20)

nota01 = Label(tela, font="Arial 14", text="Digite a primeira nota: ", fg='#000', bg='#c0c0c0').place(x=20,y=100)
txtNota01 = Entry(tela, width=55, borderwidth=0, fg="black")
txtNota01.place(x=20, y=133)

nota02 = Label(tela, font="Arial 14", text="Digite a segunda nota: ", fg='#000', bg='#c0c0c0').place(x=20,y=155)
txtNota02 = Entry(tela, width=55, borderwidth=0, fg="black")
txtNota02.place(x=20, y=188)

nota03 = Label(tela, font="Arial 14", text="Digite a terceira nota: ", fg='#000', bg='#c0c0c0').place(x=20,y=210)
txtNota03 = Entry(tela, width=55, borderwidth=0, fg="black")
txtNota03.place(x=20, y=243)

def mostrarDados():
     txtMedia.config(state="normal")
     
     mediaDasNotas = (int(txtNota01.get()) + int(txtNota02.get()) + int(txtNota03.get())) / 3

     lblTitulo = Label(tela, text="Dados cadastrados:", font="Arial 18 bold", bg='#c0c0c0')
     lblTitulo.place(x=18, y=380)

     lblNota01 = Label(tela, text="Nota 01: " + txtNota01.get() + ".", bg='#fff')
     lblNota01.place(x=20, y=420)
     lblNota02 = Label(tela, text="Nota 02: " + txtNota02.get() + ".", bg='#fff')
     lblNota02.place(x=20, y=440)
     lblNota03 = Label(tela, text="Nota 03: " + txtNota03.get() + ".", bg='#fff')
     lblNota03.place(x=20, y=460)

     txtMedia.insert(0, str(mediaDasNotas))

     lblMedia = Label(tela, text="Média das notas: " + str(mediaDasNotas) + ".", bg='#fff')
     lblMedia.place(x=20, y=480)
     txtMedia.config(state="disabled")

btnCadastrar = Button(tela, text="Calcular média", font="Arial 10 bold", bg="#fff", fg='#000', command=mostrarDados, width=40)
btnCadastrar.place(x=20, y=280)

media = Label(tela, font="Arial 14", text="Média das notas: ", fg='#000', bg='#c0c0c0').place(x=20,y=322)
txtMedia = Entry(tela, width=55, borderwidth=0, fg="black", state="disabled")
txtMedia.place(x=20, y=355)

tela.mainloop()