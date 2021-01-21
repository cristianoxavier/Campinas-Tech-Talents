#Fazer um sistema de compras (Deve mostrar um dicionário com os objetos (Nome, Preço e Cor), pedir o nome do usuário e fazer com o que o usuário selecione um objeto e imprimir a compra na tela).


compras = []
usuario = input("Bem vindo, por favor insira o seu nome: \n")
menu_principal = ["", "1 - Ver lista de compras", "2 - Adicionar produtos", "3 - Remover produtos", "4 - Fechar lista"]

while True: #Loop infinito para mostrar o menu da lista de compras
    print(f"{usuario}, o que deseja fazer?")
    for menu in menu_principal:
        print(menu)
    escolha_menu = int(input(""))
    if escolha_menu == 1:
        for produto in compras:
            print(produto)
    elif escolha_menu == 2:
        #Adicionar produto
        nome_produto = input("Insira o nome do produto: \n")
        preco_produto = input("Insira o valor \n")
        cor_produto = input("Insira a cor \n")
        adicionar_produto = {'Nome do Produto': nome_produto, 'R$': preco_produto, 'Cor': cor_produto}
        compras.append(adicionar_produto)
    elif escolha_menu == 3:
        #Remover produtos
        indice = 0
        for produto in compras:
            print(f"{indice} - {produto}")
            indice += 1
        print(f"Selecione {indice} para sair...")
        remover_produto = input("Qual desses produtos você deseja remover da lista? (Selecione um número) \n")
        if remover_produto.isnumeric():
            remover_produto_conversao = int(remover_produto)
            if remover_produto_conversao in range(0, indice):
                print("Deletando...")
                produto_removido = compras.pop(remover_produto_conversao)
                print(f"O produto {produto_removido} \n foi removido com sucesso!")
            elif remover_produto == indice:
                print("Saindo do menu de remoção de produtos")
                break
            else:
                print("Opção nao existe! Por favor insira uma opção existente.")
    elif escolha_menu == 4:
        #Fechar lista de compras
        print("Lista Finalizada")
        break
    elif escolha_menu not in(1,2,3,4):
        print("Opção invalida")