dictionary = {'bixinho': 'gato', 'carro': 'versa', 'tartarugo': 'zezo'}
print(dictionary["carro"])

keys = 'abcdef'
values = [1, 2, 3, 4, 5, 6]
dictiona = {keys[i]: values[i] for i in range(0, len(keys))}
print(dictiona)