list1 = ['physics', 'chemistry', 1997, 2000]
print(list1)

#del é utilizado para deletar.
del list1[2]
print("After deleting value at index 2 : ")
print(list1)

#ele recebe mais de um parametro por vez, ou seja, pode deletar mais de 1 item por vez.

list1.append(1997)# adicionando um elemento
print(list1)
list1.append(2020)# adicionando um elemento
print(list1)

del list1[1], list1[2] #removendo mais de 1 elemento por vez.

print("After deleting 2 values : ")
print(list1)