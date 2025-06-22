
frase = "Amanha E DIa dOis"
print(frase.upper())


email = "thaysmariano@gmail.com"

servidor = email.find("@")
print(servidor)

print(email[:servidor])
print(email[servidor:])
servidorTxt = email[servidor+1:]
print(servidorTxt)

print(len(email))

emailTrocado = email.replace(servidorTxt, "hotmail.com")
print(emailTrocado)

nome = "thays mariano"

print(nome.capitalize()) # Thays mariano
print(nome.title()) #Thays Mariano

#-------------------------------------------------------

faturamento = 1000
custo = 700

novasVendas = 300

faturamento = faturamento + novasVendas
lucro = faturamento - custo
margem = lucro/faturamento

print(f"Faturamento: R${faturamento:,.2f} \nCusto: R${custo:.2f}\nLucro: R${lucro:.2f}")
print(f"margem: {margem:.1%}")
























