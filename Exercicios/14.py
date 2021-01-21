#Fazer um sistema de biblioteca (Deve imprimir uma lista com 10 livros, pedir o nome do solicitante do empréstimo, pedir para selecionar um livro e imprimir o livro selecionado).

livros = {
    "Dom Quixote"
    ,"O Conde de Monte Cristo" 
    ,"Um Conto de Duas Cidades"
    ,"O Pequeno Príncipe"
    ,"O Senhor dos Anéis"
    ,"O Alquimista"
    ,"A vida mentirosa dos adultos"
    ,"O Homem de Giz"
    ,"A Garota do Lago"
    ,"A Paciente Silenciosa"
    ,"A Irmã do Sol"
    ,"O Hobbit"
    ,"O que aconteceu com Annie"
    ,"Duna"
}

print("Bem vindo a nossa biblioteca! \n Por favor informe o seu nome: ")
nome = input()

print(f"Ola {nome}, seja bem vindo! \n Livros disponiveis {livros} \n Informe o livro que deseja reservar: ")
reserva = input()

if reserva in livros:
    print(f"{nome} o livro selecionado foi {reserva}, desejamos uma boa leitura")
else:
    print(f"{nome}, Infelizmente o livro {reserva}, não esta no catalogo")