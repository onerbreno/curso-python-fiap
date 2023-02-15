nivel = input("Digite o nível de acesso: ").upper()

if nivel == "ADM" or nivel == "USR":
    genero = input("Digite seu gênero:")
    if nivel == "ADM":
        if genero == "F":
            print("Olá administradora")
        else:
            print("Olá administrador")
    else:
        if genero == "F":
            print("Olá usuária")
        else:
            print("Olá usuário")
elif nivel == "GUEST":
    print("Olá visitante!")
else:
    print("Olá desconhecido")


