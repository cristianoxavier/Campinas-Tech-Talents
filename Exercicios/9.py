# Elabore um algoritmo em Python que calcule a área e o perímetro de um círculo, sabendo que A = πr² e P=2πr.

pi = 3.14

print("Informe o raio: ")
raio = int(input())

circuferencia = 2 * pi * raio
area = pi * (raio * raio)

print(f"A circuferencia é {circuferencia} e a area é {area}")