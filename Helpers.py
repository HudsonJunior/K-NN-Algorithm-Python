def stringListToDouble(List):
    listDouble = []

    for i in List:
        listDouble.append(float(i))
    
    return listDouble

def tiposValidos(tipoTest, tipoTrain):
    if tipoTest != 'test' or tipoTrain != 'train':
        return False
    
    return True

def tamanhosValidos(sizeTest, sizeTrain):
    if sizeTest != sizeTrain:
        return False

    return True