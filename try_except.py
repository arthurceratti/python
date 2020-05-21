"""
Utilizamos o bloco try except para tratar erros que podem ocorrer no nosso codigo, 
previnindo assim que o programa pare de funcionar e o usuario receba mensagens de erro inesperadas
"try" - primeiro o programa tenta fazer uma determinada ação, caso não consiga "except"- faça isso

exemplo:
o progrma ira tentar executar a função "geek()" e caso não consiga, ao invés de dar erro
irá executar a função "print()"
try:
    geek()
except:
    print('deu um problema aqui')
o exemplo acima apresenta o comportamento frente à um erro genérico
-----------------------------------------------------------------------------------
para erros especificos:
try:
    geek()
except NameError:
    print('voce esta tentando utilizar uma função inexistente')

desta vez serão tratados apenas erros do tipo NameError
-----------------------------------------------------------------------------------
try:
    geek()
except NameError as err:
    print(f'voce esta tentando utilizar uma função inexistente, do tipo {err}')

    Podem ser inseridos diversos "excepts" para cada erro de uma vez
"""

try:
    geek()
except NameError as err:
    print(f'voce esta tentando utilizar uma função inexistente, do tipo {err}')

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None

dic = {"nome":"geek"}
print(pega_valor(dic,"zezo"))