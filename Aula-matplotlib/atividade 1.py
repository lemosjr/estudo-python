#1. Biblioteca escolar
#Uma escola precisa controlar os livros de sua biblioteca.
#• Cada livro possui título, autor e deve ter um status (disponível ou
#emprestado).
#• O sistema deve permitir emprestar e devolver livros.
#Questão:
#Crie uma classe que represente um livro e implemente métodos para emprestar e
#devolver. Depois, crie dois livros diferentes e simule um empréstimo e uma
#devolução.

import tkinter as tk


def emprestar_livro():
    nome_livro = entrada_livro.get() 
    nome_pessoa = entrada_pessoa.get()  
    
    if nome_livro and nome_pessoa:  
        emprestimos_lista.insert(tk.END, f"{nome_livro} - {nome_pessoa}") 
        entrada_livro.delete(0, tk.END)  
        entrada_pessoa.delete(0, tk.END)  
    else:
        mensagem_erro.config(text="Por favor, preencha todos os campos.")  

janela = tk.Tk()
janela.title("Sistema de Empréstimo de Livros")
janela.geometry("400x400")

label_livro = tk.Label(janela, text="Nome do Livro:")
label_livro.pack(pady=5)

entrada_livro = tk.Entry(janela, width=30)
entrada_livro.pack(pady=5)

label_pessoa = tk.Label(janela, text="Nome da Pessoa:")
label_pessoa.pack(pady=5)

entrada_pessoa = tk.Entry(janela, width=30)
entrada_pessoa.pack(pady=5)

botao_emprestar = tk.Button(janela, text="Emprestar Livro", width=20, command=emprestar_livro)
botao_emprestar.pack(pady=10)

emprestimos_lista = tk.Listbox(janela, width=50, height=10)
emprestimos_lista.pack(pady=10)

mensagem_erro = tk.Label(janela, text="", fg="red")
mensagem_erro.pack()

def sair():
    janela.destroy()

botao_sair = tk.Button(janela, text="SAIR", width=20, command=sair)
botao_sair.pack(side=tk.BOTTOM, padx=10)

janela.mainloop()
