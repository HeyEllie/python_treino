'''A função sum() em Python calcula a soma dos elementos de um iterável, como uma lista, tupla ou conjunto.
 Ela recebe um iterável como argumento e, opcionalmente, um valor inicial para a soma. '''
'''sum(iterável, [valor_inicial])
Parâmetros:
iterável: Uma sequência (lista, tupla, etc.) ou um iterável contendo os números a serem somados.
valor_inicial (opcional): Um valor a ser adicionado à soma dos elementos do iterável. Se não for fornecido, o valor padrão é 0. '''

#Somando os elementos de uma lista:
numeros = [1, 2, 3, 4, 5]
soma = sum(numeros)
print(soma)  # Saída: 15

#Somando com um valor inicial:
numeros = [1, 2, 3, 4, 5]
soma_com_inicial = sum(numeros, 10)
print(soma_com_inicial)  # Saída: 25

#Somando os elementos de uma tupla:
numeros = (10, 20, 30)
soma = sum(numeros)
print(soma)  # Saída: 60

#Somando os elementos de um conjunto:
numeros = {1, 2, 3, 4, 5}
soma = sum(numeros)
print(soma)  # Saída: 15

#Somando strings (concatenando):
palavras = ["Olá", " ", "mundo", "!"]
resultado = sum(palavras)
print(resultado)  # Saída: Olá mundo!