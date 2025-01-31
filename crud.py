import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('database.db')

# Função para inserir
def inserir(dados):
    conexao.execute('INSERT INTO tabela (campo1, campo2) VALUES (?, ?)', (dados['campo1'], dados['campo2']))
    conexao.commit()

# Função para listar
def listar():
    return conexao.execute('SELECT * FROM tabela').fetchall()

# Função para procurar pelo ID
def procurar_por_id(id):
    return conexao.execute('SELECT * FROM tabela WHERE id = ?', (id,)).fetchone()

# Função para alterar
def alterar(id, novos_dados):
    conexao.execute('UPDATE tabela SET campo1 = ?, campo2 = ? WHERE id = ?', (novos_dados['campo1'], novos_dados['campo2'], id))
    conexao.commit()

# Função para apagar
def apagar(id):
    conexao.execute('DELETE FROM tabela WHERE id = ?', (id,))
    conexao.commit()

# Exemplo de uso
if __name__ == "__main__":
    dados = {'campo1': 'valor1', 'campo2': 'valor2'}
    inserir(dados)
    print(listar())
    print(procurar_por_id(1))
    alterar(1, {'campo1': 'novo_valor1', 'campo2': 'novo_valor2'})
    apagar(1)
    conexao.close()
