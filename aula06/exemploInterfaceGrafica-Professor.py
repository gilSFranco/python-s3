from tkinter import *
#criação tela
tela = Tk()
#define icone

#titulo tela
tela.title("FATEC REGISTRO")
#COR DA TELA
tela.configure(background='#1e3743')

#dimensoes da tela 
largura = 720
altura = 600

#resolução do sistema(tela)
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 -altura/2

#visualizacao do tamanho da tela no terminal
print(largura_screen,altura_screen)

tela.geometry("%dx%d+%d+%d"%(largura,altura,posx,posy))

#tamanho da tela
tela.geometry("720x600")
#definir tamanho maximo e minimo tela
tela.resizable(True,True)
#define tamanho maximo
tela.maxsize(width=800,height=700)
#define tamanho minimo
tela.minsize(width=500, height=300)
tela.iconbitmap('C:/Users/lbarreto/Pictures/icone.ico')
#colocando LAbel
lbl_nome = Label(tela,font="Arial 10 bold italic",text="Nome: ",fg='#fff',bg='#1e3743').place(x= 10 , y= 15)
#colocando Caixa de Texto
txt_nome = Entry(tela, width= 60 , borderwidth= 3, fg="blue")
txt_nome.place(x= 60 , y = 15)
txt_nome.insert(0,"Digite seu nome")

lbl_cpf = Label(tela, text="CPF: ", fg='#fff', bg='#1e3743').place(x=40, y= 45)
txt_cpf = Entry(tela, width = 40, borderwidth= 3,fg="blue")
txt_cpf.place(x= 70 , y = 45)
txt_cpf.insert(0,"Digite CPF")

#funçao mostradados
def mostraDados():
 lbl_titulo = Label(tela, text="Dados Pessoa", font="Arial 20 italic")
 lbl_titulo.place(x= 205 , y= 145)
 lbl_dados = Label(tela, text="Nome: " + txt_nome.get() + "\n CPF: " + txt_cpf.get())
 lbl_dados.place(x= 205, y= 175)

#colocando botão
btn_botao = Button(tela,text="Cadastrar", font="Arial 10 bold", bg="#1ed", command=mostraDados)
btn_botao.place(x= 200 , y = 90)

tela.mainloop()