
# funcao devolvendo mais de uma resposta em ( ) -> imutável

def calcImposto2 (preco, ir=0.275, csll=0.035, iss=0.05):
    impostoIR = preco * ir
    impostoCSLL = preco * csll
    impostoISS = preco * iss
    return impostoIR, impostoCSLL, impostoISS

resposta = calcImposto2(1000)
print(resposta)
print(resposta[2])

#separar as variaveis
print("------------------")
ir, csll, iss = resposta

print(ir, csll, iss, sep="\n")

tamanho_tela = (1920, 1080) #uma tela é de tamanho fixo, usa tupla






