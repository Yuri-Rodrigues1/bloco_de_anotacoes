usuarios = []
anotacoes = []


def cadastro():
    print("")
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
    resp = input("deseja fazer um novo cadatro? s/n   ")
    if resp == "s":
        cadastro()
    else:
        login()    

def login():
    print("__________________________________")
    print(" ")
    print("faça o seu login! ")
    nome = input('nome: ')
    senha = input('senha: ')

    for usuario in usuarios:
        if usuario['nome'] == nome and usuario['senha'] == senha:
            print('Bem vindo.....')
            print("__________________________")
            print(" ")
            sistema()
        else:
            print('usuário ou senha incorretos... tente novamente')
            login()

def sistema():
    print("bem vindo ao seu blog de anotações!!")
    print("selecione a opção desejada...")
    print("1 - criar anotação")
    print("2 - ver anotações existentes")
    print("3 - sair")
    escolha = input("Digite sua escolha = ")
    if escolha == "1":
        nome = usuarios[0]['nome']
        anotacao = input(f'{nome} fale oque esta pensando')
        anotacoes.append({
            "nome": nome,
            "anotacao": anotacao
        })
        print("anotação registrada com sucesso!")
        print("_______________________________")
        print(" ")
        sistema()
    if escolha == "2":
        for i in anotacoes:
            print(i['nome']+" - "+i['anotacao'])
        print("_______________________________")
        print(" ")
        sistema()

print("Olá, por favor faça seu cadastro ou realize o login se ja tiver um.")
e = input("1 - cadastro    2 - login ")
if e == "1":
    cadastro()
if e == "2":
    login()


