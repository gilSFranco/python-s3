from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import pymongo
import tkinter as tk

tela = Tk()
tela.title("Controle de Veículos - Cadastrando")
tela.configure(background='#c0c0c0')

tela.geometry("750x450")
tela.resizable(False, False)

exemplo = pymongo.MongoClient("mongodb://localhost:27017/")
db = exemplo["controleVeiculos"]
collection = db["veiculos"]

pastaInicial = ""

def escolherImagem():
    caminhoImagem = filedialog.askopenfilename(initialdir=pastaInicial, title="Escolha a imagem...",
                                                filetypes=(("Arquivos de Imagem", "*.jpg;*.jpeg;*.png"),
                                                           ("Todos os arquivos", "*.*")))
    imagemPil = Image.open(caminhoImagem)
    largura, altura = imagemPil.size
    if largura > 150:
        proporcao = largura / 150
        novaAltura = int(altura/proporcao)
        imagemPil = imagemPil.resize((150, novaAltura))

    imagemTk = ImageTk.PhotoImage(imagemPil)
    lblImagem = Label(tela, image=imagemTk)
    lblImagem.image = imagemTk
    lblImagem.place(x=40, y=40)

def sair():
    sys.exit()

def limpar():
    txtCodigo.delete(0, tk.END)
    txtNome.delete(0, tk.END)
    txtPlaca.delete(0, tk.END)
    txtModelo.delete(0, tk.END)
    combo.set("")

def salvar():
    codigo = txtCodigo.get()
    nome = txtNome.get()
    placa = txtPlaca.get()
    utilitario = varRadioUtilitario.get()
    modelo = txtModelo.get()
    marca = combo.get()

    veiculo = { 
        "codigo": codigo, 
        "nome": nome,
        "placa": placa,
        "utilitario": utilitario,
        "modelo": modelo,
        "marca": marca
    }

    collection.insert_one(veiculo)

    messagebox.showinfo("Mensagem", f"Veiculo com o id: {codigo} foi cadastrado com sucesso.")

    txtCodigo.delete(0, tk.END)
    txtNome.delete(0, tk.END)
    txtPlaca.delete(0, tk.END)
    txtModelo.delete(0, tk.END)
    combo.set("")

def update():
    codigo = txtCodigo.get()
    nome = txtNome.get()
    placa = txtPlaca.get()
    utilitario = varRadioUtilitario.get()
    modelo = txtModelo.get()
    marca = combo.get()

    collection.update_one({ "codigo": codigo }, {"$set": {
        "codigo": codigo, 
        "nome": nome,
        "placa": placa,
        "utilitario": utilitario,
        "modelo": modelo,
        "marca": marca
    }})

    messagebox.showinfo("Mensagem", f"Veiculo com o id: {codigo} foi atualizado com sucesso.")

    txtCodigo.delete(0, tk.END)
    txtNome.delete(0, tk.END)
    txtPlaca.delete(0, tk.END)
    txtModelo.delete(0, tk.END)
    combo.set("")

def excluir():
    codigo = txtCodigo.get()

    collection.delete_one({ "codigo": codigo })

    messagebox.showinfo("Mensagem", f"Veiculo com o id: {codigo} foi deletado com sucesso.")

    txtCodigo.delete(0, tk.END)
    txtNome.delete(0, tk.END)
    txtPlaca.delete(0, tk.END)
    txtModelo.delete(0, tk.END)
    combo.set("")

def consultar():
    codigo = txtCodigo.get()

    response = collection.find_one({ "codigo": codigo })

    txtCodigo.delete(0, tk.END)
    combo.set("")

    if response:
        txtCodigo.insert(END, f"{response['codigo']}")
        txtNome.insert(END, f"{response['nome']}")
        txtPlaca.insert(END, f"{response['placa']}")
        txtModelo.insert(END, f"{response['modelo']}")
        combo.insert(END, f"{response['marca']}")
        varRadioUtilitario.set(f"{response['utilitario']}")

        messagebox.showinfo("Mensagem", f"Veiculo com o id: {codigo} foi consultado com sucesso.")
    else:
        messagebox.showinfo("Mensagem", "Nenhum resultado encontrado.")

btnEscolher = Button(tela, text ="Escolher Imagem" , command=escolherImagem)
btnEscolher.place(x=40, y=200)

lblCodigo = Label(tela, font="Arial 14", text="Codigo:", fg='#000', bg='#c0c0c0').place(x=250, y=40)
txtCodigo = Entry(tela, width=10, borderwidth=0, fg="black")
txtCodigo.place(x=330, y=47)

lblNome = Label(tela, font="Arial 14", text="Nome:", fg='#000', bg='#c0c0c0').place(x=250, y=80)
txtNome = Entry(tela, width=40, borderwidth=0, fg="black")
txtNome.place(x=320, y=87)

lblPlaca = Label(tela, font="Arial 14", text="Placa:", fg='#000', bg='#c0c0c0').place(x=250, y=120)
txtPlaca = Entry(tela, width=40, borderwidth=0, fg="black")
txtPlaca.place(x=320, y=127)

varRadioUtilitario = StringVar()
varRadioUtilitario.set("Utilitário")

radioButtonUT = Radiobutton(tela, text="Utilitário", variable=varRadioUtilitario, value="Utilitário", bg='#c0c0c0').place(x=250, y=160)
radioButtonUF = Radiobutton(tela, text="Não utilitário", variable=varRadioUtilitario, value="Não utilitário", bg='#c0c0c0').place(x=350, y=160)

lblModelo = Label(tela, font="Arial 14", text="Modelo:", fg='#000', bg='#c0c0c0').place(x=250, y=200)
txtModelo = Entry(tela, width=40, borderwidth=0, fg="black")
txtModelo.place(x=330, y=207)

lblMarca = Label(tela, font="Arial 14", text="Marca:", fg='#000', bg='#c0c0c0').place(x=250, y=240)
combo = ttk.Combobox(tela)
combo['values'] = ("Fiat","Chevrolet","Suzuky","Wolkswagen","Renault","Ford")
combo.current(2)
combo.place(x=320, y=247)

foto_salvar = PhotoImage(file = r"icones\salvar.png")
foto_excluir = PhotoImage(file = r"icones\excluir.png")
foto_alterar = PhotoImage(file = r"icones\alterar.png")
foto_consultar = PhotoImage(file = r"icones\consultar.png")
foto_sair = PhotoImage(file = r"icones\sair.png")

btn_salvar =  Button(tela, text="Salvar", image= foto_salvar ,compound=TOP, command=salvar).place(x=250,y=300)  
btn_excluir = Button(tela, text="Excluir", image=foto_excluir, compound=TOP, command=excluir).place(x=305,y=300)
btn_alterar =  Button(tela, text="Alterar", image= foto_alterar ,compound= TOP, command=update).place(x=360,y=300)  
btn_consultar = Button(tela, text="Consultar", image=foto_consultar, compound=TOP, command=consultar).place(x=415,y=300)
btn_limpar = Button(tela, text="Limpar", image=foto_excluir, compound=TOP, command=limpar).place(x=545,y=300)
btn_sair = Button(tela, text="Sair", image=foto_sair, compound=TOP, command=sair).place(x=600,y=300)

tela.mainloop()