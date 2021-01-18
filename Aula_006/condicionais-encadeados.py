nome = "Cris"
pessoa = "Aluno"
ispessoa = False


if pessoa == "Aluno":
    print("É aluno")
    if ispessoa == True:
        print(f"Olá {nome}!")
    else:
        print("Gostaria de se matricular?")


elif pessoa == "Professor":
    print("É professor")
    if ispessoa:
        print(f"Olá {nome}!")
    else:
        print("Olá gostaria de se tornar um professor?")


elif pessoa == "Aprendiz":
    print("Olá Aprendiz")
    if ispessoa == True:
        print(f"Olá {nome}!")
    else:
        print("Olá, gostaria de aprender?")
