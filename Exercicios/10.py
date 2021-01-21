#Fazer uma busca sequencial em uma lista (Criar uma tupla [0....20] e pedir para o usuário fazer uma busca).

tupla = (tuple(range(0, 21)))

# Execute para ver todos itens da tupla "print(tupla)"

print("Informe um numero de 0 a 20 para buscar")
busca = int(input())

if busca in tupla:
    print(f"O numero {busca} procurado existe!")
else:
    print(f"O numero {busca} procurado não existe!")