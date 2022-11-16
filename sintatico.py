import re

def teste_sintatico(nome_arquivo):
    arquivo = open(nome_arquivo,'r')

    numero = re.compile(r'<numero\$>')
    palavra=re.compile(r'<palavra\$>')
    dinheiro=re.compile(r'<dinheiro\$>')
    id=re.compile(r'<ID (\S+)>')
    op=re.compile(r'<OP (\S+)>')
    inteiro=re.compile(r'<numero (\d+)>')
    string=re.compile(r'<palavra (\S+)>')
    aux_numero=0
    aux_palavra=0
    aux_dinheiro=0
    aux_id=0
    aux_op=0
    tokens = []
    erros =[]

    for l in arquivo.readlines():
        l = l.replace('\n','')       
        for token in l.split(','):
            if numero.search(token):
                if(aux_numero==1 or aux_palavra==1 or aux_dinheiro==1):
                    erros.append("Erro Sintatico posição: "+str(l.index(token)+1)+", numero$: "+token)
                aux_palavra=0
                aux_dinheiro=0 
                aux_numero=1
                #print(token)
            elif palavra.search(token):
                if(aux_numero==1 or aux_palavra==1 or aux_dinheiro==1):
                    erros.append("Erro Sintatico posição: "+str(l.index(token)+1)+", palavra$: "+token)
                aux_palavra=1
                aux_numero=0
                aux_dinheiro=0 
                #print(token)
            elif dinheiro.search(token):
                if(aux_numero==1 or aux_palavra==1 or aux_dinheiro==1):
                    erros.append("Erro Sintatico posição: "+str(l.index(token)+1)+", Palavra Reservada: "+token)
                aux_palavra=0
                aux_numero=0
                aux_dinheiro=1 
                #print(token)
            elif id.search(token):
                if(aux_numero==1 or aux_palavra==1 or aux_dinheiro==1):
                    aux_palavra=0
                    aux_numero=0
                    aux_dinheiro=0
                    if(aux_op==1):
                        aux_id=1
                    else:
                        aux_id=0                    
                aux_id+=1
                if(aux_id>2):
                    erros.append("Erro Sintatico posição: "+str(l.index(token)+1)+", ID: "+token)
                # else:
                #     print(token)
            elif op.search(token):
                aux_id=1
                aux_op=1         
                #print(token)
            elif inteiro.search(token):
                aux_id=1
                #print(token)
            elif string.search(token):
                aux_id=1
                #print(token)

    if(len(erros)==0):
        print("\nSem erro sintatico\n")
        return True
    else:
        print(erros)
        return False
        