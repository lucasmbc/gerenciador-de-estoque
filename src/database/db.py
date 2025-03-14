from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error

load_dotenv()

class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = os.getenv("USER")
        self.password = os.getenv("PASSWORD")
        self.database = "gerenciamento_estoque"
        self.connection = None

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Conexão ao banco de dados estabelecida.")
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def desconectar(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexão ao banco de dados fechada.")

    def cadastrar_produto(self, nome, descricao, quantidade, preco):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO Produtos (Nome, Descricao, Quantidade, Preco) VALUES (%s, %s, %s, %s)",
                (nome, descricao, quantidade, preco)
            )
            self.connection.commit()
            print("Produto cadastrado com sucesso.")
        except Error as e:
            print(f"Erro ao cadastrar produto: {e}")
        finally:
            if cursor:
                cursor.close()

    def consultar_produtos(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Produtos")
            produtos = cursor.fetchall()
            return produtos
        except Error as e:
            print(f"Erro ao consultar produtos: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def atualizar_quantidade(self, id_produto, nova_quantidade):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "UPDATE Produtos SET Quantidade = %s WHERE ID = %s",
                (nova_quantidade, id_produto)
            )
            self.connection.commit()
            print("Quantidade atualizada com sucesso.")
        except Error as e:
            print(f"Erro ao atualizar quantidade: {e}")
        finally:
            if cursor:
                cursor.close()

    def remover_produto(self, id_produto):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Produtos WHERE ID = %s", (id_produto,))
            self.connection.commit()
            print("Produto removido com sucesso.")
        except Error as e:
            print(f"Erro ao remover produto: {e}")
        finally:
            if cursor:
                cursor.close()

    def registrar_venda(self, id_produto, quantidade_vendida):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT Quantidade FROM Produtos WHERE ID = %s", (id_produto,))
            produto = cursor.fetchone()

            if not produto:
                print(f"Erro: Produto com ID {id_produto} não encontrado.")
                return False
            
            quantidade_disponivel = produto['Quantidade']

            if quantidade_vendida > quantidade_disponivel:
                print(f"Erro: Quantidade insuficiente em estoque. Disponível: {quantidade_disponivel}")
                return False
            
            nova_quantidade = quantidade_disponivel - quantidade_vendida
            cursor.execute(
                "UPDATE Produtos SET Quantidade = %s WHERE ID = %s",
                (nova_quantidade, id_produto)
            )

            cursor.execute(
                "INSERT INTO Vendas (ID_Produto, Quantidade_Vendida) VALUES (%s, %s)",
                (id_produto, quantidade_vendida)
            )

            self.connection.commit()
            print("Venda registrada com sucesso e estoque atualizado.")
            return True
            
        except Error as e:
            print(f"Erro ao registrar venda: {e}")
            return False
        finally:
            if cursor:
                cursor.close()