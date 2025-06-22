faturamento = 1000
custo = 100

lucro = faturamento - custo

if(lucro>=0): 
    print("lucro: ",lucro)
else:
    print("Sem lucro :/")


produtos = ["celular", "maca", "pote"]
novoProduto = input("Digite o novo produto: ")
novoProduto = novoProduto.lower()

if novoProduto in produtos:
    print("Produto ja esta na lista")
else:
    produtos.append(novoProduto)
    print("produto adicionado")

print(produtos)


# acima de 15000 - 500 de bonus
# acima de 10000 - 150 de bonus
# acima de 5000 - 50 de bonus

vendas = 15100
metaempresa = 15050

if not vendas > metaempresa:
    print("sem lucro")
else:
    if vendas>=15000:
        print("bonus de 500 reais")
    elif vendas >= 10000:
        print("bonus de 150 reais")
    else:
     print("bonus de 50 reais")


# sistema consulta de precos
precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

# pedir o produto e retornar o preco, se n existir falar q n existe

nomeProduto = input("Digite o nome do produto: ")
nomeProduto = nomeProduto.lower()

if nomeProduto not in produtos:
    print("Produto não existe na base de dados")
else:
    posicaoProduto = produtos.index(nomeProduto)
    print(f"O preco do {nomeProduto} é {precos[posicaoProduto]}.")


