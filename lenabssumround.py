"""
Len, Abs, Sum, Round

-Len() - Retorna o tamanho (ou seja, o número de itens) de um iterável
-ABS() - Serve para fazer um módulo
-SUM() - faz a soma com um valor inicial que por default é zero 
-round() - retorna um numero arredondado com n 
           digitos de precisão (default inteiro mais próximo do valor).
"""
print('Porcopotamo de arimatéia'.__len__())
print(len('Porcopotamo de arimatéia'))

print(sum([1, 2, 3, 4]))
#para dicionarios é necessários explicitar que serão somados os valores
print(sum({'a':2, 'b':3, 'c': 4, 'd':5}.values()))

print(round(11.2))
print(round(13.33333, 2))
print(round(13.33333, 3))