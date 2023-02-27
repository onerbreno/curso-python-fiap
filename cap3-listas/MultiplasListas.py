equipamentos = []
valores = []
seriais = []

resposta = "S"
while resposta == "S":
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input('Valor: ')))
    seriais.append(int(input('Numero serial: ')))
    resposta = input('Digite "S" para continuar: ').upper()

# busca = input('Digite o nome do equipamento que deseja buscar: ')
# for indice in range(0, len(equipamentos)):
#     if busca == equipamentos[indice]:
#         print("Equipamento..: ", (indice + 1))
#         print("Nome.........: ", equipamentos[indice])
#         print("Valor........: ", valores[indice])
#         print("Serial.......: ", seriais[indice])

# depreciacao = input("Digite o nome do equipamento que será depreciado: ")
# for indice in range(0, len(equipamentos)):
#     if depreciacao == equipamentos[indice]:
#         print("Valor antigo: ", valores[indice])
#         valores[indice] = valores[indice] * 0.9
#         print("Novo valor: ", valores[indice])


serial = int(input("Digite o serial do equipamento: "))
for indice in range(0, len(equipamentos)):
    if serial == seriais[indice]:
        del seriais[indice]
        del valores[indice]
        del equipamentos[indice]
        print("Equipamento descartado.")
        break

for indice in range(0, len(equipamentos)):
  print("Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])