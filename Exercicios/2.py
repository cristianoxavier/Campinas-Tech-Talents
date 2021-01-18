#Algoritmo para ir ao banco para sacar dinheiro (Imprimir a sequência para ir ao banco e sacar dinheiro)

print("Você gostaria de sacar dinheiro?")

sacar = input("Digite sim ou não. ")

if  sacar == "sim":
    print("Quanto deseja sacar?")
    saque = input("Digite o valor que deseja sacar. ")
    print(f"Saque de {saque} reais realizado com sucesso!")

else:
    print("Operação finalizada")