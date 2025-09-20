''' Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um
programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.'''
import random
lista_aluno = ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4']
print(random.choice(lista_aluno))