from connect import conn, encerra_conn

def main():

    connection = conn()
    cursor = connection.cursor()

    # CREATE
    def insert_obra(ID_obra, titulo, ano_public, edicao, num_paginas, lingua, autor):
        cmd_insert = "INSERT INTO obras(ID_obra, titulo, ano_public, edicao, num_paginas, lingua, autor) VALUES (%s,%s,%s,%s,%s,%s,%s); "
        values = ID_obra, titulo, ano_public, edicao, num_paginas, lingua, autor
        cursor.execute(cmd_insert, values)
        connection.commit()
        print('dados inseridos com sucesso!')

    # READ
    def seleciona():
        cmd_select = "SELECT ID_obra, titulo, ano_public, edicao, num_paginas, lingua, autor FROM obras;"
        cursor.execute(cmd_select)
        acoes = cursor.fetchall()
        for acao in acoes:
            print(acao)
        return acao

    # UPDATE
    encerra_conn(connection)






if __name__ == "__main__":
    main()