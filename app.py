usuarios = []

nome = "yuri"
senha = 123


def cadastro():

    print("___________________________________")
    print("cadastre-se")
    nome = input("digite seu nome: ")
    senha = input("digite sua senha: ")

    usuarios.append({
        "nome": nome,
        "senha": senha       
    })

    print("cadastro feito com sucesso")
    print("Olá "+usuarios[0]['nome']+" seu cadastro foi feito com sucesso")
    resp = input("deseja fazer um novo cadatro? s/n")
    if resp == "s":
        cadastro();

def login():
    print("__________________________________")
    print("faça o seu login! ")
    nome = input('nome: ')
    senha = input('senha: ')

    for usuario in usuarios:
        if usuario['nome'] == nome and usuario['senha'] == senha:
            print('Bem vindo.....')
            print("_______________________")
        else:
            print('usuário ou senha incorretos... tente novamente')
            login()


cadastro()
login()
