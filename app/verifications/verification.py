class CheckData:
    def validarNome(self='', name='', lastname=''):
        """
        > Função que verifica os caracteres dos parametros.
        :param name primeiro nome
        :param lastname: segundo nome
        :return: True or False
        """

        name = name.replace(" ", '')
        lastname = lastname.replace(" ", '')

        if name.isalpha() and lastname.isalpha():
            return True
        else:
            print("Erro.\nOBS:Preencha todos os campos;\nCampos não aceitam caracteres numéricos ou especiais.")
        return False

    def validarIdade(self='', day='', month='', year=''):
        """
        > Função que verifica data de nascimento
        :param day: dia
        :param month: mes
        :param year: ano
        :return: True or False
        """

        from datetime import date

        if day.isnumeric() and month.isnumeric() and year.isnumeric() and int(day) in range(1, 30) and int(
                month) in range(1, 12):
            dataDeNascimento = date(day=int(day), month=int(month), year=int(year))
            dataAtual = date.today()
            idade = dataAtual.year - dataDeNascimento.year
            if idade in range(15, 129):
                return True
            elif idade >= 129:
                print(f"Você não tem {idade} anos.")
                return False
            else:
                print("Menores de 15 anos não podem se cadastrar")
                return False
        else:
            print("\033[31mData inválida, digite novamente\033[m")
            return False

    def validarCPF(self='', cpf=''):
        """
        Função que verifica cpf válido para cadastro
        :param cpf: cpf
        :return: True or False
        """
        from app.banco import banco
        if '.' in cpf or '-' in cpf:
            cpf = cpf.replace('.', '')
            cpf = cpf.replace('-', '')
        if cpf.isnumeric() and len(cpf) == 11:
            cpfCadastrados = banco.buscarCampoDaTabela('cpf')
            for item in cpfCadastrados:
                if cpf == item:
                    print("Este CPF já está cadastrado")
                    return False
            return True
        else:
            print("CPF inválido")
            return False

    def validarCEP(self='', cep=''):
        """
        Função que verifica cep
        :param cep: cep
        :return: (True, dict) or (False, textError)
        """
        import requests

        cep = cep.replace('-', '')
        if len(cep) == 8 and cep.isnumeric():
            r = requests.get('https://viacep.com.br/ws/' + cep + '/json/').json()

            if r == {'erro': 'true'}:
                return False, "CEP Inválido"
            else:
                endereco = {
                    'logradouro': r['logradouro'],
                    'bairro': r['bairro'],
                    'localidade': r['localidade']
                }

                for id, valor in endereco.items():
                    print(f"{id}: {valor}")

                while True:
                    numeroCasa = input("Número da casa: ").strip()
                    if numeroCasa.isnumeric():
                        endereco['numero'] = int(numeroCasa)
                        break
                    else:
                        print(f"{numeroCasa} não é numérico ou valor inteiro")

                condicao = input("Está correto? [S/N]:")
                if condicao.lower() == 's':
                    return True, endereco
                else:
                    return False, "Digite novamente"
        else:
            return False, "CEP Ínválido"

    def validarCredenciais(self='', username='', passsoword=''):
        """
        Função que valida senha e nome de usuário para cadastro
        :param username: nome de usuário
        :param passsoword: senha
        :return: False or True
        """
        from app.banco import banco
        if(username == '' or passsoword == ''):
            print("Os campos não podem ficar vazios")
            return False
        usernameCadastrados = banco.buscarCampoDaTabela('username')
        for item in usernameCadastrados:
            if username == item:
                print("Username existente")
                return False
        if len(passsoword) >= 8:
            return True
        else:
            print("Senha deve ter no mínimo 8 caracteres")
            return False
