from Exemplo import ExemploClass
import Helpers

def Classificar(B, X, k):
    exemplosList = []
    print('X: ', X)
    try:
        for E in B:
            sampleTrain = E.split(',')
            print('sampletrain: ', sampleTrain)
            lastIndex = len(sampleTrain) - 1

            classeTrain = sampleTrain.pop(lastIndex)

            P =  Helpers.stringListToDouble(sampleTrain) 

            distancia = Helpers.calculaDistancia(P, X)

            exemplosList.append(ExemploClass(classeTrain, distancia))
    
        ordeneredList = sorted(exemplosList, key=lambda exemplo:exemplo.distancia)
    
        kList = ordeneredList[:k]
       

        return _classeMaisFrequente(kList)
    
    except Exception as e:
        print("Ocorreu um problema ao classificar o exemplo.\n", e)

def _classeMaisFrequente(List): 
    classes = []
    
    try:
        
        for i in List:
            classes.append(i.classe)
        print('1: ', classes)
        counter = 0
        classeFrequente = classes[0]

        
        for i in classes: 
            curr_frequency = classes.count(i) 
            if(curr_frequency > counter): 
                counter = curr_frequency 
                classeFrequente = i 
        print('2: ', classeFrequente)   
        classesMaisFrequentes = []
        
        for j in classes:
            if (classes.count(j) == counter) and (j not in classesMaisFrequentes):
                classesMaisFrequentes.append(j)
        print('3: ', classesMaisFrequentes)
        if(len(classesMaisFrequentes) == 1):
            return classeFrequente

        else:
            return classesMaisFrequentes[0]
        
    except Exception as e:
        print("Ocorreu um problema ao determinar a classe mais frequente.\n", e)
  
