import knn
import Helpers
import time

def main():

    print("Digite: nome do arquivo train + nome do arquivo test + k")

    try:

        fileNameTrain, fileNameTest, k = input().split(' ')

        typeFileTest, sizeFileTest = fileNameTest.split('_')

        typeFileTrain, sizeFileTrain = fileNameTrain.split('_')

        if Helpers.tiposValidos(typeFileTest, typeFileTrain) and Helpers.tamanhosValidos(sizeFileTest, sizeFileTrain):

            listDoubleBase, listClassesBase = Helpers.fileToList(fileNameTrain)

            listDoubleTest, listClassesTest = Helpers.fileToList(fileNameTest)

            i = 0
            count = 0
            
            for x in listDoubleTest:

                result = knn.Classificar(listDoubleBase, x, int(k), listClassesBase)

                print("Análise exemplo de teste", i)
                print("Classe preditada:", result, "\nClasse do exemplo:", listClassesTest[i])

            
                if result == listClassesTest[i]:
                    count = count+1
                    print("Sucesso na predição!\n")
                else:
                    print("Falha na predição!\n")


                i = i + 1

            print("sucesso:", count)
           
        else:
            print("Arquivos incompatíveis!")

    except Exception as e:
        print("Erro na função principal.\n", e)


if __name__ == "__main__":
    start_time = time.time()
    main()

    print('tempo de execução final:', time.time() - start_time)