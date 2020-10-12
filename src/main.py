import knn
import Helpers

def main():
    print("Digite: nome do arquivo train + nome do arquivo test + k")

    try:

        fileNameTrain, fileNameTest, k = input().split(' ')

        typeFileTest, sizeFileTest = fileNameTest.split('_')

        typeFileTrain, sizeFileTrain = fileNameTrain.split('_')

        if Helpers.tiposValidos(typeFileTest, typeFileTrain) and Helpers.tamanhosValidos(sizeFileTest, sizeFileTrain):
            Base = open(fileNameTrain, 'r')

            Test = open(fileNameTest, 'r')
            
            i = 1
            for x in Test:
                sampleTest = x.split(',')

                lastIndex = len(sampleTest) - 1

                classeTest = sampleTest.pop(lastIndex)

                X = Helpers.stringListToDouble(sampleTest)
                print(X)
                result = knn.Classificar(Base, X, int(k))

                print("Análise exemplo de teste", i)
                print("Classe preditada:", result, "\nClasse do exemplo:", classeTest)

                if result == classeTest:
                    print("Sucesso na predição!\n")
                else:
                    print("Falha na predição!\n")

                if i == 10:
                    break

                i = i + 1

            Base.close()

            Test.close()

        else:
            print("Arquivos incompatíveis!")

    except Exception as e:
        print("Erro na função principal.\n", e)


if __name__ == "__main__":
    main()