nome = "Thays da Silva Mariano"
email = "thaysmariano@gmail.com"

#servidor do email
servidorEmailIndex = email.find("@")
servidorEmailTxt = email[servidorEmailIndex:]
print(servidorEmailTxt)

#primeiro nome do usuario
primeiroEspaco = nome.find(" ")
primeiroNome = nome[:primeiroEspaco]
print(primeiroNome)

#mensagem: usuario 'nome' cadastrado com o email 'email'
print(f"Usuário {primeiroNome} cadastrado com o email {email} eba eba eba")

#mensagem: enviamos um link de confrimacao para o email 'primeiraletra***servidor'
primeiraletra = email[0]
print(f"Enviamos um link de confirmação para o email {primeiraletra}*****{servidorEmailTxt}")