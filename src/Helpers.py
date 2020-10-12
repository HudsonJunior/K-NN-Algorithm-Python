def stringListToDouble(List):
    try:
        listDouble = []

        for i in List:
            newFloat = float(i)
            listDouble.append(newFloat)
        
        return listDouble

    except Exception as e:
        print("Ocorreu um erro ao converter a lista de strings para double.\n", e)

def tiposValidos(tipoTest, tipoTrain):
    if tipoTest != 'test' or tipoTrain != 'train':
        return False
    
    return True

def tamanhosValidos(sizeTest, sizeTrain):
    if sizeTest != sizeTrain:
        return False

    return True

def calculaDistancia(P, Q):
    try:
        soma = 0

        for i in range(0 , len(P) - 1):
            absValue = abs(P[i] - Q[i])

            soma += absValue
        
        return float(soma)
    
    except Exception as e:
        print("Ocorreu um erro ao calcular a distancia entre os pontos.\n", e)
