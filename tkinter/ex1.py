'''
Um programa Tkinter geralmente segue esta estrutura básica:
    Importar o Módulo Tkinter: Importe o módulo Tkinter no seu programa usando a declaração import tkinter as tk.
    Criar uma Janela: Crie uma janela principal usando Tk().
    Criar Componentes Gráficos: Adicione botões, caixas de entrada, rótulos e outros componentes à janela.
    Organizar os Componentes: Use gerenciadores de layout como grid(), pack() ou place() para organizar os componentes dentro da janela.
    Executar o Loop Principal: Chame o método mainloop() da janela para iniciar o loop principal do programa Tkinter. '''

#Exemplo 1: Criando uma Janela Simples

import tkinter as tk

# Criar uma janela
janela = tk.Tk()
janela.title("Minha Primeira Janela")

# Executar o loop principal
janela.mainloop() 

