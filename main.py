import json

def sistema_de_login():
    print("--- Sistema de Autenticação ---")
    
    # Tenta carregar o banco de dados se o arquivo já existir
    try:
        with open('usuarios.json', 'r') as arquivo:
            banco_de_dados = json.load(arquivo)
    except FileNotFoundError:
        # Se for a primeira execução, cria um dicionário vazio
        banco_de_dados = {}

    while True:
        print("\nMenu Principal:")
        print("1 - Fazer Login")
        print("2 - Cadastrar Usuário")
        print("3 - Sair")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == '2':
            print("\n-- Tela de Cadastro --")
            email_novo = input("Digite seu e-mail: ")
            
            # Verifica se o e-mail já existe no sistema
            if email_novo in banco_de_dados:
                print("Erro: Este e-mail já está cadastrado no sistema.")
                continue
                
            senha_nova = input("Crie uma senha: ")
            
            # Salva os dados no dicionário local
            banco_de_dados[email_novo] = senha_nova
            
            # Atualiza o arquivo json
            try:
                with open('usuarios.json', 'w') as arquivo:
                    json.dump(banco_de_dados, arquivo, indent=4)
                print(f"Cadastro realizado com sucesso! Bem-vindo, {email_novo}.")
            except:
                print("Erro ao salvar os dados no arquivo.")
            
        elif opcao == '1':
            print("\n-- Tela de Login --")
            email_login = input("Digite o e-mail: ")
            senha_login = input("Digite a senha: ")
            
            # Verifica se o e-mail existe e se a senha está correta
            if email_login in banco_de_dados and banco_de_dados[email_login] == senha_login:
                print(f"Login realizado com sucesso! Usuário logado: {email_login}")
            else:
                print("E-mail ou senha incorretos. Tente novamente.")
        
        elif opcao == '3':
            print("Encerrando o programa...")
            break
            
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")

# Inicia o programa
sistema_de_login()