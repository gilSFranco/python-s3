from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import pymongo
import tkinter as tk

tela = Tk()
tela.title("Controle de Pessoas - Cadastrando")
tela.configure(background='#c0c0c0')

tela.geometry("1050x450")
tela.resizable(False, False)

exemplo = pymongo.MongoClient("mongodb://localhost:27017/")
db = exemplo["controlePessoas"]
collection = db["pessoas"]

pastaInicial = "imgs/icone-guts.jpg"

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
    txtIdade.delete(0, tk.END)
    txtAltura.delete(0, tk.END)
    txtPeso.delete(0, tk.END)
    txtDataNascimento.delete(0, tk.END)
    txtDataCadastro.delete(0, tk.END)
    txtDataAtualizacao.delete(0, tk.END)
    txtDescricao.delete(0, tk.END)
    combo.set("")
    varRadioSexo.set("")    

def salvar():
    codigo = txtCodigo.get()
    nome = txtNome.get()
    sexo = varRadioSexo.get()
    idade = txtIdade.get()
    altura = txtAltura.get()
    peso = txtPeso.get()
    cidade = combo.get()
    dataNascimento = txtDataNascimento.get()
    dataCadastro = txtDataCadastro.get()
    dataAtualizacao = txtDataAtualizacao.get()
    descricao = txtDescricao.get()

    cliente = {
        "codigo": codigo, 
        "nome": nome, 
        "sexo": sexo, 
        "idade": idade, 
        "altura": altura, 
        "peso": peso, 
        "cidade": cidade,
        "dataNascimento": dataNascimento,
        "dataCadastro": dataCadastro,
        "dataAtualizacao": dataAtualizacao,
        "descricao": descricao 
    }

    collection.insert_one(cliente)

    messagebox.showinfo("Mensagem", f"Usuario com o id: {codigo} foi cadastrado com sucesso.")

    txtCodigo.delete(0, tk.END)
    txtNome.delete(0, tk.END)
    txtIdade.delete(0, tk.END)
    txtAltura.delete(0, tk.END)
    txtPeso.delete(0, tk.END)
    txtDataNascimento.delete(0, tk.END)
    txtDataCadastro.delete(0, tk.END)
    txtDataAtualizacao.delete(0, tk.END)
    txtDescricao.delete(0, tk.END)
    combo.set("")
    varRadioSexo.set("")

def update():
    codigo = txtCodigo.get()
    nome = txtNome.get()
    sexo = varRadioSexo.get()
    idade = txtIdade.get()
    altura = txtAltura.get()
    peso = txtPeso.get()
    cidade = combo.get()
    dataNascimento = txtDataNascimento.get()
    dataCadastro = txtDataCadastro.get()
    dataAtualizacao = txtDataAtualizacao.get()
    descricao = txtDescricao.get()

    collection.update_one({ "codigo": codigo }, {"$set": {
        "codigo": codigo, 
        "nome": nome, 
        "sexo": sexo, 
        "idade": idade, 
        "altura": altura, 
        "peso": peso, 
        "cidade": cidade,
        "dataNascimento": dataNascimento,
        "dataCadastro": dataCadastro,
        "dataAtualizacao": dataAtualizacao,
        "descricao": descricao
    }})

    messagebox.showinfo("Mensagem", f"Usuario com o id: {codigo} foi atualizado com sucesso.")

    txtCodigo.delete(0, tk.END)
    txtNome.delete(0, tk.END)
    txtIdade.delete(0, tk.END)
    txtAltura.delete(0, tk.END)
    txtPeso.delete(0, tk.END)
    txtDataNascimento.delete(0, tk.END)
    txtDataCadastro.delete(0, tk.END)
    txtDataAtualizacao.delete(0, tk.END)
    txtDescricao.delete(0, tk.END)
    combo.set("")
    varRadioSexo.set("")

def excluir():
    codigo = txtCodigo.get()

    collection.delete_one({ "codigo": codigo })
    messagebox.showinfo("Mensagem", f"Usuario com o id: {codigo} foi deletado com sucesso.")

    txtCodigo.delete(0, tk.END)
    txtNome.delete(0, tk.END)
    txtIdade.delete(0, tk.END)
    txtAltura.delete(0, tk.END)
    txtPeso.delete(0, tk.END)
    txtDataNascimento.delete(0, tk.END)
    txtDataCadastro.delete(0, tk.END)
    txtDataAtualizacao.delete(0, tk.END)
    txtDescricao.delete(0, tk.END)
    combo.set("")
    varRadioSexo.set("")

