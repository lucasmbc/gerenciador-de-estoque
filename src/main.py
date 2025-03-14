import flet as ft
from database.db import Database

class GerenciamentoEstoqueApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.scroll = True        
        self.page.title = "Sistema de Gerenciamento de Estoque"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.db = Database()
        self.db.conectar()
        self.criar_interface()

    def criar_interface(self):
        # Campos de entrada para cadastrar produto
        self.nome_field = ft.TextField(label="Nome")
        self.descricao_field = ft.TextField(label="Descrição")
        self.quantidade_field = ft.TextField(label="Quantidade")
        self.preco_field = ft.TextField(label="Preço")
        self.cadastrar_button = ft.ElevatedButton("Cadastrar Produto", height=50, width=200, on_click=self.cadastrar_produto_click)

        # Lista de produtos
        self.produtos_list = ft.Column()

        # Campos de entrada para atualizar quantidade
        self.id_atualizar_field = ft.TextField(label="ID do Produto")
        self.nova_quantidade_field = ft.TextField(label="Nova Quantidade")
        self.atualizar_button = ft.ElevatedButton("Atualizar Quantidade", height=50, width=200, on_click=self.atualizar_quantidade_click)

        # Campos de entrada para remover produto
        self.id_remover_field = ft.TextField(label="ID do Produto")
        self.remover_button = ft.ElevatedButton("Remover Produto", height=50, width=200, on_click=self.remover_produto_click)

        # Campos de entrada para registrar venda
        self.id_venda_field = ft.TextField(label="ID do Produto")
        self.quantidade_venda_field = ft.TextField(label="Quantidade Vendida")
        self.venda_button = ft.ElevatedButton("Registrar Venda", height=50, width=200, on_click=self.registrar_venda_click)

        self.page.add(
            ft.Column(                
                width=900,
                controls=[
                            ft.Text("Cadastrar Novo Produto", size=20),
                            self.nome_field,
                            self.descricao_field,
                            self.quantidade_field,
                            self.preco_field,
                            self.cadastrar_button,
                            ft.Divider(),
                            ft.Text("Consultar Produtos Cadastrados", size=20),
                            ft.ElevatedButton("Consultar Produtos", height=50, width=200, on_click=self.consultar_produtos_click),
                            self.produtos_list,
                            ft.Divider(),
                            ft.Text("Atualizar Quantidade de Produto", size=20),
                            self.id_atualizar_field,
                            self.nova_quantidade_field,
                            self.atualizar_button,
                            ft.Divider(),
                            ft.Text("Remover Produto", size=20),
                            self.id_remover_field,
                            self.remover_button,
                            ft.Divider(),
                            ft.Text("Registrar Venda", size=20),
                            self.id_venda_field,
                            self.quantidade_venda_field,
                            self.venda_button
                ]
            )
        )

    def limpar_campos(self):
        self.nome_field.value = ""
        self.descricao_field.value = ""
        self.quantidade_field.value = ""
        self.preco_field.value = ""
        self.id_atualizar_field.value = ""
        self.nova_quantidade_field.value = ""
        self.id_remover_field.value = ""
        self.id_venda_field.value = ""
        self.quantidade_venda_field.value = ""
        self.page.update()

    def cadastrar_produto_click(self, e):
        self.db.cadastrar_produto(
            self.nome_field.value,
            self.descricao_field.value,
            int(self.quantidade_field.value),
            float(self.preco_field.value)
        )
        self.page.open(ft.SnackBar(ft.Text("Produto cadastrado com sucesso!")))
        self.page.update()
        self.limpar_campos()        

    def consultar_produtos_click(self, e):
        produtos = self.db.consultar_produtos()
        self.produtos_list.controls.clear()
        for produto in produtos:
            self.produtos_list.controls.append(
                ft.Text(f"ID: {produto['ID']}, Nome: {produto['Nome']}, Descrição: {produto['Descricao']}, Quantidade: {produto['Quantidade']}, Preço: {produto['Preco']}")
            )
        self.page.update()

    def atualizar_quantidade_click(self, e):
        self.db.atualizar_quantidade(
            int(self.id_atualizar_field.value),
            int(self.nova_quantidade_field.value)
        )
        self.page.open(ft.SnackBar(ft.Text("Quantidade atualizada com sucesso!")))
        self.page.update()
        self.limpar_campos()

    def remover_produto_click(self, e):
        self.db.remover_produto(int(self.id_remover_field.value))
        self.page.open(ft.SnackBar(ft.Text("Produto removido com sucesso!")))
        self.page.update()
        self.limpar_campos()

    def registrar_venda_click(self, e):
        id_produto = int(self.id_venda_field.value)
        quantidade_vendida = int(self.quantidade_venda_field.value)

        if self.db.registrar_venda(id_produto, quantidade_vendida):
            self.page.open(ft.SnackBar(ft.Text("Venda registrada com sucesso!")))
        else:
            self.page.open(ft.SnackBar(ft.Text("Erro ao registrar venda: quantidade insuficiente ou produto não encontrado.")))        

        self.page.update()
        self.limpar_campos()

ft.app(target=GerenciamentoEstoqueApp)
