from connect import conn, encerra_conn

def main():

    connection = conn()
    cursor = connection.cursor()

    def insert_obra(ID_obra, titulo, ano_public, edicao, num_paginas, lingua, autor):
        cmd_insert = "INSERT INTO obras(ID_obra, titulo, ano_public, edicao, num_paginas, lingua, autor) VALUES (%s,%s,%s,%s,%s,%s,%s); "
        values = ID_obra, titulo, ano_public, edicao, num_paginas, lingua, autor
        cursor.execute(cmd_insert, values)
        connection.commit()
        print('dados inseridos com sucesso!')

    encerra_conn(connection)






if __name__ == "__main__":
    main()