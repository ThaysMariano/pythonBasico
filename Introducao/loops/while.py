# sistema consulta de precos
precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

# pedir o produto e retornar o preco, se n existir falar q n existe

while True:
    nomeProduto = input("Digite o nome do produto: ")
    nomeProduto = nomeProduto.lower()

    if nomeProduto == "sair":
        break

    if nomeProduto not in produtos:
        print("Produto não existe na base de dados")
    else:
        posicaoProduto = produtos.index(nomeProduto)
    print(f"O preco do {nomeProduto} é {precos[posicaoProduto]}.")