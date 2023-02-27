inventário = []

resposta = "S"
while resposta == "S":
    inventário.append(input("Equipamento: "))
    inventário.append(float(input("Valor: ")))
    resposta = input('Digite "S" para continuar: ').upper()

for elemento in inventário:
    print(elemento)