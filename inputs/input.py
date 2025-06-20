nome = input("digite seu nome completo ")
email = input("digite aqui seu email: ")


#servidor do email
servidorEmailIndex = email.find("@")
servidorEmailTxt = email[servidorEmailIndex:]
print("servidor:",servidorEmailTxt)

#primeiro nome do usuario
primeiroEspaco = nome.find(" ")
primeiroNome = nome[:primeiroEspaco]
print("Primeiro nome:",primeiroNome)

#mensagem: usuario 'nome' cadastrado com o email 'email'
print(f"Usuário {primeiroNome} cadastrado com o email {email} eba eba eba")

#mensagem: enviamos um link de confrimacao para o email 'primeiraletra***servidor'
primeiraletra = email[0]
print(f"Enviamos um link de confirmação para o email {primeiraletra}*****{servidorEmailTxt}")

# ------------

# 1% das vendas

vendas = float(input("Digite suas vendas do dia: "))
bonus = vendas * 0.01

print(f"Seu bonus foi de R${bonus}")