def consultar():
    codigo = txtCodigo.get()

    response = collection.find_one({ "codigo": codigo })

    txtCodigo.delete(0, tk.END)
    combo.set("")

    if response:
        txtCodigo.insert(END, f"{response['codigo']}")
        txtNome.insert(END, f"{response['nome']}")
        txtIdade.insert(END, f"{response['idade']}")
        txtAltura.insert(END, f"{response['altura']}")
        txtPeso.insert(END, f"{response['peso']}")
        txtDataNascimento.insert(END, f"{response['dataNascimento']}")
        txtDataCadastro.insert(END, f"{response['dataCadastro']}")
        txtDataAtualizacao.insert(END, f"{response['dataAtualizacao']}")
        txtDescricao.insert(END, f"{response['descricao']}")
        combo.insert(END, f"{response['cidade']}")
        varRadioSexo.set(f"{response['sexo']}")

        messagebox.showinfo("Mensagem", f"Usuario com o id: {codigo} foi consultado com sucesso.")

    else:
        messagebox.showinfo("Mensagem", "Nenhum resultado encontrado.")

btnEscolher = Button(tela, text ="Escolher Imagem" , command=escolherImagem)
btnEscolher.place(x=40,y=200)

lblCodigo = Label(tela, font="Arial 14", text="Codigo:", fg='#000', bg='#c0c0c0').place(x=250, y=40)
txtCodigo = Entry(tela, width=10, borderwidth=0, fg="black")
txtCodigo.place(x=330, y=47)

lblNome = Label(tela, font="Arial 14", text="Nome:", fg='#000', bg='#c0c0c0').place(x=250, y=80)
txtNome = Entry(tela, width=40, borderwidth=0, fg="black")
txtNome.place(x=320, y=87)

lblIdade = Label(tela, font="Arial 14", text="Idade:", fg='#000', bg='#c0c0c0').place(x=590, y=80)
txtIdade = Entry(tela, width=10, borderwidth=0, fg="black")
txtIdade.place(x=660, y=87)

varRadioSexo = StringVar()
varRadioSexo.set("Masculino")

radioButtonM = Radiobutton(tela, text="Masculino", variable=varRadioSexo, value="Masculino", bg='#c0c0c0').place(x=250, y=122)
radioButtonF = Radiobutton(tela, text="Feminino", variable=varRadioSexo, value="Feminino", bg='#c0c0c0').place(x=350, y=122)

lblAltura = Label(tela, font="Arial 14", text="Altura:", fg='#000', bg='#c0c0c0').place(x=450, y=120)
txtAltura = Entry(tela, width=10, borderwidth=0, fg="black")
txtAltura.place(x=520, y=127)

lblPeso = Label(tela, font="Arial 14", text="Peso:", fg='#000', bg='#c0c0c0').place(x=610, y=120)
txtPeso = Entry(tela, width=10, borderwidth=0, fg="black")
txtPeso.place(x=680, y=127)

lblCidade = Label(tela, font="Arial 14", text="Cidade:", fg='#000', bg='#c0c0c0').place(x=760, y=120)
combo = ttk.Combobox(tela)
combo['values'] = ("Iguape", "Ilha Comprida", "Registro", "Juquiá", "Miracatu", "Cajati")
combo.current(2)
combo.place(x=835, y=125)

lblDataNascimento = Label(tela, font="Arial 14", text="Data de Nascimento:", fg='#000', bg='#c0c0c0').place(x=250, y=160)
txtDataNascimento = Entry(tela, width=20, borderwidth=0, fg="black")
txtDataNascimento.place(x=440, y=167)

lblDataCadastro = Label(tela, font="Arial 14", text="Data de Cadastro:", fg='#000', bg='#c0c0c0').place(x=590, y=160)
txtDataCadastro = Entry(tela, width=20, borderwidth=0, fg="black")
txtDataCadastro.place(x=755, y=167)

lblDataAtualizacao = Label(tela, font="Arial 14", text="Data de Atualização:", fg='#000', bg='#c0c0c0').place(x=250, y=200)
txtDataAtualizacao = Entry(tela, width=20, borderwidth=0, fg="black")
txtDataAtualizacao.place(x=440, y=207)

lblDescricao = Label(tela, font="Arial 14", text="Descrição:", fg='#000', bg='#c0c0c0').place(x=250, y=240)
txtDescricao = Entry(tela, width=103, borderwidth=0, fg="black")
txtDescricao.place(x=355, y=247)

foto_salvar = PhotoImage(file = r"icones\salvar.png")
foto_excluir = PhotoImage(file = r"icones\excluir.png")
foto_alterar = PhotoImage(file = r"icones\alterar.png")
foto_consultar = PhotoImage(file = r"icones\consultar.png")
foto_sair = PhotoImage(file = r"icones\sair.png")

btn_salvar =  Button(tela, text="Salvar", image= foto_salvar ,compound=TOP, command=salvar).place(x=250,y=300)  
btn_excluir = Button(tela, text="Excluir", image=foto_excluir, compound=TOP, command=excluir).place(x=305,y=300)
btn_alterar =  Button(tela, text="Alterar", image= foto_alterar ,compound= TOP, command=update).place(x=360,y=300)  
btn_consultar = Button(tela, text="Consultar", image=foto_consultar, compound=TOP, command=consultar).place(x=415,y=300)
btn_limpar = Button(tela, text="Limpar campos", image=foto_excluir, compound=TOP, command=limpar).place(x=475,y=300)
btn_sair = Button(tela, text="Sair", image=foto_sair, compound=TOP, command=sair).place(x=920,y=300)

tela.mainloop()