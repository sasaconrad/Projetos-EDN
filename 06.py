def classificar_idade():
    idade = int(input("Digite sua idade: "))
    if idade <= 12:
        print("Criança")
    elif idade <= 17:
        print("Adolescente")
    elif idade <= 59:
        print("Adulto")
    else:
        print("Idoso")

def calcular_imc():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    imc = peso / (altura ** 2)
    print(f"Seu IMC é {imc:.2f}")

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 25:
        print("Peso normal")
    elif imc < 30:
        print("Sobrepeso")
    else:
        print("Obeso")

def converter_temperatura():
    temp = float(input("Digite a temperatura: "))
    origem = input("Origem (C/F/K): ").upper()
    destino = input("Destino (C/F/K): ").upper()

    if origem == "C":
        celsius = temp
    elif origem == "F":
        celsius = (temp - 32) * 5/9
    elif origem == "K":
        celsius = temp - 273.15
    else:
        print("Unidade inválida!")
        return

    if destino == "C":
        resultado = celsius
    elif destino == "F":
        resultado = (celsius * 9/5) + 32
    elif destino == "K":
        resultado = celsius + 273.15
    else:
        print("Unidade inválida!")
        return

    print(f"Resultado: {resultado:.2f} {destino}")

def ano_bissexto():
    ano = int(input("Digite o ano: "))
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("Ano bissexto!")
    else:
        print("Não é bissexto.")

while True:
    print("\n===== MENU =====")
    print("1 - Classificador de Idade")
    print("2 - Calculadora IMC")
    print("3 - Conversor de Temperatura")
    print("4 - Verificador de Ano Bissexto")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        classificar_idade()
    elif opcao == "2":
        calcular_imc()
    elif opcao == "3":
        converter_temperatura()
    elif opcao == "4":
        ano_bissexto()
    elif opcao == "0":
        print("Valeu! Encerrando...")
        break
    else:
        print("Opção inválida! Tenta de novo.")