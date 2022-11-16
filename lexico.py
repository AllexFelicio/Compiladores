## definindo o afd principal para processar e categorizar os tokens
import os
import re
import sintatico as sin

T_KEYWORDS_RESERVADO = ["<palavra$>","<numero$>","<dinheiro$>","rodarodajequiti","estacertodisso","possoconfirmar"]
T_OP = "<OP %s>"
T_INT = "<numero %s>"
T_STRING = "<palavra %s>"
T_IDENTIF = "<ID %s>"

#seleciona o exercicio para testar analisadores
exercicio='ex2.x'

regex=re.compile(r"^[a-zA-Z].*$")
regex_num=re.compile(r"^[0-9]+$")
regex_letra=re.compile(r"^[a-zA-Z]+$")
regex_string= re.compile(r'"(.*?)"')
regex_op=re.compile(r"!?=|[<>]=?")
regex_mat=re.compile(r"(\\d*|[+*/().-]|np\\d+|\\s+)*")

def afd_principal(token):
    
    if token == "palavra$":
        return T_KEYWORDS_RESERVADO[0]
    elif token =="numero$":
        return T_KEYWORDS_RESERVADO[1]
    elif token =="dinheiro$":
        return T_KEYWORDS_RESERVADO[2]
    elif token =="rodarodajequiti": #for
        return T_KEYWORDS_RESERVADO[3] 
    elif token =="estacertodisso": #if
        return T_KEYWORDS_RESERVADO[4]  
    elif token =="possoconfirmar": #else
        return T_KEYWORDS_RESERVADO[5]
    elif re.fullmatch(regex_mat,token):
        return T_OP % token
    elif re.fullmatch(regex_op,token):
        return T_OP % token
    elif re.fullmatch(regex, token):   
        return T_IDENTIF % token
    elif re.fullmatch(regex_num,token):
        return T_INT % token
    elif re.fullmatch(regex_string,token):
        return T_STRING % token

    return None
    
arquivo = open(exercicio,'r')
for l in arquivo.readlines():
    l = l.replace('\n','') # remove a quebra de linha
    tokens = []
    for token in l.split():
        result_lexico = open('result.txt','a')
        tokens.append(afd_principal(token))
    result_lexico.write(str(tokens)+'\n')        
    print(tokens)
result_lexico.close()

resposta = sin.teste_sintatico("result.txt")
os.remove("result.txt")

if(resposta==True):
    arquivo.close()
    arquivo = open(exercicio,'r')
    aux_simbolo=""
    aux_valor=[]

    for j in arquivo.readlines():
        j = j.replace('\n','') # remove a quebra de linha
        for token in j.split():
            if re.fullmatch(regex_num,token):
                aux_valor.append(token)      
            elif re.fullmatch(regex_mat,token):
                aux_simbolo=token
#aux para fazer contas
    mult=1
    soma=0

    for i in aux_valor:
        if(aux_simbolo=="*"):
            mult=mult*int(i)
        if(aux_simbolo=="+"):
            soma=soma+int(i)

    if(aux_simbolo=="*"):
        print("Produto: "+str(mult))
    if(aux_simbolo=="+"):
        print("Soma: ",soma)






