'''
Diferente de listas, tuplas nao permitem que voce troque o valor, somente onde ela foi criada.
Tupla obrigatoriamente usam parenteses() ao inves de Colchetes na lista[].
TypeError: 'tuple' object does not support item assignment//nao permite a troca de valor do item.
'''
teste = 123

tuple = ( teste, 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print(tuple)               # Prints the complete tuple
print(tuple[0])            # Prints first element of the tuple
print(tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print(tuple[2:])           # Prints elements of the tuple starting from 3rd element
print(tinytuple * 2)       # Prints the contents of the tuple twice
print(tuple + tinytuple)   # Prints concatenated tuples


tuple[0] = "hahaha"
#Aqui ao executar essa linha 19, o terminal retornara o erro citado nos comentarios iniciais