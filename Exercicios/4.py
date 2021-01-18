#Elabore um algoritmo em Python que leia, calcule e escreva a média aritmética entre quatro números;

print("Digite o primeiro numero")
num_1 = int(input())

print("Digite o segundo numero")
num_2 = int(input())

print("Digite o terceiro numero")
num_3 = int(input())

print("Digite o quarto numero")
num_4 = int(input())

print(num_1, num_2, num_3, num_4)

media = (num_1 + num_2 + num_3 + num_4) / 4
print("A media aritmética é: ", media)