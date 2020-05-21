def function(x):
    return 3 * x + 1

print(function(4))
completeName = lambda firstName, Lastname: firstName.strip().title() + ' ' + Lastname.strip().title()
nome = 'arthur'

print(completeName('     arthur', 'ceRAtti'))

def duas(x, y):
    return (x+y)
print(duas(2,4))
autores = ['Porcopotamo de Nariz', 'Tartarugo da Bunda Grande', 'Gato Zé']
tres = lambda x, y, z: x + y / z
print(tres(2, 4, 2))

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)