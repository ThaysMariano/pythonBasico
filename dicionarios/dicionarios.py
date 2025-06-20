dicPrecos = {"celular": 1000, "camera": 1600, "fone de ouvido": 278, "monitor": 1650}

# pegar um item
precoCelular = dicPrecos["celular"]
print(precoCelular)

#editar item
dicPrecos["celular"] = 2000
print(dicPrecos)

# add item
dicPrecos["iphone"] = 4500
print(dicPrecos)

# deletar da lista 
dicPrecos.pop("camera")
print(dicPrecos)

# tamanho  -> numero de pares
tam = len(dicPrecos)
print(tam)

print("televisao" in dicPrecos)
print(dicPrecos.keys())
print(dicPrecos.values())

# exerc de conculta com dicionario

# dicPrecos = {"celular": 2000, "fone de ouvido": 278, "monitor": 1650, 'iphone': 4500}}

nomeProduto = input("Digite o item: ")
nomeProduto = nomeProduto.lower()

if nomeProduto not in dicPrecos:
    print("produto nao encontrado")
else :
    print(f"O produto '{nomeProduto}' custa R${dicPrecos[nomeProduto]:.2f}")