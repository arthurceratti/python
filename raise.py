"""
não é uma função, é uma palavra reservada assim como def ou qualquer outra em python
serve para criar nossas próprias exceções e mensagens de erro

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa se uma entre {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Arthur','azul')

o comando raise precisa ser sempre o ultimo comando do bloco, pois os comandos posteriores 
não são executados


"""

#raise ValueError('Valor Incorreto')


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa se uma entre {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Arthur','rosa')