"""
ZIP
zip() - cria um iteravel, chamado zip object que agrega elementos de cada um dos iteraveis
passado como entradas em pares.
o comando ZIP utiliza como parâmetro o menor tamanho de listas, tuplas e etc...
entre os valores inseridos.

Podem ser utilizados diferentes iteraveis com o zip, tuplas, listas, dicionários, sets e etc..

"""
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
print(zip1)
#<zip object at 0x027DDF68>
print(type(zip1))
# <class 'zip'>
print(list(zip1))
# resposta = [(1, 4), (2, 5), (3, 6)]
print(dict(zip(lista1, lista2)))

dados = [(0,1),(2,3),(4,5),(6,7)]
print(list(zip(*dados))) # * serve para fazer o desempacotamento dos dados, assim o zip
# consegure fornecer a seguinte saída [(0, 2, 4, 6), (1, 3, 5, 7)]

