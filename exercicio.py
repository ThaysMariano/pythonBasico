vendas = {
    "andre": [1000, 500, 300, 5000, 1500, 80, 3000],
    "andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "alan": [800, 100],
    "ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180, 100, 120, 110, 130, 140]
}

#cada venda o vendedor ganha 2 reais e 1% da venda 
#calcular o valor total de bonus e o bonus de cada vendedor 

somaBonus =0
somaIndividual = 0

for venda in vendas:
    somaIndividual = 0
    for valor in vendas[venda]:
        somaIndividual = valor * 0.01 + somaIndividual
    
    somaIndividual = somaIndividual + (len(vendas[venda]))*2
    print(f"Soma de bonus de: {venda} -> {somaIndividual:.2f}")
    somaBonus = somaIndividual +somaBonus
    
print(f"soma total {somaBonus:.2f}")
        
        

