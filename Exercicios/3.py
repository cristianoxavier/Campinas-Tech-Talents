#Algoritmo para trocar o pneu do carro (Imprimir a sequência para trocar o pneu do carro).

print("Bem vindo, você gostaria de trocar o pneu do carro?")

trocar = input("Sim? ou Não?: ")

if trocar == "Sim" or "sim":
    print("Qual dos pneus quer trocar?")
    escolha1 = input("Os da frente? ou os de tras?: ")
    if escolha1 == "frente" or escolha1 == "tras":
        print("O da esquerda ou da direita?: ")
        escolha2 = input("Esquerda ou Direita?: ")
        if escolha2 == "esquerda" or escolha2 == "direita":
            print(f"Pneu da {escolha2} trocado com sucesso!")
        
else:
    print("Obrigado! Operação Finalizada.")