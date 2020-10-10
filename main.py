import knn

def tiposValidos(tipoTest, tipoTrain):
    if tipoTest != 'test' or tipoTrain != 'train':
        return False
    
    return True

def tamanhosValidos(sizeTest, sizeTrain):
    if sizeTest != sizeTrain:
        return False

    return True

def main():
    print("Digite: nome do arquivo train + nome do arquivo test + k")


    fileNameTrain, fileNameTest, k = input().split(' ')

    typeFileTest, sizeFileTest = fileNameTest.split('_')

    typeFileTrain, sizeFileTrain = fileNameTrain.split('_')

    if tiposValidos(typeFileTest, typeFileTrain) and tamanhosValidos(sizeFileTest, sizeFileTrain):
        Base = open(fileNameTrain, 'r')

        Test = open(fileNameTest, 'r')
        
        i = 1
        for x in Test:
            sampleTest = x.split(',')

            lastIndex = len(sampleTest)

            classeTest = sampleTest[lastIndex - 1]
            X = sampleTest.pop(lastIndex)  

            result = knn.Classificar(Base, X, k)

            print("Análise exemplo de teste", i)
            print("Classe preditada:", result, "\nClasse do exemplo:", classeTest)

            if result == classeTest:
                print("Sucesso na predição!")
            else:
                print("Falha na predição!")

            i = i + 1

    else:
        print("Arquivos incompatíveis!")


main()