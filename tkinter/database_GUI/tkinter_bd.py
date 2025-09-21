import sqlite3
import tkinter as tk
from tkinter import messagebox

def salvar():
    nome = entry_nome.get()
    idade = int(entry_idade.get())
    sexo = entry_sexo.get()

    try:
        idade_int = int(idade)
    except ValueError:
        messagebox.showerror("Erro", "Idade deve ser um número inteiro")
    return

    if nome and idade and sexo:
        conn = sqlite3.connect("meuBanco.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pessoas (nome, idade, sexo) VALUES" (nome, idade, sexo))
        conn.commit() #Salva a transação (persiste a inserção no arquivo).
        conn.close() #Fecha a conexão com o banco.
        messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
        entry_nome.delete(0, tk.END) #Limpa o campo entry_nome. 0 é o índice inicial do texto e tk.END indica até o fim. Após isso o campo fica vazio.
        entry_idade.delete(0, tk.END)
        entry_sexo.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")

#criando a janela
janela = tk.Tk()
janela.title("Insterface com banco de dados. Databse GUI")

tk.Label(janela, text="Nome: ").grid(row=0, column=0)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text="Idade: ").grid(row=1, column=0)
entry_idade = tk.Entry(janela)
entry_idade.grid(row=1, column=1)

tk.Label(janela, text="Sexo: ").grid(row=2, column=0)
entry_sexo = tk.Entry(janela)
entry_sexo.grid(row=2, column=1)

button = tk.Button(janela, text="Salvar", command=salvar)
button.grid(row=3, column=0, columnspan=2)

janela.mainloop()