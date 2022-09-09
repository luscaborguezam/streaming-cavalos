# TODO: Loja de streaming tipo, NETFLIX, HBO etc.
# TODO: Quando o usuário acessar o programa deverá haver opção de cadastro e de acesso, login, logon
# TODO: Coletar dados de cadastro de usuários (caso não haja)
# TODO: Coletar nome completo, separar para as varáveis: nome, sobrenome
# TODO: Caso usuário já exista, mostra um menu com opções de filmes para assistir
# TODO: Criar opção de logout
# TODO: Coletar idade
# TODO: Coletar CPF: ATENÇÃO, não coloque seus dados originais
# TODO: Na coleta do CPF, deverá ser aceito somente números: 1203120398
# TODO: Coletar CEP, e apartir do cep preencher o restante dos dados, rua e cidade
# TODO: Perguntar se dados do CEP estão corretos
# TODO: Coletar número da casa

from verifications.verification import CheckData
from banco import banco
from datetime import date
import re

def acessar():
    """
    >Função que mostra o menu e retorna a opção desejada
    :return: opcao
    """


    print(f"{'Straming Horse':-^30}")
    menu = ["Login", "Register", "Exit"]
    for i, op in enumerate(menu):
        print(f"[{i + 1}] - {op}")

    opcaoMenu = input('\n>>')
    if re.search(r'[04-9a-zA-Z]', opcaoMenu) or int(opcaoMenu) > len(menu):
        print(f"\033[31mNão exite essa opção {opcaoMenu}\033[m")
    else:
        if opcaoMenu == '1':
            login()
        elif opcaoMenu == '2':
            coletarDados()
        elif opcaoMenu == '3':
            exit()


def login():
    condicao = True
    while condicao:
        username = input("Username: ").strip()
        passoword = input("Passoword:").strip()
        if banco.consultarCredenciais(username=username, passoword=passoword):
           condicao = index()
        else:
            print("Username ou Passoword estão incorretos")
            op = input("Voltar ao menu? [S/N]")
            if op.lower() == 's':
                break
def index():
    while True:
        servicos = ['filmes', 'séries', 'streamins', 'Log out']
        for i, item in enumerate(servicos):
            print(f'[{i + 1}]-{item}')

        opcao = input('\n>>')
        if re.search(r'[05-9a-zA-Z]', opcao) or int(opcao) > len(servicos):
            print(f"\033[31mNão exite essa opção {opcao}\033[m")
        else:
            if opcao == '4':
                return False


def coletarDados():

    #Recebendo nome
    while True:
        print(f"{'Cadastro':-^30}")
        nome = input("Nome:").strip()
        sobrenome = input("Sobrenome:").strip()
        if CheckData.validarNome(name=nome, lastname=sobrenome):
            break

    #Recebendo data de nascimento
    while True:
        print("Data de nascimento")
        dia = input("Dia: ").strip()
        mes = input("Mes: ").strip()
        ano = input("Ano: ").strip()
        if CheckData.validarIdade(day=dia, month=mes, year=ano):
            dataNascimento = date(day=int(dia), month=int(mes), year=int(ano))
            break


    #Recebendo CPF
    while True:
        cpf = input("CPF: ").strip()
        if CheckData.validarCPF(cpf=cpf):
            break

    #Recebendo CEP
    import requests
    while True:
        cep = input("CEP: ").strip()
        verificacao, endereco = CheckData.validarCEP(cep=cep)
        if verificacao:
            break
        else:
            print(endereco)

    #Recebendo email e senha
    while True:
        username = input("Username: ").strip()
        passoword = input("Passoword:").strip()
        if CheckData.validarCredenciais(username=username, passsoword=passoword):
            break

    #Cadastro
    while True:
        confirmar = input("Cadastar? [S/N]")
        if confirmar.lower() == 's':
            user = {
                "nome": nome,
                "sobrenome": sobrenome,
                "data_nascimento": dataNascimento,
                "cpf": cpf,
                'logradouro': endereco['logradouro'],
                'bairro': endereco['bairro'],
                'localidade': endereco['localidade'],
                "numero": endereco['numero'],
                "username": username,
                "passoword": passoword
            }
            if banco.compararDados(cpf=user['cpf'], username=user['username']):
                banco.cadastraruser(user)
            else:
                print("Cadastre novamente")
            break
        elif confirmar.lower() == 'n':
            break
        else:
            print("Opção inesistente")


#----------------------------------
while True:
    acessar()
