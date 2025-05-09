from connect import conn, encerra_conn
from inputs.insert import insert, insert_obra
from inputs.select import seleciona
from inputs.update import autor_inp, lingua_inp, edicao_inp, anopubli_inp, npag_inp, title_inp
from inputs.delete import delete 

def main():

    connection = conn()
    cursor = connection.cursor()


    # insert()

    # autor_inp()
    # lingua_inp()
    # edicao_inp()
    # npag_inp()
    # anopubli_inp()
    # title_inp()

    # delete()

    seleciona()


    # atualiza('Isaac Asimov', 2)

    # seleciona()

    encerra_conn(connection)






if __name__ == "__main__":
    main()