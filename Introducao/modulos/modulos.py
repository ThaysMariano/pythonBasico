# bibliotecas - os - requests

import os # acessar arquivos do computador

#listar
arquivos = os.listdir()
print(arquivos)

#mover
# os.rename("vendas.txt", "arquivos/vendas.txt")

arquivosExercicio = os.listdir("pastaDeArquivos")
print(arquivosExercicio)

for arq in arquivosExercicio:
    if "txt" in arq:
        if "22" in arq:
            os.rename(f"pastaDeArquivos/{arq}", f"pastaDeArquivos/22/{arq}")
        elif "23" in arq:
            os.rename(f"pastaDeArquivos/{arq}", f"pastaDeArquivos/23/{arq}")
   

import requests #API

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

resposta = requests.get(link)

dic_resposta = resposta.json()

print(dic_resposta)
print("---------------")
cotDolar = dic_resposta["USDBRL"]
print(cotDolar)
print("---------------")
bidDOlar = cotDolar["bid"]
print("bid: ",bidDOlar)






