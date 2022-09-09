import sqlite3

def cadastrar(dados_user=dict()):
    """
    > Função que cadastra usuário no banco dedados
    :param dados_user: Dicionário com dados do cliente
    """
    con = sqlite3.connect('banco\streaminghorse.db')
    cur = con.cursor()

    try:
        cur.execute('CREATE TABLE cliente ('
                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                    'nome TEXT, '
                    'sobrenome TEXT, '
                    'data_nascimento TEXT, '
                    'cpf TEXT, '
                    'logradouro TEXT, '
                    'bairro TEXT, '
                    'localidade TEXT, '
                    'numero INTEGER, '
                    'username TEXT, '
                    'passoword TEXT);')
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
                'numero, '
                'username, '
                'passoword) '
                'VALUES (?,?,?,?,?,?,?,?,?,?)',(
                                            dados_user['nome'],
                                            dados_user['sobrenome'],
                                            dados_user['data_nascimento'],
                                            dados_user['cpf'],
                                            dados_user['logradouro'],
                                            dados_user['bairro'],
                                            dados_user['localidade'],
                                            dados_user['numero'],
                                            dados_user['username'],
                                            dados_user['passoword'])
                )

    # salvar a conexão
    con().commit()
    print("Cadastrado com sucesso!!!")

    # fechando a conexão
    con().close()


def consultarCredenciais(username='', passoword=''):
    """
    Função que compara credenciais cadastradas com as inseridas
    :param username: nome de usuário
    :param passoword: senha
    :return: True
    """
    try:
        con = sqlite3.connect('banco\streaminghorse.db')
        cur = con.cursor()

        cur.execute("SELECT username, passoword, id FROM cliente")
        resultado = cur.fetchall()
        for linha in resultado:
            login = list()
            for i in linha:
                login.append(i)
            if login[0] == username and login[1] == passoword:
                print("Bem vindo ao Streaming Horse")
                return True
        print("Usuário ou senha incorretos.")
    except sqlite3.Error as error:
        print(f"Falha na execução da query\n{error}")
        con().close()


def buscarCampoDaTabela(campo=''):
    """
    Função que retorna uma lista dos dados cadasrados em uma coluna especifica da tabela cliente
    :param campo: nome da coluna de uma tabela
    :return: listaResultados
    """
    con = sqlite3.connect("banco\streaminghorse.db")
    cur = con.cursor()

    cur.execute('SELECT '+campo+' FROM cliente')
    resultado = cur.fetchall()
    listaResultado = list()
    for item in resultado:
        listaResultado.append(item[0])
    # print(listaResultado)
    return listaResultado
    con.close()
