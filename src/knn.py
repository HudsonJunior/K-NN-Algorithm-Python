from Exemplo import ExemploClass
import Helpers

def Classificar(B, X, k, listCLassesBase):

    exemplosList = []
    i = 0

    try:
        for E in B:

            distancia = Helpers.calculaDistancia(E, X)

            classeTrain = listCLassesBase[i]

            exemplosList.append(ExemploClass(classeTrain, distancia))
            
            i = i + 1
    
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
        
    except Exception as e:
        print("Ocorreu um problema ao determinar a classe mais frequente.\n", e)
  
