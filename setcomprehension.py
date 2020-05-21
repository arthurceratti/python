
numeros = {num for num in range(1, 7)}
print(numeros)
#conjuntos não mantem ordenação e não recebem valores repetidos
numeros = {x ** 2 for x in range(10)}
print(numeros)
#listas mantem ordenação e não existem problemas em ter valores repetidos
numbers = [x ** 2 for x in range(10)]
print(numbers)