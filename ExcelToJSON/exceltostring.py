
def ObtainExcelValues(pExcelparsed):
    excelparsed = pExcelparsed
    aux = []
    aux2 = []
    M = []
    cont = 0
    for i in range(len(excelparsed)+1):
        print(i)
        if len(aux2) == 3:
            M.append(aux2)
            aux2 = []
        if i == len(excelparsed):
            break
        
        if ord(excelparsed[i]) != 32:
            if ord(excelparsed[i]) >= 65 and ord(excelparsed[i]) <= 90:
                aux.append(excelparsed[i])
            elif ord(excelparsed[i]) >= 97 and ord(excelparsed[i]) <=122:
                aux.append(excelparsed[i])
            elif ord(excelparsed[i]) >= 128 and ord(excelparsed[i]) <=165:
                aux.append(excelparsed[i])
                
        if ord(excelparsed[i]) == 32 and ord(excelparsed[i-1]) != 32 and i !=0:
            resultado = "".join(aux)
            aux2.append(resultado)
            aux = []


    
    print('valor total' + str(len(excelparsed)))
    return M