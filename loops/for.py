for i in range(4):
    print("ola", i)

# imposto de 10% em cada produto 

listaPrecos = [1500, 1000, 800, 2000]

for preco in listaPrecos:
    imposto = preco * 0.1
    print(preco, imposto)

# se preco ate 1000 -> imp = 10%
# se preco >1000 -> imp = 15%

print("------------------------------")

somaImposto = 0

for preco in listaPrecos:
    if preco<=1000:
        imposto = 0.1
    else:
        imposto = 0.15
    somaImposto = somaImposto + preco*imposto
    print(f"preco: {preco:.2f}, imposto: {preco*imposto:.2f}, soma dos impostos: {somaImposto:.2f}")

    
print("------------------------------")

vendas22 = {"jan":15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas23 = {"jan":17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}

# quando variou cada mes em 23 em comparação com 22 (variacao percentual de jan23 para jan22 etc)
# simular: se a empresa tivesse ao menos empatado com 23 nos meses que vendeu pouco qual seria ao faturamento de 22

faturamento23=0
faturamento22=0
faturamento22Nv=0

for mes in vendas23:
    percentual = vendas23[mes]/vendas22[mes]-1
    faturamento22 = faturamento22+ vendas22[mes]
    faturamento23 = faturamento23+ vendas23[mes]
    print(f"Percentual: {percentual:.2%}. Vendas 2022: {faturamento22}. Vendas 2023: {faturamento23}")

    if vendas22[mes]<vendas23[mes]:
        faturamento22Nv = vendas23[mes] + faturamento22Nv
    else:
        faturamento22Nv = faturamento22Nv + vendas22[mes]
print(f"Faturamento corrigido {faturamento22Nv}")








