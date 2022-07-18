
def obtainCSVvalues(pCSV):
    csv = pCSV
    aux = []
    aux2 = []
    M = []
    i = 0
    bol = False
    while i < len(csv):
            
        if ord(csv[i]) >= 65 and ord(csv[i]) <=90:
            bol = True
    
        if ord(csv[i]) != 59 and bol == True and csv[i] != "\r":
            if ord(csv[i]) == 44:
                aux.append(",")
            else:
                aux.append(csv[i])
            
        if ord(csv[i]) == 59 and bol == True or csv[i] == "\r":
    
                string = "".join(aux)
                aux2.append(string)
                aux = []
                
        if ord(csv[i]) == 92 and aux != []:
                string = "".join(aux)
                aux2.append(string)
                aux = []
        
        if csv[i] == "\r":
            if aux2 != []:
                M.append(aux2)
                aux2 = []
                bol = False
        
        i+=1
    
    return M