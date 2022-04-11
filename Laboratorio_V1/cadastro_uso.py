import tkinter
import datetime
from conexao_bd import BancoDados

banco, cursor = BancoDados.conectar_banco()
lista_classes = BancoDados.obter_classes(cursor)
lista_usuarios = BancoDados.obter_usuarios(cursor)
lista_equipamentos = BancoDados.obter_equipamentos(cursor)


class JanelaUsoEquipamento(tkinter.Tk):
    """
    Classe de cadastro de uso de equipamento
    """
    def __init__(self):
        super().__init__()
        #Define características da janela
        self.geometry("400x200")
        self.title('Cadastro de uso de equipamento')

        #Frame 1
        self.frame_1 = tkinter.Frame(self)
        self.frame_1.pack(padx=10, pady=10)
        self.label_nome = tkinter.Label(self.frame_1, text='Usuario:')
        self.label_nome.grid(row=0, column=0, padx=5, pady=5)
        self.entrada_usuario = tkinter.StringVar(self)
        self.entrada_usuario.set('Escolha um usuário')
        self.input_usuario = tkinter.OptionMenu(self.frame_1, self.entrada_usuario, *lista_usuarios)
        self.input_usuario.grid(row=0, column=1, padx=5, pady=5)

        #Frame 2
        self.frame_2 = tkinter.Frame(self)
        self.frame_2.pack(padx=10, pady=10)
        self.label_equipamento = tkinter.Label(self.frame_2, text='Equipamento:')
        self.label_equipamento.grid(row=0, column=0, padx=5, pady=5)
        self.entrada_equipamento = tkinter.StringVar(self)
        self.entrada_equipamento.set('Escolha um equipamento')
        self.input_equipamento = tkinter.OptionMenu(self.frame_2, self.entrada_equipamento, *lista_equipamentos)
        self.input_equipamento.grid(row=0, column=1, padx=5, pady=5)

        #Frame 3
        self.frame_3 = tkinter.Frame(self)
        self.frame_3.pack(padx=10, pady=10)
        self.botao_cadastrar = tkinter.Button(self.frame_3, text='Cadastrar', command=self.cadastrar_uso)
        self.botao_cadastrar.grid(row=0, column=0, padx=5, pady=5)
    
    def cadastrar_uso(self) -> None:
        """
        Cadastra uso do equipamento no Banco de Dados.
        Argumentos:
            Nenhum
        Retorno:
            Nenhum
        """
        nome = self.entrada_usuario.get()
        equipamento = self.entrada_equipamento.get()
        print(f'Nome: {nome}')
        print(f'Classe: {equipamento}')
        self.entrada_usuario.set("Escolha um usuário")
        self.entrada_equipamento.set("Escolha um equipamento")
        data = datetime.datetime.today().strftime('%Y-%m-%d')
        print(data)
        BancoDados.executar_sql(banco, cursor, 
            f"INSERT INTO usoEquipamento SET data = '{data}', "
            f"equipamento_idEquipamento = (SELECT idEquipamento FROM equipamento WHERE nomeEquipamento = '{equipamento}'), "
            f"usuario_idUsuario = (SELECT idUsuario FROM usuario WHERE nomeUsuario = '{nome}');")


if __name__ == "__main__":
    janela_uso_equipamento = JanelaUsoEquipamento()
    janela_uso_equipamento.mainloop()
