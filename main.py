from connect import conn, encerra_conn

def main():

    connection = conn()
    cursor = connection.cursor()

    # CREATE
    def insert_obra(titulo, ano_public, edicao, num_paginas, lingua, autor):
        cmd_insert = "INSERT INTO obras(titulo, ano_public, edicao, num_paginas, lingua, autor) VALUES (%s,%s,%s,%s,%s,%s); "
        values = titulo, ano_public, edicao, num_paginas, lingua, autor
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
    def atualiza(autor_novo, ID_obra):
        cmd_update = f"UPDATE obras SET autor='{autor_novo}' WHERE ID_obra={ID_obra}"
        cursor.execute(cmd_update)
        connection.commit()
        print("titulo atualizado com sucesso")
        # dps tem q ver pra mudar as outras opções tb mas isso vc tem q se virar ok

    # DELETE
    def deleta(ID_obra):
        cmd_delete = f"DELETE FROM obras WHERE ID_obra='{ID_obra}'"
        cursor.execute(cmd_delete)
        connection.commit()
        print("obra deletada com sucesso")


    # insert_obra("eu robo", "10/04/1984", 3, 450, "português", "isaque neto")



    # atualiza('Isaac Asimov', 2)

    # seleciona()

    # deleta(2)
    encerra_conn(connection)






if __name__ == "__main__":
    main()