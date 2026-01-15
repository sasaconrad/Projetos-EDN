# ==========================================
# 1 - CONVERSOR DE MOEDA
# ==========================================

valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

dolares = valor_reais / taxa_dolar
euros = valor_reais / taxa_euro

print("===== CONVERSOR DE MOEDA =====")
print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Em dólares: US$ {dolares:.2f}")
print(f"Em euros: € {euros:.2f}")
print()

# ==========================================
# 2 - CALCULADORA DE DESCONTO
# ==========================================

produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

print("===== CALCULADORA DE DESCONTO =====")
print(f"Produto: {produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
print()

# ==========================================
# 3 - CALCULADORA DE MÉDIA ESCOLAR
# ==========================================

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print("===== MÉDIA ESCOLAR =====")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média final: {media:.2f}")
print()

# ==========================================
# 4 - CONSUMO DE COMBUSTÍVEL
# ==========================================

distancia = 300
combustivel = 25

consumo_medio = distancia / combustivel

print("===== CONSUMO DE COMBUSTÍVEL =====")
print(f"Distância percorrida: {distancia} km")
print(f"Combustível gasto: {combustivel} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")
print()