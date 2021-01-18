#Tuplas são imutaveis, mas existe uma forma alternativa de mudarmos isso (famosa gambiarra)

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Nõ é possivel adicionar um item na tupla conforme abaixo.
# tup1[0] = 100

# Então a gambiarra é, criarmos uma nova tupla.
tup3 = tup1 + tup2
print(tup3)
