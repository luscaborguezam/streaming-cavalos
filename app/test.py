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
except Exception:
    pass