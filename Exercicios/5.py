#Algoritmo para calcular a média do aluno (Deve colocar o nome do aluno, colocar 4 notas e imprimir sua média)

print("Calcular media!")
print("Informe a sua nota no primeiro Bimestre!")
nota1 = int(input())

print("Informe a sua nota no segundo Bimestre!")
nota2 = int(input())

print("Informe a sua nota no terceiro Bimestre!")
nota3 = int(input())

print("Informe a sua nota no quarto Bimestre!")
nota4 = int(input())

print("Suas notas foram:")
print("Primeiro Bimestre: ", nota1)
print("Segundo Bimestre: ", nota2)
print("Terceiro Bimestre: ", nota3)
print("Quarto Bimestre: ", nota4)

media = (nota1 + nota2 + nota3 + nota4) / 4

print("Sua media é de: ", media)