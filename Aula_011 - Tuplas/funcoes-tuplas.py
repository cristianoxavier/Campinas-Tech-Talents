tup1 = (1, 2, 3, 4, 5, 9)
tup2 = (6, 7, 8, 9, 10, 5)
lista = ["hahaha", "jajaja", "kkkk"]

print(len(tup1)) #Imprime a quantidade de elementos da tupla.

print(max(tup2)) #Imprime o maior valor dentre os elementos da tupla.

print(min(tup1)) #Imprime o menor valor dentre os elementos da tupla.

print(type(tuple(lista))) #Converte uma lista para tupla.


print(set(tup1) & set(tup2)) #Pegando os valores em comum