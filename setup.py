import sqlite3
conn = sqlite3.connect('bancodedados.db')
cursor = conn.cursor()

def tab_doencas():
    cursor.execute('CREATE TABLE doencas(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, doenca TEXT(30) NOT NULL, sintomas TEXT(100) NOT NULL);')


def buscar(sintomas):
    num = 0
    num_sintomas = len(sintomas)
    retorno = []
    while(num < num_sintomas):
        cursor.execute('SELECT * FROM tab_doencas WHERE sintomas LIKE "%'+sintomas[num]+'%"')
        for coluna in cursor.fetchall():
            retorno.insert(num, coluna[1])
        num += 1
    return retorno


def cadastro_doencas(doenca, sintomas):
    cursor.execute('INSERT INTO tab_doencas(doenca, sintomas) VALUES (?,?)', (doenca, sintomas))
    conn.commit()


def lista():
    cursor.execute('SELECT * FROM tab_doencas')
    for coluna in cursor.fetchall():
        print(coluna[1],'-' , coluna[2])


def cadastro_doencas(doenca, sintomas):
    cursor.execute('INSERT INTO doencas(doenca, sintomas) VALUES (?,?)', (doenca, sintomas))
    conn.commit()


def altera_doenca(id_doenca):
    cursor.execute('SELECT * FROM doencas WHERE id = ?', (id_doenca))
    for coluna in cursor.fetchall():
        doenca_anterior = coluna[1]
    if alteracao_campo == 'doenca':
        cursor.execute("UPDATE doenca SET doenca = ? WHERE id = ?", (alteracao, id_doenca))
    if alteracao_campo == 'sintomas':
        cursor.execute("UPDATE sintomas SET sintomas = ? WHERE id = ?", (alteracao, id_doenca))
    conn.commit()


def altera_sintomas(id_doenca, campo_alteracao, alteracao):
    cursor.execute('SELECT * FROM doencas WHERE id = ? OR id = ?', (id_doenca, id_doenca))
    for coluna in cursor.fetchall():
        sintoma_anterior = coluna[2]
        sintomas = sintoma_anterior.split(',')
        qtd_sintomas = len(sintomas)
        num=0
        while num < qtd_sintomas:
            if campo_alteracao == sintomas[num]:
                sintomas[num] = alteracao
                break
            num+=1
        num=0
        sintomas_novo = ''
        while num < qtd_sintomas:
            if num == 0:
                sintomas_novo += sintomas[num]
            else:
                sintomas_novo += ','+sintomas[num]
            num+=1
        cursor.execute("UPDATE doencas SET sintomas = ? WHERE id = ?", (sintomas_novo, id_doenca))
        conn.commit()


def remove_sintomas(id_doenca, campo_alteracao):
    cursor.execute('SELECT * FROM doencas WHERE id = ? OR id = ?', (id_doenca, id_doenca))
    for coluna in cursor.fetchall():
        sintoma_anterior = coluna[2]
        sintomas = sintoma_anterior.split(',')
        qtd_sintomas = len(sintomas)
        num=0
        while num < qtd_sintomas:
            if campo_alteracao == sintomas[num]:
                ondeta = num
                break
            num+=1
        num=0
        sintomas_novo = ''
        while num < qtd_sintomas:
            if ondeta != num:
                if num == 0:
                    sintomas_novo += sintomas[num]
                else:
                    sintomas_novo += ','+sintomas[num]
            num+=1
        cursor.execute("UPDATE doencas SET sintomas = ? WHERE id = ?", (sintomas_novo, id_doenca))
        conn.commit()


def cadastra_sintomas(id_doenca, novo_sintoma):
    cursor.execute('SELECT * FROM doencas WHERE id = ? OR id = ?', (id_doenca, id_doenca))
    for coluna in cursor.fetchall():
        sintoma_anterior = coluna[2]
        sintomas_novo = sintoma_anterior + ',' + novo_sintoma
        cursor.execute("UPDATE doencas SET sintomas = ? WHERE id = ?", (sintomas_novo, id_doenca))
        conn.commit()
