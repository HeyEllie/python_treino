import tkinter as tk 
from tkinter import filedialog
from tkinter import *

def novo():
    text_area.delete(1.0, tk.END)

def abrir():
    arquivo = filedialog.askopenfilename(defaultextension=".txt",
                                         filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")])
    if arquivo:
        with open(arquivo, "r", encoding="utf-8") as f:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f.read())

def salvar():
    arquivo = filedialog.asksaveasfilename(defaultextension=".txt",
                                           filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")])
    if arquivo:
        with open(arquivo, "w", encoding="utf-8") as f:
            f.write(text_area.get(1.0, tk.END))

# Criar janela
janela = tk.Tk()
janela.title("Bloco de Notas em Python")

# Área de texto
text_area = tk.Text(janela, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both")

# Menu
menu = tk.Menu(janela)
janela.config(menu=menu)

#scrollbar test
import tkinter as tk

# Janela principal
root = tk.Tk()
root.title("Bloco de Notas com Scrollbar")

# Cria um Frame para organizar melhor
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Cria a área de texto
texto = tk.Text(frame, wrap="word")
texto.pack(side="left", fill="both", expand=True)

# Cria a barra de rolagem
scrollbar = tk.Scrollbar(frame, command=texto.yview)
scrollbar.pack(side="right", fill="y")

# Conecta o Text à Scrollbar
texto.config(yscrollcommand=scrollbar.set)

# Coloca bastante texto só para testar
for i in range(100):
    texto.insert("end","{i+1}\n")
"""testando a srcollbar ainda em"""
root.mainloop()


arquivo_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Arquivo", menu=arquivo_menu)
arquivo_menu.add_command(label="Novo", command=novo)
arquivo_menu.add_command(label="Abrir", command=abrir)
arquivo_menu.add_command(label="Salvar", command=salvar)
arquivo_menu.add_separator()
arquivo_menu.add_command(label="Sair", command=janela.quit)

janela.mainloop()
