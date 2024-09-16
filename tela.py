import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, \
    QHBoxLayout, QDialog, QComboBox, QSpinBox


class TelaPrincipal(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Treino")
        self.setGeometry(250, 90, 900, 600)

        # Definindo um estilo global para todos os botões QPushButton
        self.setStyleSheet('QPushButton {background-color:#00a1ff;font:bold; font-size:15px}')

        # Criando o botão "Cadastrar" com um estilo próprio
        self.btn_cadastrar = QPushButton(self)
        self.btn_cadastrar.setText('Cadastrar')
        self.btn_cadastrar.setFixedSize(150, 50)
        self.btn_cadastrar.clicked.connect(self.cadastrar_produto)

        # Outros botões com o estilo global definido em setStyleSheet
        self.btn_produtos = QPushButton(self)
        self.btn_produtos.setText('Produtos')
        self.btn_produtos.setFixedSize(150, 50)
        self.btn_produtos.clicked.connect(self.listar_produtos)

        self.btn_estoque = QPushButton(self)
        self.btn_estoque.setText('Estoque')
        self.btn_estoque.setFixedSize(150, 50)
        self.btn_estoque.clicked.connect(self.estoque)

        self.btn_itens_repor = QPushButton(self)
        self.btn_itens_repor.setText('Itens para Repor')
        self.btn_itens_repor.setFixedSize(150, 50)

        # Layout dos botões
        layout_botao = QHBoxLayout()  # Corrigido: Sem "self" no QHBoxLayout
        layout_botao.addWidget(self.btn_cadastrar)
        layout_botao.addWidget(self.btn_produtos)
        layout_botao.addWidget(self.btn_estoque)
        layout_botao.addWidget(self.btn_itens_repor)

        # Campos de entrada
        self.label_nome = QLabel(self)
        self.label_nome.setText('Nome: ')
        self.edt_nome = QLineEdit(self)

        # Layout para os campos do formulário
        layout_formulario = QVBoxLayout()
        layout_formulario.addWidget(self.label_nome)
        layout_formulario.addWidget(self.edt_nome)

        # Layout principal, combinando o layout dos botões e do formulário
        layout_principal = QVBoxLayout()
        layout_principal.addLayout(layout_botao)  # Adiciona o layout dos botões
        layout_principal.addLayout(layout_formulario)  # Adiciona o layout dos campos de entrada

        # Definir o layout no widget central
        self.componentes = QWidget(self)
        self.componentes.setLayout(layout_principal)
        self.setCentralWidget(self.componentes)

    # Método para abrir a janela de cadastro de produto
    def cadastrar_produto(self):
        formulario = CadastraProduto(self)
        formulario.exec_()

    def listar_produtos(self):
        listar_produto = Produtos(self)
        listar_produto.exec_()
    def estoque(self):
        estoque = Estoque(self)

class Estoque(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Estoque')
        self.setFixedSize(500,500)


from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QComboBox, QSpinBox, QPushButton, QVBoxLayout, QHBoxLayout

class CadastraProduto(QDialog):
    produtos = []

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle('Cadastrar')
        self.setFixedSize(600, 500)

        self.setStyleSheet('font-size:15px; font:bold')

        # Função para adicionar categorias
        def opcoes_categories():
            categorias = [
                'Limpeza',
                'Escritório',
                'Manutenção',
                'Peças de Máquinas',
                'API',
                'Matéria Prima',
                'Construção',
                'Produção'
            ]
            self.categoria.addItems(categorias)

        # Criação dos widgets
        self.label_nome_produto = QLabel('Nome do Produto: ')
        self.nome_produto = QLineEdit()
        self.nome_produto.setFixedSize(400, 25)

        self.categoria_produto = QLabel('Categoria: ')
        self.categoria = QComboBox()
        self.categoria.setFixedSize(150, 30)

        # Adicionando as categorias ao QComboBox
        opcoes_categories()

        # Parte de quantidade do produto
        self.label_quantidade = QLabel('Quantidade: ')
        self.quantidade = QSpinBox()  # Usando QSpinBox para aceitar apenas números inteiros
        self.quantidade.setFixedSize(100, 30)
        self.quantidade.setRange(0, 1000)  # Limite de 0 a 1000 como exemplo

        # Layout para os widgets de categoria e quantidade
        layout_horizontal_categoria_quantidade = QHBoxLayout()
        layout_horizontal_categoria_quantidade.setSpacing(15)  # Reduzir o espaçamento entre os widgets
        layout_horizontal_categoria_quantidade.setContentsMargins(10, 0, 100, 150)  # Reduzir margens

        layout_horizontal_categoria_quantidade.addWidget(self.categoria_produto)
        layout_horizontal_categoria_quantidade.addWidget(self.categoria)
        layout_horizontal_categoria_quantidade.addWidget(self.label_quantidade)
        layout_horizontal_categoria_quantidade.addWidget(self.quantidade)

        layout_horizontal_nome = QHBoxLayout()
        layout_horizontal_nome.setSpacing(5)  # Reduzir o espaçamento entre os widgets
        layout_horizontal_nome.setContentsMargins(10, 0, 100, 0)  # Reduzir margens

        layout_horizontal_nome.addWidget(self.label_nome_produto)
        layout_horizontal_nome.addWidget(self.nome_produto)

        # Layout principal
        layout = QVBoxLayout()
        layout.setSpacing(10)  # Reduzir o espaçamento entre os layouts
        layout.setContentsMargins(0, 100, 0, 0)  # Reduzir margens

        layout.addLayout(layout_horizontal_nome)
        layout.addLayout(layout_horizontal_categoria_quantidade)

        # Botão para finalizar o cadastro
        self.btn_cadastrar = QPushButton('Cadastrar')
        self.btn_cadastrar.setFixedSize(300, 35)

        layout_botao = QHBoxLayout()
        layout_botao.addStretch()
        layout_botao.addWidget(self.btn_cadastrar)
        layout_botao.setContentsMargins(0,100,0,0)
        layout_botao.addStretch()

        layout.addLayout(layout_botao)
        self.setLayout(layout)



class Produtos(QDialog):  # Corrigido: Produtos agora herda de QDialog
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Produtos')
        self.setFixedSize(500, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = TelaPrincipal()
    tela.show()
    sys.exit(app.exec_())
