#Fazer um sistema de Agenda de revisão do Carro (Deve pedir o nome do carro, ano e modelo, nome do proprietário, data e hora da revisão. Depois deve guardar os dados em um dicionário e mostrar a lista de dicionários (agendamentos) na tela).

usuario = input("Olá! Insira o seu nome por favor. \n")
agendados = []
menu_principal = ["", "1 - Verificar Agendados", "2 - Adicionar revisão", "3 - Remover revisão", "4 - Sair"]

print(f"Ola {usuario}, bem vindo! \n O que deseja fazer?")
while True:
    for opcao in menu_principal: #loop para mostrar todas as opções do menu.
        print(opcao)
    opcao_escolhida = int(input("")) #Escolha da opção
    if opcao_escolhida == 1: #Visualizar todos agendamentos
        for tem_revisao in agendados:
            print(tem_revisao)
    elif opcao_escolhida == 2:
        #adicionar
        nome_do_carro = input("Insira o nome do proprietario do veiculo \n")
        modelo_do_carro = input("Insira o modelo do veiculo \n")
        ano_do_carro = input("Insira o ano do veiculo \n")
        data_agendamento = input("Insira a data que pretende agendar \n")
        hora_agendamento = input("Insira o horario que quer agendar \n")
        reserva = {'Proprietario': nome_do_carro, 'Modelo': modelo_do_carro, 'Ano': ano_do_carro, 'Data': data_agendamento, 'Hora': hora_agendamento}
        agendados.append(reserva)
    elif opcao_escolhida == 3:
        #Remover
        indice = 0
        for reservado in agendados:
            print(f"{indice} - {reservado}")
            indice += 1
        print(f"Selecione {indice} para sair...")
        opcao_escolhida_delecao = input("Qual desses items você deseja excluir? (Selecione um número) \n")
        if opcao_escolhida_delecao.isnumeric():
            opcao_delecao_convertida = int(opcao_escolhida_delecao)
            if opcao_delecao_convertida in range(0, indice):
                print("Deletando...")
                reserva_desfeita = agendados.pop(opcao_delecao_convertida)
                print(f"A reserva {reserva_desfeita} \n foi desfeita com sucesso!")
            elif opcao_escolhida_delecao == indice:
                print("Saindo do menu de remoção de revisões")
                break
            else:
                print("Opção nao existe! Por favor insira uma opção existente.")
        else:
            print("Opção incorreta!")
    elif opcao_escolhida == 4: 
        print(f"Fechando menu de revisão \n Até mais {usuario}")
        break
    elif opcao_escolhida not in(1,2,3,4): 
        print(f" {usuario}, a opção esta errada ou é inexistente! \n Insira uma das opções abaixo.")