from connect import conn, encerra_conn
from inputs.insert import insert, insert_obra
from inputs.select import seleciona
from inputs.update import autor_inp, lingua_inp, edicao_inp, anopubli_inp, npag_inp, title_inp
from inputs.delete import delete 

def main():

    connection = conn()
    cursor = connection.cursor()

    print("\n")
    print("Seja bem vindo ao sistema da biblioteca!")
    print("ainda não está completo :(")
    print("mas já temos um CRUD com banco de dados funcional! :>")
    while True:
        try:    
            opt = int(input("você gostaria de: \n" \
            "1 - cadastrar uma obra\n" \
            "2 - ver as obras no banco\n" \
            "3 - atualizar alguma obra\n" \
            "4 - deletar uma obra\n" \
            "5 - sair\n"))

            if opt == 1:
                insert()

            elif opt == 2:
                seleciona()

            elif opt == 3:
                while True:
                    update = int(input("o que gostaria de atualizar?\n" \
                    "1 - titulo\n" \
                    "2 - ano de publicação\n" \
                    "3 - edição\n" \
                    "4 - número de páginas\n" \
                    "5 - língua\n" \
                    "6 - autor\n"))
                    
                    if update == 1:
                        title_inp()
                    elif update == 2:
                        anopubli_inp()
                    elif update == 3:
                        edicao_inp()
                    elif update == 4:
                        npag_inp()
                    elif update == 5:
                        lingua_inp()
                    elif update == 6:
                        autor_inp()
                    else:
                        print("insira um valor válido!")
                        continue

            elif opt == 4:
                delete()

            elif opt == 5:
                break;
        
            else:
                print("coloca um numero certo ai boboca")
                continue
           
        except ValueError: 
            print("coloca numero direito bocó")
            continue

    encerra_conn(connection)


if __name__ == "__main__":
    main()