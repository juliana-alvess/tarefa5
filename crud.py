import sqlite3

conexao = sqlite3.connect('database.db')

def inserir(dados):
    conexao.execute('INSERT INTO tabela (campo1, campo2) VALUES (?, ?)', (dados['campo1'], dados['campo2']))
    conexao.commit()

def listar():
    return conexao.execute('SELECT * FROM tabela').fetchall()

def procurar_por_id(id):
    return conexao.execute('SELECT * FROM tabela WHERE id = ?', (id,)).fetchone()

def alterar(id, novos_dados):
    conexao.execute('UPDATE tabela SET campo1 = ?, campo2 = ? WHERE id = ?', (novos_dados['campo1'], novos_dados['campo2'], id))
    conexao.commit()


def apagar(id):
    conexao.execute('DELETE FROM tabela WHERE id = ?', (id,))
    conexao.commit()


if __name__ == "__main__":
    
    conexao.execute('''CREATE TABLE IF NOT EXISTS tabela (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        campo1 TEXT NOT NULL,
                        campo2 TEXT NOT NULL)''')

    dados = {'campo1': 'valor1', 'campo2': 'valor2'}

    
    inserir(dados)
    print("Após Inserir:")
    print(listar())


    print("Procurar pelo ID 1:")
    print(procurar_por_id(1))

    # Alterar
    alterar(1, {'campo1': 'novo_valor1', 'campo2': 'novo_valor2'})
    print("Após Alterar:")
    print(listar())

    # Apagar
    apagar(1)
    print("Após Apagar:")
    print(listar())

    conexao.close()
