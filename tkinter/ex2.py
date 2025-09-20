# Exemplo 2: Adicionando um Rótulo

import tkinter as tk

# Criar uma janela
janela = tk.Tk()
janela.title("Rótulo Simples")

# Adicionar um rótulo
rotulo = tk.Label(janela, text="Olá, Tkinter!")
rotulo.pack()

# Executar o loop principal
janela.mainloop()

