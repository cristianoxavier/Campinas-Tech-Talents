# Fazer um sistema de Agenda de contatos (Deve criar um dicionário com Nome, Telefone e Endereço, Imprimir os dados do dicionário, ser capaz de inserir e excluir um contato)
usuario = input("Ola! Bem vindo a sua agenda, por favor insira o seu nome: \n") #Inserir o nome do dono da Agenda
agenda = [] #Agenda vazia
opcoes_agenda = ["", "1 - Ver agenda", "2 - Adicionar Contatos", "3 - Remover Contato", "4 - Fechar agenda"] #Menu de opções iniciais

while True: # While para rodar o programa
    print(f"Ola {usuario}, o que deseja fazer?") #Mensagem de boas vindas e primeira escolha de opções
    for opcao in opcoes_agenda: #loop para mostrar todas as opções da agenda.
        print(opcao)
    opcao_escolhida = int(input("")) #Escolha da opção

    if opcao_escolhida == 1: #Se a opção for 1, ira mostrar a agenda completa
        print(agenda)
    elif opcao_escolhida == 2: #Se a opção for 2 ira adicionar 1 contato na agenda
        nomeContato = input(f"{usuario}, insira o nome do contato que quer adicionar: \n") #nome do contato que pretende adicionar
        telefoneContato = input(f"{usuario}, insira o telefone do contato que quer adicionar: \n") #telefone do contato que pretende adicionar
        enderecoContato = input(f"{usuario}, insira o endereço do contato que quer adicionar: \n") #endereço do contato que pretende adicionar
        contatoAdicionado = {'Nome':nomeContato, 'Telefone': telefoneContato, 'Endereço': enderecoContato} #adicionando as informaçoes em um novo dicionario para inserir na agenda
        agenda.append(contatoAdicionado) #realizando inserção na agenda.
    elif opcao_escolhida == 3: #se a opção for 3, ira remover 1 contato da agenda
        indice = 0
        for item in agenda: # loop para passar por todos os contatos ja cadastrados na agenda.
            print(f"{indice} - {item}")
            indice += 1 #Incremento para dar opções
        print(f"Selecione {indice} para sair..") #Depois de sair do For, a ultima opção do indice sera a opção de sair das opções de deleção
        opcao_delecao = input("Qual desses items você deseja excluir? (Selecione um número) \n")
        if opcao_delecao.isnumeric(): #Verifica se a opção selecionada é numerica
            opcao_delecao_convertida = int(opcao_delecao) #Se sim, ele converte para INT
            if opcao_delecao_convertida in range(0, indice):
                print(f"Apagando {opcao_delecao_convertida}")
                item_selecionado = agenda.pop(opcao_delecao_convertida)
                print(f"O item {item_selecionado} \n foi apagado com sucesso!")
                break
            elif opcao_delecao_convertida == indice:
                break #Sai do menu de remoção de contatos da agenda
            else:
                print("Opção nao existente! Por favor insira uma opção existente.")
        else:
            print("Opção incorreta!")
    elif opcao_escolhida == 4: 
        print(f"Fechando Agenda \n Até mais {usuario}")
        break
    elif opcao_escolhida not in(1,2,3,4): 
        print(f" {usuario}, a opção esta errada ou é inexistente! \n Insira uma das opções abaixo.")