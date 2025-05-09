from connect import conn, encerra_conn

connection = conn()
cursor = connection.cursor()

    # CREATE
def insert_obra(titulo, ano_public, edicao, num_paginas, lingua, autor):
    cmd_insert = "INSERT INTO obras(titulo, ano_public, edicao, num_paginas, lingua, autor) VALUES (%s,%s,%s,%s,%s,%s); "
    values = titulo, ano_public, edicao, num_paginas, lingua, autor
    cursor.execute(cmd_insert, values)
    connection.commit()
    print('dados inseridos com sucesso!')


def insert():
    titulo = input("Qual o titulo da obra? \n")

    data_publicacao = input("Qual a data de publicação dela? xx/xx/xxxx \n")

    edicao = int(input("Qual a edição dela? \n"))

    lingua = input("Qual a linguagem da obra? \n")

    numero_paginas = int(input("Quantas paginas tem? \n"))

    autor = input("quem é o autor? \n")

    return insert_obra(titulo, data_publicacao, edicao, numero_paginas, lingua, autor)

  



