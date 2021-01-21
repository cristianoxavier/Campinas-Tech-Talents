#Elabore um algoritmo em Python que receba um número inteiro e escreva na tela o número fornecido, o antecessor desse número e o sucessor desse número;

print("Bem vindo! \n Informe o um numero")

numero_informado = int(input())

antecessor = numero_informado - 1
sucessor = numero_informado + 1

print(f"O numero informado é: {numero_informado}")
print(f"Seu sucessor é : {sucessor}")
print(f"E o seu antecessor é : {antecessor}")