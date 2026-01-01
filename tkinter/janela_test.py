import tkinter as tk
janela = tk.Tk()
janela.title("Janela teste")

def mensagem():
    print("Você clicou no botão! Congratulations!")

def mensagem_botao():
    print("Resultado: Parabéns!!!")

botao = tk.Button(janela, text="Clique aqui little one", command=mensagem)
botao.grid(row=1, column=0, padx=100, pady=100)  # Posicionado na segunda linha e primeira coluna

botaoo = tk.Button(janela, text="Clicou!!!", command=mensagem_botao)


janela.mainloop()