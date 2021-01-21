#Fazer um sistema de Loteria (Deve pedir o nome do usuário, pedir um número e comparar com um conjunto aleatório de número (de 0 a 100) e dizer se o usuário advinhou).

import random

inicio = 0
fim = 100

loteria = list(range((inicio+1), (fim+1)))

# Para ver os valores da lista execute "print(loteria)"

numero_premiado = random.choice(loteria)

# Para ver o numero premiado execute "print(numero_premiado)"

print("Digite o seu nome: ")
nome = input()
print("Digite o numero que quer apostar!")
numero_apostado = int(input())

if numero_apostado == numero_premiado:
    print(f"Parabens {nome} você ganhou na loteria")
else:
    print(f"Infelizmente o numero premiado era {numero_premiado}!")