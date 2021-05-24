try:
    file = open("prueba.txt", "r")
    #lee todo el archivo
    #print(file.read())

    #lee solamente dos caracteres
    #print(file.read(2))

    #lee solamente una linea
    #print(file.readline())

    #itera el archivo
    #for line in file:
    #    print(line)

    #lee todas las lienas
    #print(file.readlines())

    #acceder a una lista determinada
    #print(file.readlines()[1])

    #Abrimos nuevo archivo
    file2 = open("copia.txt", "w")
    file2.write(file.read())

except Exception as e:
    print(e)
finally:
     file.close()
     file2.close()

