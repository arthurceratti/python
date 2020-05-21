"""
Try / Except / Else / Finally
Dica de quando e onde tratar código:
TODA POSSIBILIDADE DE ENTRADA DE DADO DEVE SER TRATADA

Se no caso abaixo for digitada uma letra haverá erro de tipo de dado
num = int(input("Informe um numero:  "))
print(f'Voce digitou {num}')
------------------------------------------------------------------------
no caso abaixo caso não venha a ser digitado um numero ocorrerá um ValueError

num = 0
try:
    num = int(input("Informe um numero:  "))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Voce digitou {num}')
-------------------------------------------------------------------------
o bloco finally sempre é executado, ese bloco geralmente é utilizado para fechar
ou desalocar recursos (fechar banco de dados, arquivos para leitura ou escrita e similares).

-------------------------------------------------------------------------
"""
num = 0
try:
    num = int(input("Informe um numero:  "))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Voce digitou {num}')