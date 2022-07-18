from ExcelToJSON.config import EXCEL_COLUMNS

def ObtainExcelValues(pExcelparsed,pColumns = EXCEL_COLUMNS):
    excelparsed = pExcelparsed
    aux = []
    aux2 = []
    M = []
    #cont = 0
    #numbol = False
    
    for i in range(len(excelparsed)):
        
        if ord(excelparsed[i]) != 32:
            
            if ord(excelparsed[i]) >= 65 and ord(excelparsed[i]) <= 90:
                aux.append(excelparsed[i])
            # Codigo comentado para evitar numeraciones. El motivo es que al parsear el excel, te saca al final la fila en la que está.
            
            #elif ord(excelparsed[i]) >= 48 and ord(excelparsed[i]) <=57:
            #    if numbol == False:
            #        aux.append(excelparsed[i])
            #        cont+=1
            #    elif numbol == False and cont == 1:
            #        aux.append(excelparsed[i])
            #        numbol = True
            #        cont = 0
            #    else:
            #        numbol = False
                    
            elif ord(excelparsed[i]) >= 97 and ord(excelparsed[i]) <=122:
                aux.append(excelparsed[i])
            elif ord(excelparsed[i]) >= 128 and ord(excelparsed[i]) <=255:
                aux.append(excelparsed[i])
            elif ord(excelparsed[i]) == 95:
                aux.append(" ")
            elif ord(excelparsed[i]) == 45 or ord(excelparsed[i]) == 44:
               aux.append(excelparsed[i])

        if ord(excelparsed[i]) == 32 and ord(excelparsed[i-1]) != 32 and i !=0 or i == len(excelparsed)-1:
            
            resultado = "".join(aux)
            aux2.append(resultado)
            aux = []
            
        if len(aux2) == pColumns:
            M.append(aux2)
            aux2 = []
    
    return M