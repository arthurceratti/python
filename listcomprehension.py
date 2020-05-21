nomes = ['arthur', 'tartarugo', 'gato zé']
nombres = "tartarugo de arimatéia"
print([nome.upper() for nome in nomes])

numeros = [1, 2, 3, 4, 5, 6]
pares = [numero for numero in numeros if numero % 2 ==0]
impares = [numero for numero in numeros if numero % 2 !=0]
print(pares)
print(impares)
pares = [numero for numero in numeros if not numero % 2]
#print(pares) 
lista = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
#print(lista[0])

"""for componente in lista:
    for elemento in componente:
        print(elemento)
"""
#[[print(elemento) for elemento in componente] for componente in lista]

[[print(elemento) for elemento in range(1, 4)] for componente in range (1, 4)]