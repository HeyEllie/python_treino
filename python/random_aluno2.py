'''O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos
dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem
sorteada'''
import random

# Lê os nomes dos quatro alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Cria uma lista com os nomes
lista_alunos = [aluno1, aluno2, aluno3, aluno4]

# Embaralha a lista. Esta é a função principal do exercício,
# que embaralha a ordem dos elementos dentro da lista_alunos, atribuindo uma ordem aleatória.
random.shuffle(lista_alunos)

# Exibe a ordem sorteada
print("\nA ordem sorteada para a apresentação dos trabalhos é:")
for aluno in lista_alunos:
    print(f"- {aluno}")