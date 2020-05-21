"""
Não confunda com a função reverse() que foi estudada nas listas
A função reverse só funciona nas listas
A função reversed funciona com qualquer interavel, responsavel por inverter o iteravel
a função reversed retorna um iterável chamado list reverse iterator



"""
lista =[1, 2, 3, 4, 5]
res = reversed(lista)
print(res)
print(type(res))
print(list(reversed(lista)))
# não é possivel definir ordem para conjuntos (SET), o restante pode ser trabalhado
strings = "Tartarugo Cabeçudo"
strings2 = reversed(strings)
print(list(strings2))

for letra in reversed(strings):
    print(letra, end='')
print('\n')
print(''.join(list(reversed(strings))))
