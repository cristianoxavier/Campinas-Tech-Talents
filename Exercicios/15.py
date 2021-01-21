# Fazer um sistema de Feira Livre(Deve imprimir uma lista com as frutas e pedir para o solicitante colocar o nome e selecionar a fruta e depois deve imprimir o nome do solicitante e a fruta).


frutas = {
    "Banana"
    ,"Maça" 
    ,"Tomate"
    ,"Melancia"
    ,"Uva"
    ,"Ameixa"
    ,"Pera"
    ,"Goiaba"
    ,"Acerola"
    ,"Melão"
}

print("Bem vindo a nossa feira! \n Por favor informe o seu nome: ")
nome = input()

print(f"Ola {nome}, seja bem vindo! \n Hoje temos essas frutas disponiveis {frutas} \n Qual fruta deseja comprar: ")
reserva = input()

if reserva in frutas:
    print(f"{nome} a fruta selecionada foi {reserva}, desejamos uma otima alimentação! \n Volte Sempre")
else:
    print(f"{nome}, Infelizmente a fruta {reserva}, não esta mais disponivel")