lista = [1, 2, 3, 8, 34, 129]
print(max(lista))

dicionario = {'a': 1, 'b': 2, 'c':34,'d': 23}
# se for simplesmente passado o dicionário, será avaliada a maior chave. 
# Caso se queira o maior valor, deverá ser utilizado em conjunto o valor value.
print(max(dicionario))
print(max(dicionario.values()))

#exemplo de programa onde usuário passa dois valores e o programa aponta 
# o maior entre os dois
"""
val1 = int(input('Informe o primeiro valor:  '))
val2 = int(input('Informe o segundo valor:  '))
print(max(val1, val2))
print(f'O maior valor é {max(val1, val2)}')
"""
#exemplo de programa onde usuário passa dois valores e o programa aponta 
# o menor entre os dois
"""
val1 = int(input('Informe o primeiro valor:  '))
val2 = int(input('Informe o segundo valor:  '))
print(min(val1, val2))
print(f'O menor valor é {min(val1, val2)}')
"""
nomes = ['Zezo', 'José', 'Tartarugo', 'Gato Zé', 'Porconhento']
#neste caso será apresentado o "maior" nome entre aqueles que fazem parte da lista
print(max(nomes, key=lambda nome: len(nome)))


musicas = [
        {"titulo": "black in black", "tocou": 3},
        {"titulo": "adocica", "tocou": 4},
        {"titulo": "skank", "tocou": 21},
        {"titulo": "Elis Regina", "tocou": 43},
        {"titulo": "Carnavalito", "tocou": 21},
        {"titulo": "Kiss", "tocou": 1}
]

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
