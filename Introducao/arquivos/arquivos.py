# arquivo = open("vendas.txt", "r") #ou caminho completo C:etc // r:leitura 

# arquivo.close()

with open("vendas.txt", "r") as arquivo: #abre e fecha automaticamente
    info= arquivo.readlines()

print(info)

vendasTotais=0

for item in info:
    item = item.replace("\n", "")
    item = item.replace(" ", "")
    resultado = item.split(",")
    valor = resultado[1]
    valor = float(valor)
    vendasTotais = vendasTotais + valor
print(vendasTotais)

