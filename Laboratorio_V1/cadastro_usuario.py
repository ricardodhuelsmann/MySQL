import tkinter
from conexao_bd import BancoDados

banco, cursor = BancoDados.conectar_banco()
lista_classes = BancoDados.obter_classes(cursor)

class JanelaUsuario(tkinter.Tk):
    """
    Classe de cadastro de usuário
    """
    def __init__(self):
        super().__init__()
        #Define características da janela
        self.geometry("400x200")
        self.title('Cadastro de usuários')

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
        self.label_classe = tkinter.Label(self.frame_2, text='Classe:')
        self.label_classe.grid(row=0, column=0, padx=5, pady=5)
        self.classe = tkinter.StringVar(self)
        self.classes = lista_classes
        self.classe.set('Escolha uma classe')
        self.input_classe = tkinter.OptionMenu(self.frame_2, self.classe, *self.classes)
        self.input_classe.grid(row=0, column=1, padx=5, pady=5)


        #Frame 3
        self.frame_3 = tkinter.Frame(self)
        self.frame_3.pack(padx=10, pady=10)
        self.botao_cadastrar = tkinter.Button(self.frame_3, text='Cadastrar', command=self.cadastrar_usuario)
        self.botao_cadastrar.grid(row=0, column=0, padx=5, pady=5)
    
    def cadastrar_usuario(self) -> None:
        """
        Cadastra usuário no Banco de Dados.
        Argumentos:
            Nenhum
        Retorno:
            Nenhum
        """
        nome = self.input_nome.get()
        classe = self.classe.get()
        BancoDados.executar_sql(banco, cursor, 
            f"INSERT INTO usuario SET nomeUsuario = '{nome}',"
            f"classe_idClasse = (SELECT idClasse FROM classe WHERE nomeClasse = '{classe}');")
        self.input_nome.delete(0, tkinter.END)
        self.classe.set('Escolha uma classe')


if __name__ == "__main__":
    janela_usuario = JanelaUsuario()
    janela_usuario.mainloop()
