#Exemplo 4: Utilizando o método grid()

'''
O método grid() é um dos gerenciadores de layout disponíveis na biblioteca Tkinter, posicionando os widgets em uma janela. Ele organiza os widgets em uma grade,
 onde cada widget é colocado em uma célula específica da grade, identificada por uma linha e uma coluna.
Especificar a posição do widget:
    Para posicionar um widget usando grid(), você precisa especificar em qual linha e coluna da grade ele deve ser colocado. Isso é feito passando 
    os argumentos row e column para o método grid().

Espaçamento interno:
    Os argumentos padx e pady no método grid() permitem especificar o espaçamento interno em x e y, respectivamente, ao redor do widget.

Redimensionamento do widget:
    Por padrão, os widgets se ajustam automaticamente ao seu conteúdo. No entanto, você pode controlar o redimensionamento de um widget usando os argumentos 
    sticky, columnspan e rowspan no método grid():
    O argumento sticky controla a direção na qual o widget se expande para preencher o espaço da célula. Por exemplo, sticky="w" expande o widget para 
    preencher a célula na direção oeste (esquerda).
    O argumento columnspan permite que o widget se estenda por várias colunas.
    O argumento rowspan permite que o widget se estenda por várias linhas.

Ordenação de widgets:

    A ordem na qual os widgets são colocados no método grid() determina a ordem de sobreposição. Widgets colocados posteriormente podem cobrir 
     colocados anteriormente.
Usar o grid() pode ser um pouco mais complexo em comparação com pack(), mas oferece mais controle sobre o posicionamento dos widgets em uma janela. 
É uma escolha popular para layouts mais complexos e precisos em aplicações Tkinter.'''

import tkinter as tk

# Função para exibir uma mensagem quando o botão for clicado
def exibir_mensagem():
  print("O botão foi clicado!")

# Criar uma janela
janela = tk.Tk()
janela.title("Posicionamento com Grid")

# Adicionar um rótulo
rotulo = tk.Label(janela, text="Olá, Tkinter!")
rotulo.grid(row=0, column=0, padx=10, pady=10)  # Posicionado na primeira linha e primeira coluna

# Adicionar um botão
botao = tk.Button(janela, text="Clique Aqui", command=exibir_mensagem)
botao.grid(row=1, column=0, padx=10, pady=10)  # Posicionado na segunda linha e primeira coluna

# Executar o loop principal
janela.mainloop()

