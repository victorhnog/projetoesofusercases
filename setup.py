import sqlite3
conn = sqlite3.connect('bancodedados.db')
cursor = conn.cursor()

def cria_tabela():
    cursor.execute('CREATE TABLE tab_doencas (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, doenca TEXT(30) NOT NULL, sintomas(100) TEXT NOT NULL)')

def remove_doença(o_que_vai_deletar):
    cursor.execute('DELETE FROM tab_doencas WHERE id =?', o_que_vai_deletar)
    conn.commit()

cria_tabela()
