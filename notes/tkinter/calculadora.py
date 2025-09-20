import tkinter as tk

def calcular():
    try:
        resultado = eval(entrada.get())  # cuidado: só para testes
        label.config(text=f"Resultado: {resultado}")
    except:
        label.config(text="Erro!")

janela = tk.Tk()
janela.title("Calculadora")

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text="Calcular", command=calcular)
botao.pack()

label = tk.Label(janela, text="Resultado: ")
label.pack()

janela.mainloop()
