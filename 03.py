idade = int(input("Digite a sua idade: "))

if idade < 18:
    if idade < 12:
        print("Você é uma criança.")
    else:
        print("Você é um adolescente.")
else:
    if idade < 65:
        print("Você é um adulto.")
    else:
        print("Você é um idoso.")