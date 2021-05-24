try:
    file = open("prueba.txt", "w")
    file.write("\nAdd information in file \n")
    file.write("My name es Rose, nice to meet you :3\n")
except Exception as e:
    print(e)
finally:
     file.close()

