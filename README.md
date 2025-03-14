# Sistema de Gerenciamento de Estoque

Este é um sistema de gerenciamento de estoque desenvolvido em Python utilizando a biblioteca Flet para a interface gráfica e MySQL como banco de dados. O sistema permite:

-   Cadastrar novos produtos.
-   Consultar produtos cadastrados.
-   Atualizar a quantidade disponível de produtos.
-   Remover produtos do cadastro.
-   Registrar vendas e atualizar o estoque automaticamente.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

1. **Python 3.8 ou superior**:

    - [Download Python](https://www.python.org/downloads/)

2. **MySQL Server**:

    - [Download MySQL](https://dev.mysql.com/downloads/mysql/)

3. **Bibliotecas Python**:
    - Instale as dependências do projeto executando:
        ```bash
        pip install -r requirements.txt
        ```

## Configuração do Banco de Dados

1. Crie um banco de dados chamado `gerenciamento_estoque` no MySQL:

    ```sql
    CREATE DATABASE gerenciamento_estoque;
    ```

2. Crie as tabelas necessárias executando o seguinte script SQL:

    ```sql
    USE gerenciamento_estoque;

    CREATE TABLE Produtos (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Nome VARCHAR(255) NOT NULL,
        Descricao TEXT,
        Quantidade INT NOT NULL,
        Preco DECIMAL(10, 2) NOT NULL
    );

    CREATE TABLE Vendas (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        ID_Produto INT,
        Quantidade_Vendida INT NOT NULL,
        Data_Venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (ID_Produto) REFERENCES Produtos(ID)
    );
    ```

## Configuração do Ambiente

1. Crie um arquivo `.env` na raiz do projeto para armazenar as credenciais do banco de dados:

    ```plaintext
    USER=seu_usuario_mysql
    PASSWORD=sua_senha_mysql
    ```

    Substitua `seu_usuario_mysql` e `sua_senha_mysql` pelo seu usuário e senha do MySQL.

2. Certifique-se de que o arquivo `.env` não seja commitado no repositório Git. Adicione-o ao `.gitignore`:
    ```plaintext
    .env
    ```

## Como Executar o Projeto

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/gerenciamento-estoque.git
    cd gerenciamento-estoque
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

3. Execute o aplicativo:

    ```bash
    python main.py
    ```

4. A interface gráfica será aberta automaticamente no seu navegador ou em uma janela separada, dependendo da configuração do Flet.

## Funcionalidades

### 1. Cadastrar Produto

-   Preencha os campos **Nome**, **Descrição**, **Quantidade** e **Preço**.
-   Clique em **Cadastrar Produto** para adicionar o produto ao banco de dados.

### 2. Consultar Produtos

-   Clique em **Consultar Produtos** para exibir todos os produtos cadastrados.

### 3. Atualizar Quantidade

-   Insira o **ID do Produto** e a **Nova Quantidade**.
-   Clique em **Atualizar Quantidade** para modificar o estoque.

### 4. Remover Produto

-   Insira o **ID do Produto** que deseja remover.
-   Clique em **Remover Produto** para excluí-lo do banco de dados.

### 5. Registrar Venda

-   Insira o **ID do Produto** e a **Quantidade Vendida**.
-   Clique em **Registrar Venda** para registrar a venda e atualizar o estoque.

## Estrutura do Projeto

```
gerenciamento-estoque/
│
├── database/
│   └── db.py          # Código de conexão e operações no banco de dados
│
├── main.py            # Aplicação Flet (interface gráfica)
│
├── .env               # Arquivo de variáveis de ambiente (não versionado)
│
├── requirements.txt   # Dependências do projeto
│
└── README.md          # Documentação do projeto
```

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.
