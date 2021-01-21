#Fazer um cadastro de viagem (Deve pedir o nome do viajante, dar as opções de destino e imprimir a selecionada).

destinos = {
    'Alter do Chão'
    ,'Lençóis Maranhenses'
    ,'Chapada Diamantina'
    ,'Chapada dos Veadeiros'
    ,'Tiradentes'
    ,'Maresias'
    ,'Praia do Espelho'
    ,'Capitólio'
}

print("Bem Vindo \n Por favor informe seu nome: ")
nome = input()

print(f"Ola {nome}, escolha um dos destinos disponiveis: ", destinos)
destino_escolhido = input()

if destino_escolhido in destinos:
    print(f"Sua viagem para {destino_escolhido} foi reservada com sucesso, aproveite ao maximo!!!")
else:
    print(f"Infelizmente a viagem para {destino_escolhido} ainda não esta disponivel.")
