list = ['physics', 'chemistry', 1997, 2000]
print("Value available at index 2 : ")
print(list[2])
list[2] = 2001
print("New value available at index 2 : ")
print(list[2])


#o .append() adiciona 1 elemento no final da lista.
#ele so recebe 1 argumento. 
list.append("hahaha")
print(list)

#tambem é possivel adicionar lista dentro de lista.
list.append(["jajaja", 1234])
print(list)
