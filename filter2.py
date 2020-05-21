
users = [
    {"username": "Samuel", "tweets": ["Ratunabatata"]},
    {"username": "Manuel", "tweets": []},
    {"username": "Ariel", "tweets": ["Pipoca"]},
    {"username": "Ezequiel", "tweets": ["Gata"]},
    {"username": "Rafael", "tweets": []},
    {"username": "Mizael", "tweets": ["Chumbawanba"]}
]
# determinação de usuarios inativos
#inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, users))
#print(inativos)

inativos = list(filter(lambda usuario: not usuario['tweets'], users))
print(inativos)