# serve para filtrar dados de uma determinada coleção
import statistics
values = 1, 2, 3, 4, 5, 6
media = (sum(values) / len(values))
print(media)

# calculando média dos dados usando função mean
media = statistics.mean(values)
print (media)
# no exemplo abaixo para cada valor X em dado será realizada uma comparação com a média para
# imprimir só aquilo que está acima dela
res = filter(lambda x: x > media, values)
print(list(res))
# após o valor ser utilizado uma primeira vez ele é eliminado da memória
print(list(res))
value = 5
value > media
# comando filter sendo usado para remover espaços em branco de uma lista de paises
countries = ['', 'Brasil', 'Argentina', '', 'Colombia', '', 'Equador', '']
print(countries)
res = filter(None, countries)
print (list(res))
res = filter(lambda pais: pais != '', countries)
print(list(res))