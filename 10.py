import pandas as pd # type: ignore
import csv, json

def media_logs():
    try:
        arq = input("Arquivo CSV: ")
        df = pd.read_csv(arq)
        print("Média:", df["tempo_execucao"].mean())
        print("Desvio padrão:", df["tempo_execucao"].std())
    except Exception:
        print("Falha ao ler arquivo.")

def criar_csv():
    try:
        nome = input("Salvar como: ")
        dados = [
            ["Nome","Idade","Cidade"],
            ["Ana",23,"São Paulo"],
            ["Beto",30,"Rio"],
            ["Carla",19,"BH"]
        ]
        with open(nome, "w", newline="") as f:
            csv.writer(f).writerows(dados)
        print("Arquivo criado!")
    except Exception:
        print("Falha ao salvar.")

def ler_csv():
    try:
        arq = input("Arquivo CSV: ")
        with open(arq) as f:
            for linha in csv.reader(f):
                print(linha)
    except Exception:
        print("Arquivo não encontrado.")

def json_rw():
    try:
        dados = {"nome": "Luna", "idade": 28, "cidade": "Recife"}
        with open("dados.json","w") as f:
            json.dump(dados,f)
        print("Salvo!")
        with open("dados.json") as f:
            print(json.load(f))
    except Exception:
        print("Erro JSON.")

while True:
    op = input("\n1-média logs 2-criar CSV 3-ler CSV 4-JSON 0-sair: ")
    if op=="1": media_logs()
    elif op=="2": criar_csv()
    elif op=="3": ler_csv()
    elif op=="4": json_rw()
    elif op=="0": break
    else: print("X")