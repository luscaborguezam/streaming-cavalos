# TODO: Loja de streaming tipo, NETFLIX, HBO etc.


def acessar():
    """
    >Função que mostra o menu e retorna a opção desejada
    :return: x
    """
    # TODO: Quando o usuário acessar o programa deverá haver opção de cadastro e de acesso, login, logon
    while True:
        print(f"{'Straming Horse':-^30}")
        menu = ["Login", "Logon"]
        for i, op in enumerate(menu):
            print(f"[{i+1}] - {op}")

        x = str(input('\n>>'))
        if (x.isnumeric() and int(x) in range(1, len(menu)+1)):
            return x
        else:
            print(f"\033[31mNão exite essa opção {x}\033[m")



# TODO: Coletar dados de cadastro de usuários (caso não haja)

def verificarCadastro():
    pass


# TODO: Coletar nome completo, separar para as varáveis: nome, sobrenome

def coletarDados():
    print(f"{'Cadastro':-^30}")
    nome = input("Nome:")
    sobrenome = input("Sobrenome: ")
    # TODO: Coletar idade
    from datetime import date
    while True:
        print("Data de nascimento")
        dia = input("Dia: ")
        mes = input("Mes: ")
        ano = input("Ano: ")
        if (dia.isnumeric() and mes.isnumeric() and ano.isnumeric()):
            nascimento = date(day=int(dia), month=int(mes), year=int(ano))
            break
        else:
            print("Data inválida, digite novamente")
    # fim while
    atual = date.today()
    idade = atual.year - nascimento.year
    # TODO: Coletar CPF: ATENÇÃO, não coloque seus dados originais
    # TODO: Na coleta do CPF, deverá ser aceito somente números: 1203120398
    while True:
        x = input("CPF: ")
        if x.isnumeric() and len(x) == 11:
            cpf = x
            break
        else:
            print("CPF inválido")
    #fim while
    # TODO: Coletar CEP, e apartir do cep preencher o restante dos dados, rua e cidade
    import requests
    while True:
        cep = input("CEP: ")
        r = requests.get('https://viacep.com.br/ws/'+cep+'/json/').json()
        endereco = {
            'logradouro': r['logradouro'],
            'bairro': r['bairro'],
            'localidade': r['localidade']
        }
        for id, valor in endereco.items():
          print(f"{id}: {valor}")
        condicao = input("Está correto? [S/N]:")
        # TODO: Perguntar se dados do CEP estão corretos
        if condicao.lower() == 's':
            break
    #fim while
    # TODO: Coletar número da casa
    while True:
        numeroCasa = input("Número da casa: ")
        if numeroCasa.isnumeric():
            break
    while True:
        confirmar = input("Cadastar? [S/N]")
        if confirmar.lower() == 's':
            user = {
                "nome": nome,
                "sobrenome": sobrenome,
                "data_nascimento": nascimento,
                "cpf": cpf,
                'logradouro': r['logradouro'],
                'bairro': r['bairro'],
                'localidade': r['localidade'],
                "numero": numeroCasa
            }
            cadastrar(user)
            break
# TODO: Caso usuário já exista, mostra um menu com opções de filmes para assistir
# TODO: Criar opção de logout


def cadastrar(dados_user=dict()):
    import sqlite3
    con = sqlite3.connect('streaminghorse.db')
    cur = con.cursor()

    try:
        cur.execute('CREATE TABLE cliente ('
                    'nome text, '
                    'sobrenome text, '
                    'data_nascimento text, '
                    'cpf text, '
                    'logradouro text, '
                    'bairro text, '
                    'localidade text, '
                    'numero int);')
    except:
        pass

    #inserindo valores

    cur.execute('INSERT INTO cliente ('
                'nome, '
                'sobrenome, '
                'data_nascimento, '
                'cpf, '
                'logradouro, '
                'bairro, '
                'localidade, '
                'numero) '
                'VALUES (?,?,?,?,?,?,?,?)',(
                                            dados_user['nome'],
                                            dados_user['sobrenome'],
                                            dados_user['data_nascimento'],
                                            dados_user['cpf'],
                                            dados_user['logradouro'],
                                            dados_user['bairro'],
                                            dados_user['localidade'],
                                            dados_user['numero'])
                )

    # salvar a conexão
    con.commit()
    print("Cadastrado com sucesso!!!")

    # fechando a conexão
    con.close()
#----------------------------------
opcaoMenu = acessar()
if opcaoMenu == '2':
    coletarDados()
