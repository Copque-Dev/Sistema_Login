Fiz esse projeto para treinar a lógica de programação em Python e entender como funciona a persistência de dados. 

A ideia aqui foi criar um sistema de cadastro e login pelo terminal que não perde as informações quando o programa fecha. Para resolver isso, usei a biblioteca json nativa do Python. O sistema guarda os e-mails e senhas em um arquivo de texto, funcionando como um banco de dados simples local.

O que o projeto faz:
- Cadastro de usuário com bloqueio para e-mail repetido
- Login checando se os dados digitados batem com o arquivo salvo
- Tratamento de erros básico para o programa não quebrar na tela do usuário

Para rodar o projeto na sua máquina, basta ter o Python instalado e digitar no terminal:
python main.py
