nome_user = input("Olá! Por favor insira o nome do usuário por favor.\n") #Pergunte pelo nome do usuário
lista_agendamentos =[] #Cria uma lista de agendamentos vazia para começar o programa
lista_opcoes = ["","1 -) Listar Agendamentos", "2 -) Excluir um agendamento", "3 -) Inserir um Agendamento", "4 -) Sair"] #Cria uma lista de opções para o usuário ver na tela
while True: #Loop infinito para manter o programa e as variáveis vivos
    print(f"Olá {nome_user}, selecione uma das opções abaixo:") #Dá as boas vindas ao usuário
    for opcao in lista_opcoes: #Lista as opções na tela do usuário
        print(opcao) #Imprime as opções
    opcao_selecionada = int(input("")) #Aguarda para receber um valor do usuário (Pode ter um tratamento aqui)
    if opcao_selecionada == 1: #Se a opção selecionada for a 1, então liste os agendamentos existentes
        print(lista_agendamentos) #Imprima os agendamentos existentes na lista
    elif opcao_selecionada == 2: #Se a opção selecionada for a 2, então prepare para excluir um agendamento
        while True: #Loop infinito para navegar nas "Telas" de exclusão
            indice = 0 #Índice para controlar as opções de exclusão
            for item in lista_agendamentos: #Lista dos agendamentos
                print(f"{indice} - {item}") #Imprime os Agendamentos com os seus respectivos índices
                indice += 1 #Incrementa os índices
            print(f"Selecione {indice} para sair...") #Dá a opção para o usuário sair desta tela de exclusão
            opcao_delecao = input("Qual desses items você deseja excluir? (Selecione um número) \n") #Pergunte para o usuário qual é o item que ele deseja excluir, dado o índice
            if opcao_delecao.isnumeric(): #Verifica se o índice é numérico
                opcao_delecao_convertida = int(opcao_delecao) #caso seja um índice numérico, então converta para inteiro
                if opcao_delecao_convertida in range(0, indice): #Verifica se o número convertido está no range da lista
                    print("Apagando...") #Avise ao usuário que está apagando
                    item_selecionado = lista_agendamentos.pop(opcao_delecao_convertida) #Apague o item (Dado o seu índice) e extraia o item excluído
                    print(f"Seu item {item_selecionado} foi removido!") #Avise para o usuário que o item foi excluído
                    break #Saia da tela fazendo o comando break para sair do loop
                elif opcao_delecao_convertida == indice: #Se o usuário selecionou o último indice (ou indice extra), então saia da tela de excluir
                    break #Saia da tela fazendo o comando break para sair do loop
                else: #Senão, se o usuário digitou algum índice numérico que não exista, então mostre que não há essa opção
                    print("Não existe essa opção!") #Mostre para o usuário que não há essa opção
            else: #Senão, se o usuário digitou algo não numérico, então avise que a opção está incorreta
                print("Opção incorreta ou inexistente!") #Mostre para o usuário que essa opção não existe
​
    elif opcao_selecionada ==3: #Se o usuário optou por inserir então, vamos inserir um novo registro
        nome_cliente = input("Insira o nome do cliente\n") #Campo para inserir o nome do cliente no dicionário
        veiculo_cliente = input("Insira o veículo do cliente\n") #Campo para inserir o veículo do cliente no dicionário
        dicionario_veiculo = {"nome_cliente":nome_cliente,"veiculo_cliente":veiculo_cliente} #Criando um dicionário com os dados acima
        lista_agendamentos.append(dicionario_veiculo) #Inserindo o dicionário na lista (Escopo Global)
        print("Cliente inserido") #Avise para o usuário que o agendamento foi inserido
    elif opcao_selecionada == 4: #Se o usuário selecionar a opção 4, então saia do sistema
        print("Você saiu do sistema!") #Avise para o usuário que ele saiu do sistema
        break #Saia do sistema fazendo o comando break para sair do loop infinito
    elif opcao_selecionada not in(1,2,3,4): #Se o usuário não selecionou nenhuma das opções existentes então avise que não existe a opção
        print("Opção errada ou inexistente!") #Mostre para o usuário que a opção não existe