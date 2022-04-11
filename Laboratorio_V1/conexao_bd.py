import mysql.connector

class BancoDados():
    """
    Classe Banco da Dados, possui funções de conexão com o banco de dados,
    escrita de comandos SQL e leitura de resultados.
    """
    def conectar_banco():
        """
        Faz a conexão com o banco de dados.
        Argumentos:
            Nenhum
        Retorno:
            Banco de dados e cursor
        """        
        banco_dados = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1234",
            database="laboratorio_novo")
        cursor = banco_dados.cursor()
        return banco_dados, cursor

    def executar_sql(banco_dados, cursor, sql, *valores) -> None:
        """
        Executa comando SQL.
        Argumentos:
            banco_dados: Banco de dados
            cursor: Cursor
            sql: Comando SQL
            *valores: Valores para o comando SQL
        Retorno:
            Nenhum
        """
        cursor.execute(sql, *valores)
        banco_dados.commit()

    def obter_classes(cursor) -> list:
        """
        Obtêm classes de usuários disponíveis no Banco de Dados.
        Argumentos:
            cursor: Cursor
        Retorno:
            Lista de classes de usuários
        """
        cursor.execute("SELECT nomeClasse FROM classe")
        lista = cursor.fetchall()
        for index in range(len(lista)):
            lista[index] = lista[index][0]
        return lista

    def obter_usuarios(cursor) -> list:
        """
        Obtêm usuários disponíveis no Banco de Dados.
        Argumentos:
            cursor: Cursor
        Retorno:
            Lista de usuários
        """        
        cursor.execute("SELECT nomeUsuario FROM usuario")
        lista = cursor.fetchall()
        for index in range(len(lista)):
            lista[index] = lista[index][0]
        return lista
    
    def obter_equipamentos(cursor) -> list:
        """
        Obtêm equipamentos disponíveis no Banco de Dados.
        Argumentos:
            cursor: Cursor
        Retorno:
            Lista de equipamentos
        """
        cursor.execute("SELECT nomeEquipamento FROM equipamento")
        lista = cursor.fetchall()
        for index in range(len(lista)):
            lista[index] = lista[index][0]
        return lista

