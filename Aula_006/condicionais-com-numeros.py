numero = int(input("Informe o um número entre 0 e 10: "))

if numero >= 0 and numero <= 3:
    print(f"O número {numero} esta entre o 0 e 3.")
elif numero >= 3 and numero <= 4:
    print(f"O número {numero} esta entre 3 e 4.")
elif numero >= 5 and numero < 10:
    print(f"O número {numero} esta entre 5 e 9.")
elif numero == 10:
    print(f"O número {numero} é o maior possivel.")