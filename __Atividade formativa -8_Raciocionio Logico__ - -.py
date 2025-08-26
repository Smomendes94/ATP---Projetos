import json

def menu_professores():


    print(f"Você escolheu essa opção:{op}")

    menu_operacional()

    codigo = input("Informe o codigo do professor:")

    professores.append({
        "codigo": codigo,
    })

    nome = input("Informe o nome do professor:")

    professores.append({
        "Codigo professor": nome,
    })

    cpf = input("Informe o cpf do professor:")

    professores.append({
        "cpf professor": cpf,
    })

    novo_cadastro = {
        "codigo": codigo,
        "Codigo professor": nome,
        "cpf professor": cpf,
    }

    salvar_arquivo(novo_cadastro, codigo)

    print(novo_cadastro)

def menu_matriculas():


    print(f"Você escolheu essa opção:{op}")

    menu_operacional()

    codigo = input("Informe o codigo da turma:")

    matriculas.append({
        "codigo": codigo,
    })

    codigo1 = input("Informe o codigo do estudante:")

    matriculas.append({
        "Codigo professor": codigo1,
    })

    novo_cadastro = {
        "codigo": codigo,
        "Codigo professor": codigo1,

    }

    salvar_arquivo(novo_cadastro, codigo)

    print(novo_cadastro)


def menu_disciplinas():

    print(f"Você escolheu essa opção:{op}")

    menu_operacional()

    nome = input("Informe o nome da disciplina:")

    disciplinas.append({
        "Nome": nome,
    })

    codigo = input("Informe o codigo disciplina:")

    disciplinas.append({
        "Codigo professor": codigo,
    })

    novo_cadastro = {
        "Nome": nome,
        "Codigo professor": codigo,

    }

    salvar_arquivo(novo_cadastro, codigo)

    print(novo_cadastro)

def menu_turmas():

    print(f"Você escolheu essa opção:{op}")

    menu_operacional()

    codigo = input("Informe o codigo da turma:")

    turmas.append({
        "Codigo": codigo,
     })

    codigo1 = input("Informe o codigo do professor:")

    turmas.append({
        "Codigo_professor": codigo1 ,
    })

    codigo2 = input("Informe o codigo da Disciplina:")

    turmas.append({
        "Codigo disciplina": codigo2,
    })

    novo_cadastro = {
        "Codigo": codigo,
        "Codigo professor": codigo1,
        "Codigo disciplina": codigo2,
    }

    salvar_arquivo(novo_cadastro,codigo)

    print(novo_cadastro)

def menu_principal():
    print("☺ Menu principal cadastro de estudantes ☺")

    print("♦(1)Estudante")
    print("♦(2)Turmas")
    print("♦(3)Disciplinas")
    print("♦(4)Matriculas")
    print("♦(5)Professores")
    print("♦(6)Menu principal")

    return input("Informe a opção desejada:")


def menu_operacional():
    # **** MENU DE OPERAÇOES / DADOS CADASTRAIS ****#

    print(f"☺☺☺ (Estudantes) Menu DE OPERAÇÔES ☺☺☺ Opção:{op}")
    print("♦(1)Incluir")
    print("♦(2)listar")
    print("♦(3)Atualizar")
    print("♦(4)Excluir")
    print("♦(5)Sair")

    return input("Informe a opção desejada:")


def menu_excluir():

    codigo = int(input("Informe o codigo do estudante:"))
    novo_estudante = {
        "codigo": codigo
    }
    estudantes.pop()

    ler_arquivo(codigo)

    for i in list([estudantes]):
        print(f"Você excluiu o codigo :{codigo}")

def menu_atualizar():
    print(f"Você escolheu essa opção:{op2}")

    codigo = int(input("Informe o codigo do estudante:"))
    novo_estudante = {

        "codigo": codigo
    }
    estudantes.pop()

    ler_arquivo(codigo)
    for codigo in list([estudantes]):
        print(f"Você atualizou o codigo :{codigo}")

def menu_incluir():

    print(f"Você escolheu essa opção:{op2}")

    nome = input("Informe o nome do estudante:")

    estudantes.append({
        "nome": nome,
    })

    cpf = input("Informe o cpf de estudante:")

    estudantes.append({
        "cpf": cpf,
    })

    codigo = input("Informe o codigo de estudante:")

    estudantes.append({
        "codigo": codigo,
    })

    novo_estudante = {
        "Nome" : nome,
        "cpf" : cpf,
        "codigo": codigo
    }

    salvar_arquivo(novo_estudante,nome)

    print(novo_estudante)

def menu_listar():

    print(f"Você escolheu essa opção:{op2}")

    for _ in list([estudantes]):
        ler_arquivo(_)
        print(f"Nomes na lista :{estudantes}")


    if estudantes == ():
        print("Lista com nomes Vazia!")

        return

def salvar_arquivo(lista_qualquer,nome_arquivo):
    with open(nome_arquivo,'w', encoding='utf - 8') as f:
     json.dump(lista_qualquer, f, ensure_ascii= False)


    return

def ler_arquivo(nome_arquivo):

     try:
        with open(nome_arquivo,'r') as f:
         lista_qualquer = json.load(f)

        return lista_qualquer

     except:
         return []



estudantes = [{"codigo": 1, "nome": "Lucas", "cpf": "999"},
              {"codigo": 2, "nome": "Pedro", "cpf": "555"},
              {"codigo": 3, "nome": "Carlos", "cpf": "3535"},
              {"codigo": 4, "nome": "Alex", "cpf": "0909"}]

professores = [{}]
turmas = [{}]
disciplinas = [{}]
matriculas = [{}]

while True:

    op = menu_principal()

    if op == "5":

     menu_professores()
     menu_operacional()

    elif op == "4":

     menu_matriculas()
     menu_operacional()

    elif op == "3":

     menu_disciplinas()
     menu_operacional()

    elif op == "2":

     menu_turmas()
     menu_operacional()

    elif op == "1":

        print(f"Você escolheu essa opção:{op}")

        while True:

            op2 = menu_operacional()

            if op2 == "4":

                menu_excluir()

            elif op2 == "3":

                menu_atualizar()

            elif op2 == "1":

                menu_incluir()

            elif op2 == "2":

                menu_listar()

            elif op2 == "5":
                break
            else:
                print("Voçe digitou uma opção INVALIDA")

    elif op == "6":
        print("Voltar ao menu.")
        break
    else:
        print("Voçe digitou uma opção INVALIDA")




