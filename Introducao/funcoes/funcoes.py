
listaPrecos = [1500, 1000, 800, 2000]

somaImposto = 0


def calcularImposto(preco):
    if preco<=1000:
        return 0.1
    else:
        return 0.15


for preco in listaPrecos:
    imposto = calcularImposto(preco)
    somaImposto = somaImposto + preco * imposto
    print(f"preco: {preco:.2f}, imposto: {preco*imposto:.2f}, soma dos impostos: {somaImposto:.2f}")





