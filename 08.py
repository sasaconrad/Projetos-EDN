from datetime import date

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)

def eh_palindromo(texto):
    txt = "".join(c.lower() for c in texto if c.isalnum())
    return txt == txt[::-1]

def programa_gorjeta():
    conta = float(input("Valor da conta: R$ "))
    gorj = float(input("Porcentagem da gorjeta (%): "))
    valor = calcular_gorjeta(conta, gorj)
    print(f"Gorjeta: R$ {valor:.2f}")

def programa_palindromo():
    frase = input("Digite uma palavra ou frase: ")
    print("Sim" if eh_palindromo(frase) else "Não")

def programa_desconto():
    valor = float(input("Preço do produto: R$ "))
    desconto = float(input("Percentual de desconto (%): "))
    preco_final = valor - (valor * desconto / 100)
    print(f"Preço final: R$ {preco_final:.2f}")

def dias_vivo():
    ano = int(input("Ano de nascimento: "))
    mes = int(input("Mês de nascimento: "))
    dia = int(input("Dia de nascimento: "))
    nasc = date(ano, mes, dia)
    hoje = date.today()
    print(f"Você está vivo há {(hoje - nasc).days} dias!")

while True:
    print("\n===== MENU AP05 =====")
    print("1 - Calcular gorjeta")
    print("2 - Verificar palíndromo")
    print("3 - Desconto no produto")
    print("4 - Dias de vida")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        programa_gorjeta()
    elif opcao == "2":
        programa_palindromo()
    elif opcao == "3":
        programa_desconto()
    elif opcao == "4":
        dias_vivo()
    elif opcao == "0":
        print("Encerrado!")
        break
    else:
        print("Opção inválida!")
