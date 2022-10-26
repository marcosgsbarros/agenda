import pyodbc


def conexao_dados():
    conexao = pyodbc.connect("Driver={SQL Server};"
                    "Server=DESKTOP-DQJD276\SQLEXPRESS;"
                    "Database=Agenda;")
    cursor = conexao.cursor()
    return cursor

def cadastro_sql(nome,telefone,email):
    cursor = conexao_dados()
    cursor.execute(f"INSERT INTO Contatos (Nome,Telefone,Email) VALUES ('{nome}','{telefone}','{email}')")
    cursor.commit()

def pesquisar_contato_sql(nome):
    cursor = conexao_dados()
    cursor.execute(f"SELECT * FROM Contatos WHERE nome LIKE '%{nome}%'")
    contato = cursor.fetchall()
    return contato

def mostrar_contatos_sql():
    cursor = conexao_dados()
    cursor.execute("SELECT * FROM Agenda.dbo.Contatos")
    contatos = cursor.fetchall()
    return contatos

def editar_contato_sql(id_contato, nome, telefone, email):
    cursor = conexao_dados()
    cursor.execute(f"UPDATE Contatos SET Nome = '{nome}' WHERE Id_contato = {id_contato}")
    cursor.execute(f"UPDATE Contatos SET Telefone = '{telefone}' WHERE Id_contato = {id_contato}")
    cursor.execute(f"UPDATE Contatos SET Email = '{email}' WHERE Id_contato = {id_contato}")
    cursor.commit()

def excluir_contato_sql(id_contato):
    cursor = conexao_dados()
    cursor.execute(f"DELETE FROM Contatos WHERE Id_contato = {id_contato}")
    cursor.commit()
    return cursor

