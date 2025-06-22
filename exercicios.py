
# media das notas

print("digite suas notas:")
n1 = int(input("1: "))
n2 = int(input("2: "))
n3 = int(input("3: "))

media = float((n1+n2+n3) /3)

if media>7.0:
    print("aprovado")
elif media>=5.0:
    print("rec")
else:
    print("reprovado")

print("media", media)

print("-----------------------------------")

# contar o nuemro de vogais

print ("digite uma palavra ou frase: ")
string = input()

vogais = ["a", "e", "i" ,"o", "u"]
v = 0

for letra in string.lower():
    if letra in vogais:
        v+=1

print("Num de vogais:", v)

print("-----------------------------------")

# tabuada do numero inserido

num = int(input("digite um numero para fazer a tabuada: "))

print(f"Tabuada do {num}:")
for i in range(11):
    print(f"{i} * {num} = {i*num}")

print("-----------------------------------")

# fazer a média de uma lista de numeros 

numDeNumeros = int(input("Digite o numero de numeros que vc quer inserir: "))

lista = []

for num in range(numDeNumeros):
    numero = int(input("insira um valor: "))
    lista.append(numero)

media = sum(lista)/numDeNumeros
print(lista)
print(media)


print("-----------------------------------")

# ver se é palindromo

palavra = input("Digite sua palavra: ").lower().replace(" ", "")

palavraINvertida = palavra[::-1]

print(palavra, palavraINvertida)


if palavra == palavraINvertida:
    print("é palindromo")
else:
    print("nao e palindromo")

print("-------------------------------")

# contar palavras de uma frase

frase = input("Digite sua frase: ")

palavras = frase.split(" ")

print(f"Total de palavras: {len(palavras)}")

print("-------------------------------")

# Somar apenas os numeros pares da lista de inputs

listaNuns = []

while True:
    entrada = input("Digite o numero ou 'sair' para sair: ")
    if entrada == "sair":
        break
    else:
        entrada = int(entrada)
        listaNuns.append(entrada)

soma=0

for num in listaNuns:
    if num%2==0:
        soma += num

print(f"Soma dos numeros pares: {soma}")

print("-------------------------")

# Calcular a sequencia de fibonacci até um número limite

limite = int(input("Digite seu limite de fibonacci: "))

fib = [0, 1]

while True:
    num = fib[-1] + fib[-2]

    if num > limite:
        break

    fib.append(num)

print(fib)


