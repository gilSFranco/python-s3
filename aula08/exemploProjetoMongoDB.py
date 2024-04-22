import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import os
import pymongo

os.system('cls')

tela = Tk()

largura = 800
altura = 500

largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = largura_screen / 2 - largura / 2
posy = altura_screen / 2 - altura / 2

print(largura_screen, altura_screen)

tela.geometry("%dx%d+%d+%d"%(largura, altura, posx, posy))

tela.title("Exemplo MongoDB")
tela.configure(background='#c0c0c0')
tela.geometry("800x500")
tela.resizable(False,False)

exemplo = pymongo.MongoClient("mongodb://localhost:27017/")
db = exemplo["exemplo"]
collection = db["clientes"]

lblTitulo = Label(tela, font=("Arial", 30, "bold"), text="Cadastro de Clientes", fg='#000', bg='#c0c0c0').place(x=200,y=50)

lblCodigo = Label(tela, text="Código", fg='#000', bg='#c0c0c0').place(x=130,y=140)
txtCodigo = Entry(tela, width=20, borderwidth=0, fg='#000', bg='#fff')
txtCodigo.place(x=190,y=140)

lblNome = Label(tela, text="Nome", fg='#000', bg='#c0c0c0').place(x=130,y=170)
txtNome = Entry(tela, width=20, borderwidth=0, fg='#000', bg='#fff')
txtNome.place(x=190,y=170)

lblCpf = Label(tela, text="Cpf", fg='#000', bg='#c0c0c0').place(x=450,y=170)
txtCpf = Entry(tela, width=20, borderwidth=0, fg='#000', bg='#fff')
txtCpf.place(x=480,y=170)

lblIdade = Label(tela, text="Idade", fg='#000', bg='#c0c0c0').place(x=130,y=200)
txtIdade = Entry(tela, width=20, borderwidth=0, fg='#000', bg='#fff')
txtIdade.place(x=190,y=200)

lblEndereco = Label(tela, text="Endereco", fg='#000', bg='#c0c0c0').place(x=450,y=200)
txtEndereco = Entry(tela, width=20, borderwidth=0, fg='#000', bg='#fff')
txtEndereco.place(x=510,y=200)

lblCidade = Label(tela, text="Cidade", fg='#000', bg='#c0c0c0').place(x=130,y=230)
txtCidade = Entry(tela, width=20, borderwidth=0, fg='#000', bg='#fff')
txtCidade.place(x=190,y=230)

lblEstado = Label(tela, text="UF", bg='#c0c0c0').place(x=450, y=230)
comboUf = ttk.Combobox(tela, values=["Sao Paulo", "Santa Catarina", "Rio de Janeiro", "Minas Gerais", "Espirito Santo"])
comboUf.place(x=480, y=230)

def salvar():
    codigo = txtCodigo.get()
    nome = txtNome.get()
    cpf = txtCpf.get()
    idade = txtIdade.get()
    endereco = txtEndereco.get()
    cidade = txtCidade.get()
    uf = comboUf.get()

    cliente = { "codigo": codigo, "nome": nome, "cpf": cpf, "idade": idade, "endereco": endereco, "cidade": cidade, "uf": uf }
    collection.insert_one(cliente)

    messagebox.showinfo("Mensagem", f"Usuario com o id: {codigo} foi cadastrado com sucesso.")

    txtCodigo.delete(0, tk.END)
    txtNome.delete(0, tk.END)
    txtCpf.delete(0, tk.END)
    txtIdade.delete(0, tk.END)
    txtEndereco.delete(0, tk.END)
    txtCidade.delete(0, tk.END)
    comboUf.set("")

def update():
    codigo = txtCodigo.get()
    nome = txtNome.get()
    cpf = txtCpf.get()
    idade = txtIdade.get()
    endereco = txtEndereco.get()
    cidade = txtCidade.get()
    uf = comboUf.get()

    collection.update_one({ "codigo": codigo }, {"$set": {
        "nome": nome, 
        "cpf": cpf, 
        "idade": idade, 
        "endereco": endereco, 
        "cidade": cidade, 
        "uf": uf
    }})

    messagebox.showinfo("Mensagem", f"Usuario com o id: {codigo} foi atualizado com sucesso.")

    txtCodigo.delete(0, tk.END)
    txtNome.delete(0, tk.END)
    txtCpf.delete(0, tk.END)
    txtIdade.delete(0, tk.END)
    txtEndereco.delete(0, tk.END)
    txtCidade.delete(0, tk.END)
    comboUf.set("")

def excluir():
    codigo = txtCodigo.get()

    collection.delete_one({ "codigo": codigo })
    messagebox.showinfo("Mensagem", f"Usuario com o id: {codigo} foi deletado com sucesso.")

    txtCodigo.delete(0, tk.END)
    txtNome.delete(0, tk.END)
    txtCpf.delete(0, tk.END)
    txtIdade.delete(0, tk.END)
    txtEndereco.delete(0, tk.END)
    txtCidade.delete(0, tk.END)
    comboUf.set("")

def consultar():
    codigo = txtCodigo.get()

    response = collection.find_one({ "codigo": codigo })

    if response:
        txtNome.insert(END, f"{response['nome']}")
        txtCpf.insert(END, f"{response['cpf']}")
        txtIdade.insert(END, f"{response['idade']}")
        txtEndereco.insert(END, f"{response['endereco']}")
        txtCidade.insert(END, f"{response['cidade']}")
        comboUf.insert(END, f"{response['uf']}")

        messagebox.showinfo("Mensagem", f"Usuario com o id: {codigo} foi consultado com sucesso.")

    else:
        messagebox.showinfo("Mensagem", "Nenhum resultado encontrado.")

btnSalvar = Button(tela, text="Salvar", width=7, height=2, command=salvar).place(x=130, y=280)
btnUpdate = Button(tela, text="Atualizar", width=7, height=2, command=update).place(x=220, y=280)
btnExcluir = Button(tela, text="Excluir", width=7, height=2, command=excluir).place(x=310, y=280)
btnConsultar = Button(tela, text="Consultar", width=7, height=2, command=consultar).place(x=400, y=280)
btnSair = Button(tela, text="Sair", width=7, height=2, command=tela.quit).place(x=490, y=280)

tela.mainloop()