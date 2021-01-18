dict_celulares = {
    "modelo": "Galaxy S20",
    "Fabricante": "Samsung",
    "Preço": "R$ 3100.00"
}


# print(len(dict_celulares)) #Quantidade de elementos(chave:valor) do dicionário.

# print(str(dict_celulares)) #Converte para string o dicionário inteiro.

# print(type(dict_celulares)) #Mostra o tipo de dado do dicionário. 

# dict_celulares.clear() #Apaga os elementos(chave:valor) dentro do dicionário.
# print(str(dict_celulares))

# new_dict = dict_celulares.copy() #Cópia do dicionário para outra variável
# print(new_dict)

# #Criar um dicionario somente com as chaves, os valores vao ser None.
# seq = ('Modelo', 'Fabricante', 'Preço')
# new1_seq = dict.fromkeys(seq)
# print(new1_seq)

#Realiza a busca da chave.
print(dict_celulares.get("Modelo"))

 #Exporta uma lista com Chaves e Valores no formato Tupla
# print(dict_celulares.items())
# # #Dicionarios de chaves e valores
# print(dict_celulares.keys())
# print(dict_celulares.values())