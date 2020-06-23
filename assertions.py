"""
Assertions(Checagem/Questionamentos) - Afirmações

'assert' é uma expressão utilizada quando queremos checar uma expressão, quando a expressão
é correta retorna "none" quando é errada retorna erro do tipo AssertionError

OBS1> É possivel especificar um segundo argumento ou inclusive uma mensagem de erro personalizada
OBS2> A palavra pode ser utilizada em qualquer função ou código (não presica ser só no modo teste)

def soma_numero_positivos(a, b):
    assert a > 0 and b > 0, 'ambos números precisam ser positivos'
    return a + b


ret = soma_numero_positivos(-1,4)
print(ret)

#resultado:

n38-32/python.exe "c:/Users/Arthur/Documents/Arthur Denicol Ceratti/python/assertions.py"
Traceback (most recent call last):
  File "c:/Users/Arthur/Documents/Arthur Denicol Ceratti/python/assertions.py", line 25, in <module>
    ret = soma_numero_positivos(-1,4)
  File "c:/Users/Arthur/Documents/Arthur Denicol Ceratti/python/assertions.py", line 21, in soma_numero_positivos
    assert a > 0 and b > 0, 'ambos números precisam ser positivos'
AssertionError: ambos números precisam ser positivos

OBS> Cuida ao utilizar assert
- Se um programa Python com o parâmetro -O for executado nenhum assertion será validado
ou seja, todas as suas validações seram ignoradas.

"""

def soma_numero_positivos(a, b):
    assert a > 0 and b > 0, 'ambos números precisam ser positivos'
    return a + b


ret = soma_numero_positivos(-1,4)
print(ret)