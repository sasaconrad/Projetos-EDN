import random, string, requests # type: ignore

def senha():
    try:
        n = int(input("Tamanho: "))
        chars = string.ascii_letters + string.digits + string.punctuation
        s = "".join(random.choice(chars) for _ in range(n))
        print("Senha:", s)
    except:
        print("Erro.")

def usuario():
    try:
        r = requests.get("https://randomuser.me/api/").json()["results"][0]
        print(r["name"]["first"], r["name"]["last"], "|", r["email"], "|", r["location"]["country"])
    except:
        print("Erro.")

def cep():
    try:
        d = requests.get(f"https://viacep.com.br/ws/{input('CEP: ')}/json/").json()
        if "erro" in d:
            print("CEP inválido.")
        else:
            print(d["logradouro"], d["bairro"], d["localidade"], d["uf"])
    except:
        print("Erro.")

def moeda():
    try:
        m = input("Moeda (USD/EUR...): ").upper()
        d = requests.get(f"https://economia.awesomeapi.com.br/json/last/{m}-BRL").json().get(f"{m}BRL")
        if not d:
            print("Moeda inválida.")
        else:
            print(d["bid"], d["high"], d["low"], d["create_date"])
    except:
        print("Erro.")

while True:
    o=input("\n1-senha 2-user 3-cep 4-moeda 0-sair: ")
    if o=="1": senha()
    elif o=="2": usuario()
    elif o=="3": cep()
    elif o=="4": moeda()
    elif o=="0": break
    else: print("X")
