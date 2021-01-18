dict_compras = {"Nome":"Secador de cabelo","Preço":"R$ 1000,00", "Tamanho":"Médio"}

print(dict_compras)
# #Excluí todos os elementos mas não excluí o dicionario da memória
# dict_compras.clear()
# print(dict_compras)
# #Exclui o dicionário da memória
# del dict_compras
# print(dict_compras)
# #Excluí um elemento do dicionário
del dict_compras["Nome"]
print(dict_compras)
