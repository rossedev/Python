import os

stack = []
top = -1

while True:
    print("________________Menu________________")
    print("Select an option")
    print("1. Insert data \n" +
          "2. Delete data \n" +
          "3. Empty Stack? \n" +
          "4. View last value entered in the stack\n" +
          "5. View the number of nodes in the stack \n" +
          "6. Show Stack \n" +
          "7. Empty Stack\n" +
          "8. Exit \n")
    option = int(input("Enter the value: "))

    if option == 1:
        if top < 5:
            stack.append(input("Enter the value to store in the node: "))
            top += 1
        else:
            print("Ops! Full Stack")
    elif option == 2:
        if top > -1:
            print("Node deleted correctly", stack.pop())
            top -= 1
        else:
            print("Ops! Empty Stack")
    elif option == 3:
        if top == -1:
            print("Ops! Empty Stack")
        else:
            print("Yeah! The Stack isn't empty")
    elif option == 4:
        if top != -1:
            print("The last node is:", stack[-1])
        else:
            print("Ops! Empty Stack")
    elif option == 5:
        if top != -1:
            print("The stack size is:", len(stack))
        else:
            print("Ops! Empty Stack")
    elif option == 6:
        if top != -1:
            print("The Stack es:", stack)
        else:
            print("Ops! Empty Stack")
    elif option == 7:
        while top != -1:
            stack.pop()
            top -= 1
        print("Empty Stack, yeahhh!")

    elif option == 8:
        break
    else:
        print("Ops! Try again")
        os.system("pause")
        os.system("cls")