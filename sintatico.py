import re


def teste_sintatico(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')

    numero = re.compile(r'numero\$')
    palavra = re.compile(r'palavra\$')
    dinheiro = re.compile(r'dinheiro\$')
    maoe = re.compile(r'Maoe')
    id = re.compile(r'ID (\S+)')
    op = re.compile(r'OP (\S+)')
    inteiro = re.compile(r'int (\d+)')
    string = re.compile(r'string (\S+)')
    r_for = re.compile(r'rodarodajequiti')
    r_if = re.compile(r'estacertodisso')
    r_else = re.compile(r'possoconfirmar')
    aux_numero = 0
    aux_palavra = 0
    aux_dinheiro = 0
    aux_maoe = 0
    aux_int=0
    aux_string=0
    aux_id = 0
    aux_op = 0
    aux_for = 0
    aux_if = 0
    aux_else = 0
    tokens = []
    erros = []

    # texto=arquivo.read()
    # result = re.sub(r"[\([{})\]]", "", texto)
    # for token in result.split(','):
    # print(token)
    for l in arquivo.readlines():
         l = l.replace('\n', '')
         for token in l.split(','):
            if numero.search(token):# se o token atual for igual o anterior das reservadas consta erro sintatico
                if(aux_numero == 1 or aux_palavra == 1 or aux_dinheiro == 1 or aux_maoe == 1):
                    erros.append("Erro Sintatico posição: " +str(token.index(token)+1)+", numero$: "+token)
                aux_palavra = 0
                aux_dinheiro = 0
                aux_maoe = 0
                aux_numero = 1  # Salva o token anterior
                    # print(token)
            elif palavra.search(token):
                if(aux_numero == 1 or aux_palavra == 1 or aux_dinheiro ==1 or aux_maoe==1):#se o token atual for igual o anterior das reservadas consta erro sintatico
                    erros.append("Erro Sintatico posição: " +str(token.index(token)+1)+", palavra$: "+token)
                aux_palavra = 1  # Salva o token anterior
                aux_numero = 0
                aux_dinheiro = 0
                aux_maoe = 0
                    # print(token)
                # se o token atual for igual o anterior das reservadas consta erro sintatico
            elif dinheiro.search(token):
                if(aux_numero == 1 or aux_palavra == 1 or aux_dinheiro ==1 or aux_maoe==1):
                    erros.append("Erro Sintatico posição: "+str(token.index(token)+1)+", Palavra Reservada: "+token)
                    aux_palavra = 0
                    aux_numero = 0
                    aux_maoe = 0
                    aux_dinheiro = 1  # Salva o token anterior
                    # print(token)
                # se o token atual for igual o anterior das reservadas consta erro sintatico
            elif maoe.search(token):
                    if(aux_numero == 1 or aux_palavra == 1 or aux_dinheiro ==1 or aux_maoe==1):
                        erros.append(
                            "Erro Sintatico posição: "+str(token.index(token)+1)+", Palavra Reservada: "+token)
                    aux_palavra = 0
                    aux_numero = 0
                    aux_maoe = 1  # Salva o token anterior
                    aux_dinheiro = 0
                    aux_string=0
                    aux_int=0
                    # print(token)
            elif id.search(token):
                    # se o id vier depois de uma palavra reservada, ele reseta as palavras reservadas para utlizar novamente
                    if(aux_numero == 1 or aux_palavra == 1 or aux_dinheiro ==1 or aux_maoe==1):
                        aux_palavra = 0
                        aux_numero = 0
                        aux_dinheiro = 0
                        aux_maoe = 0
                        if (aux_op == 1):
                            aux_id = 1
                            aux_for = 0
                            aux_int = 0
                            aux_string=0
                        else:
                            aux_int = 0
                            aux_string=0
                            aux_for = 0
                            aux_id = 0
                    aux_id += 1
                    aux_int = 0
                    aux_string=0
                    aux_for = 0
                    if (aux_id > 2):
                        erros.append("Erro Sintatico posição: " +
                                     str(token.index(token)+1)+", ID: "+token)
                    # else:
                       # print(token)
                # se for um operador ele coloca 1 no id para não dar erro no seguinte token
            elif op.search(token):
                    aux_id = 1
                    aux_op = 1
                    aux_string=0
                    aux_int=0
                    # print(token)
            elif inteiro.search(token):
                    if(aux_numero == 1 or aux_palavra == 1 or aux_dinheiro ==1 or aux_int==1 or aux_string==1):
                        erros.append("Erro Sintatico posição: "+str(token.index(token)+1)+", Int: "+token)
                    aux_int=1
                    aux_id=1
                    aux_string=1
                    # print(token)
            elif string.search(token):
                    if(aux_numero == 1 or aux_palavra == 1 or aux_dinheiro ==1 or aux_int==1 or aux_string==1):
                        erros.append("Erro Sintatico posição: "+str(token.index(token)+1)+", String: "+token)
                    aux_id = 1
                    aux_string=1
                    aux_int=1
                    # print(token)
            elif r_for.search(token):
                    if(aux_numero == 1 or aux_dinheiro == 1 or aux_palavra ==1 or aux_maoe==1 or aux_if==1):
                        erros.append("Erro Sintatico posição: " +
                                     str(token.index(token)+1)+", Palavra Reservada: "+token)
                    aux_for = 1
                    aux_id = 1
            elif r_if.search(token):
                    if(aux_numero == 1 or aux_dinheiro == 1 or aux_palavra ==1 or aux_maoe==1):
                        erros.append("Erro Sintatico posição: " +
                                     str(token.index(token)+1)+", Palavra Reservada: "+token)
                    aux_if = 1
                    aux_id = 1
            elif r_else.search(token):
                    if(aux_numero == 1 or aux_dinheiro == 1 or aux_palavra ==1 or aux_maoe==1):
                        erros.append("Erro Sintatico posição: " +
                                     str(token.index(token)+1)+", Palavra Reservada: "+token)
                    aux_else = 1
                    aux_id = 1

    if (len(erros) == 0):
        print("\nSem erro sintatico\n")
        return True
    else:
        print(erros)
        return False
