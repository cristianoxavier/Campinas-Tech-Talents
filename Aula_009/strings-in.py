var = "hello python"
letra = input(f"A string é {var}... Digite uma letra para busca...")

if len(letra) ==1:
    if letra in var:
        print(f"A letra {letra} existe")
    elif letra.isdigit():
        print(f"Você digitou um número, não uma letra!")
    elif not letra.isprintable():
        print(f"Você alguma coisa, não uma letra!")
    else:
        print(f"A letra {letra} não existe")
elif len(letra) > 1:
    print("Você digitou mais que um caractere. A busca será cancelada!")
else:
    print("Você não digitou uma letra!")
