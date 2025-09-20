''' Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um
programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.'''
import random

al1 = input("Informe o nome do aluno 1: ")
al2 = input("Informe o nome do aluno 2: ")
al3 = input("Informe o nome do aluno 3: ")
al4 = input("Informe o nome do aluno 4: ")
lista_alunos = [al1, al2, al3, al4]

print("O aluno sorteado foi:")
print(random.choice(lista_alunos))
 