def calculadora():
    a = float(input("1º número: "))
    op = input("Op (+ - * /): ")
    b = float(input("2º número: "))
    if op == "+": print(a + b)
    elif op == "-": print(a - b)
    elif op == "*": print(a * b)
    elif op == "/" and b != 0: print(a / b)
    else: print("Operação inválida ou divisão por zero.")

def media_turma():
    n = int(input("Qtd alunos: "))
    notas = [float(input(f"Nota {i+1}: ")) for i in range(n)]
    print(f"Média: {sum(notas)/n:.2f}")

def validar_senha():
    s = input("Senha: ")
    if len(s) >= 8 and any(c.isdigit() for c in s):
        print("Senha válida")
    else:
        print("Senha inválida")

def par_impar():
    p = i = 0
    while True:
        n = int(input("Número (0 sai): "))
        if n == 0: break
        (p := p + 1) if n % 2 == 0 else (i := i + 1)
        print("Par" if n % 2 == 0 else "Ímpar")
    print(f"Pares: {p}, Ímpares: {i}")

while True:
    print("\n1-Calc 2-Média 3-Senha 4-Par/Ímpar 0-Sair")
    op = input("Opção: ")
    if op == "1": calculadora()
    elif op == "2": media_turma()
    elif op == "3": validar_senha()
    elif op == "4": par_impar()
    elif op == "0": break
    else: print("Inválido")
