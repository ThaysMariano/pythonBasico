nome = "Thays Mariano"
venda = [100, 50, 130, 80, 120]

print(len(venda))
print("ultimo",venda[-1])

totalVendas = sum(venda)
print("somavendas",totalVendas)

quantidadeVendas = len(venda)
print("qnt vendas",quantidadeVendas)

maxVenda = max(venda)
minVenda = min(venda)
print(f"valor min: {minVenda}, valor max {maxVenda}")

posicao = venda.index(130)
print(f"130 esta na posicao: {posicao}")
print(f"do segundo ao final", venda[posicao:])

produtos = ["celular", "maca", "pote"]
precos = [4000, 3, 18]
print("celular" in produtos) # true
# produtoUsuario = input("digite o produto para adicionar: ")
# print(produtoUsuario in produtos)

precos[0]= precos[0]*1.1

print(precos)

produtos.append("macbook") #inserir no final
precos.append(10300)

print(produtos, precos)

produtos.remove("macbook") #valor
precos.pop(-1) #indice
print(produtos, precos)

produtos.insert(1, "banana") #insere no indice que quer
print(produtos)

print(produtos.count("banana")) #contar aparicoes

precos.sort() #ordena crescente
print(precos)

precos.sort(reverse=True) #ordena decrescente
print(precos)




