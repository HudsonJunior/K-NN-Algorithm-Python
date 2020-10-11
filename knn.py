import Exemplo
import Helpers
def Classificar(B, X, k):
    exemplosList = []

    for E in B:
        sampleTrain = E.split(',')

        lastIndex = len(sampleTrain)

        classeTrain = sampleTrain[lastIndex - 1]
        P =  Helpers.stringListToDouble(sampleTrain.pop(lastIndex)) 

        distancia = calculaDistancia(P, X)

        exemplo = Exemplo.ExemploClass(classeTrain, distancia)

        exemplosList.append(exemplo)
    
    ordeneredList = sorted(exemplosList, key= lambda exemplo: exemplo.distancia)

    kList = ordeneredList[:k]
    

    return classeMaisFrequente(kList)

        
def calculaDistancia(P, Q):
    soma = 0

    for i in range(0 , len(P) - 1):
        absValue = + (P[i] - Q[i])

        soma += absValue
    
    return soma

def classeMaisFrequente(List): 
    classes = []
    for i in List:
        classes.append(i.classe)

    counter = 0
    classeFrequente = classes[0]

      
    for i in classes: 
        curr_frequency = classes.count(i) 
        if(curr_frequency > counter): 
            counter = curr_frequency 
            classeFrequente = i 
        
    classesMaisFrequentes = []
    
    for j in classes:
        if (classes.count(j) == counter) and (j not in classesMaisFrequentes):
            classesMaisFrequentes.append(j)

    if(len(classesMaisFrequentes) == 1):
        return classeFrequente

    else:
        return classesMaisFrequentes[0]
  
