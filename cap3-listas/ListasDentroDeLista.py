inventário = []

resposta = "S"

while resposta == "S":
    equipamento = [input("Equipamento: "), float(input(Valor: )), int(input("Número serial: "))]
    inventario.append(equipamento)
    resposta = input('Digite o "S" para continuar: ').upper()
    
for elemento in inventario:
    print("Nome............", elemento[0])
    print("Valor...........", elemento[1])
    print("Serial..........", elemento[2])