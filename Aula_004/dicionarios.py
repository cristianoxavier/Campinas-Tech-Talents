'''
Dicionario é mais proximo do JSON.
Dicionarios recebem valores sensiveis, devem se respeitar os tipos de dados(string, int, float, boolean...)
São definidas chaves e valores. 
    Ex:
    dict = {'Keys': 'value', key: value, key: true or false}

'''

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print(dict['one'])       # Prints value for 'one' key
print(dict[2])           # Prints value for 2 key
print(tinydict)          # Prints complete dictionary
print(tinydict.keys())   # Prints all the keys
print(tinydict.values()) # Prints all the values



parametros = {'nome': 'Cristiano',
            'codigo':6734,
            'departamento': 'Tecnologia',
            'ativo': True
            }

print(parametros)