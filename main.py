from connect import conn, encerra_conn
from inputs.insert import insert, insert_obra
from inputs.select import seleciona
from inputs.update import autor_inp, lingua_inp, edicao_inp, anopubli_inp, npag_inp, title_inp
from inputs.delete import delete 

def main():

    connection = conn()
    cursor = connection.cursor()

    opcoes_principais = {
        1: insert,
        2: seleciona,
        3: "menu updates",
        4: delete,
        5: "sair"
    }

    opcoes_update = {
        1: title_inp,
        2: anopubli_inp,
        3: edicao_inp,
        4: npag_inp,
        5: lingua_inp,
        6: autor_inp
    }

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

            if opt not in opcoes_principais:
                print("Opção inválida! Tente novamente.")
                continue

            acao = opcoes_principais[opt]

            if acao == "sair":
                break
            elif acao == "menu updates":
                    while True:
                        try:
                            update_opt = int(input("o que gostaria de atualizar?\n" \
                            "1 - titulo\n" \
                            "2 - ano de publicação\n" \
                            "3 - edição\n" \
                            "4 - número de páginas\n" \
                            "5 - língua\n" \
                            "6 - autor\n"
                            "7 - Voltar\n"))
                            
                            if update_opt == 7:
                                break
                            elif update_opt in opcoes_update:
                                opcoes_update[update_opt]()  
                            else:
                                print("Opção inválida!")
                                continue

                        except ValueError:
                            print("Digite um número válido!")
            else:
                acao()
           
        except ValueError: 
            print("coloca numero direito bocó")
            continue

    encerra_conn(connection)


if __name__ == "__main__":
    main()