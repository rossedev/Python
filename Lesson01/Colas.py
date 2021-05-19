i = 0
cola = []
cola.append("Rosa")
cola.append("Daniel")
cola.append("Carlos")
cola.append("Karla")
cola.append("Tomas")

print("Cola:", cola)
while i < len(cola):
    cola.pop(0)
    if len(cola) > 0:
        print("Frente: ", cola[0])

print("Cola final:", cola)