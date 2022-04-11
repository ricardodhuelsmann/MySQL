import tkinter
from conexao_bd import BancoDados

banco, cursor = BancoDados.conectar_banco()
lista_classes = BancoDados.obter_classes(cursor)

class JanelaEquipamento(tkinter.Tk):
    """
    Classe de cadastro de equipamento
    """
    def __init__(self):
        super().__init__()
        #Define características da janela
        self.geometry("400x200")
        self.title('Cadastro de equipamento')

        #Frame 1
        self.frame_1 = tkinter.Frame(self)
        self.frame_1.pack(padx=10, pady=10)
        self.label_nome = tkinter.Label(self.frame_1, text='Nome:')
        self.label_nome.grid(row=0, column=0, padx=5, pady=5)
        self.input_nome = tkinter.Entry(self.frame_1, width=30)
        self.input_nome.grid(row=0, column=1, padx=5, pady=5)

        #Frame 2
        self.frame_2 = tkinter.Frame(self)
        self.frame_2.pack(padx=10, pady=10)
        self.botao_cadastrar = tkinter.Button(self.frame_2, text='Cadastrar', command=self.cadastrar_equipamento)
        self.botao_cadastrar.grid(row=0, column=0, padx=5, pady=5)
    
    def cadastrar_equipamento(self) -> None:
        """
        Cadastra equipamento no Banco de Dados.
        Argumentos:
            Nenhum
        Retorno:
            Nenhum
        """        
        nome = self.input_nome.get()
        print(f'Nome: {nome}')
        self.input_nome.delete(0, tkinter.END)
        BancoDados.executar_sql(banco, cursor, f"INSERT INTO equipamento SET nomeEquipamento = '{nome}';")


if __name__ == "__main__":
    janela_equipamento = JanelaEquipamento()
    janela_equipamento.mainloop()
