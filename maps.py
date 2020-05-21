# MAP serve para mapeamento de valores para funções

import math

def area(r):
    #calcula a área de um circulo com raio R
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

radio = [2, 3, 5, 7.1, 0.3, 4]

#forma tosca
areas = []
for r in radio:
    areas.append(area(r))
print(areas)

# forma como MAP - map recebe dois valores, uma função e um iteravel
areas = map(area, radio)
print(list(areas))

# normalmente a entrada é uma expressão tipo lambda
# no caso abaixo o resultado é transformado numa lista, mas poderia ser qualquer outro tipo
print(list(map(lambda r: math.pi * (r ** 2), radio)))
# depois de utilizar o resultado da função MAP a variavel é zerada (os valores são apagados)
# este funcionamento garante a limpeza da memória pós utilização

