import tkinter
from cadastro_usuario import JanelaUsuario
from cadastro_equipameto import JanelaEquipamento
from cadastro_uso import JanelaUsoEquipamento


class JanelaPrincipal(tkinter.Tk):
    """
    Classe Principal
    """
    def __init__(self):
        super().__init__()
        #Define características da janela
        self.geometry("400x200")
        self.title('Uso de equipamentos - Laboratório')

        #Frame Principal
        self.frame_principal = tkinter.Frame(self)
        self.frame_principal.pack(padx=10, pady=10)

        #Adiciona botões
        self.botao_1 = tkinter.Button(self.frame_principal, text='Adicionar usuário', bd=1, width=20, height=3, command=self.janela_adicionar_usuario)
        self.botao_1.grid(row=0, column=0, padx=12, pady=15)
        self.botao_2 = tkinter.Button(self.frame_principal, text='Adicionar equipamento', bd=1, width=20, height=3, command=self.janela_adicionar_equipamento)
        self.botao_2.grid(row=0, column=1, padx=12, pady=15)
        self.botao_3 = tkinter.Button(self.frame_principal, text='Cadastrar uso', bd=1, width=20, height=3, command=self.janela_cadastrar_uso)
        self.botao_3.grid(row=1, column=0, padx=12, pady=15)
        self.botao_4 = tkinter.Button(self.frame_principal, text='Sair', bd=1, width=20, height=3, command=self.destroy)
        self.botao_4.grid(row=1, column=1, padx=12, pady=15)


    def janela_adicionar_usuario(self) -> None:
        """
        Abre janela para adicionar usuário.
        Argumentos:
            Nenhum
        Retorno:
            Nenhum
        """
        self.janela_usuario = JanelaUsuario()
        self.janela_usuario.mainloop()


    def janela_adicionar_equipamento(self) -> None:
        """
        Abre janela para adicionar equipamentos.
        Argumentos:
            Nenhum
        Retorno:
            Nenhum
        """
        self.janela_equipamento = JanelaEquipamento()
        self.janela_equipamento.mainloop()

    def janela_cadastrar_uso(self) -> None:
        """
        Abre janela para registrar uso de equipamentos.
        Argumentos:
            Nenhum
        Retorno:
            Nenhum
        """
        self.janela_uso_equipamento = JanelaUsoEquipamento()
        self.janela_uso_equipamento.mainloop()


if __name__ == "__main__":
    janela_principal = JanelaPrincipal()
    janela_principal.mainloop()