#Se houver 2 chaves iguais, a última é a que prevalece
# dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni', 'Name': 'Jeff'}
# print("dict['Name']: ", dict['Name'])

#Não é permitido a inserção de uma lista na chave do dicionário
# dict = {['Name']: 'Zara', 'Age': 7}
# print("dict['Name']: ", dict['Name'])
# Com a tupla você consegue adicionar um nome com 2 ou mais itens
dict = {('Name','haha'): 'Zara', 'Age': 7}
print("dict[('Name','haha')]: ", dict[('Name','haha')])
