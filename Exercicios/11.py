# Fazer uma busca sequencial em uma matriz (Criar uma matriz 10 linhas e 10 colunas e pedir para o usuário fazer uma busca).


matriz = [list(range(i, i+10)) for i in range(1, 100, 10)]

print("Insira o numero que deseja buscar de 0 a 100")
numero_buscado = int(input())

i = 0
j = 0
isencontrado = False

for linha in matriz: #varre a linha da Matriz
    for coluna in linha: #varre a coluna da linha da Matriz
        if(coluna == numero_buscado): #Compara para fazer a busca
            print(f"encontrou o {coluna} na linha {i+1} e na coluna {j+1}")
            isencontrado = True
            break
        j += 1
    if isencontrado:
        break
    i += 1
    j = 0 #reset de coluna