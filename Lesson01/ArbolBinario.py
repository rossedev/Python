class Node:
    def __init__(self, name=None, cedula=None, left=None, right=None):
        self.name = name
        self.cedula = cedula
        self.left = left
        self.right = right

    def __str__(self):
        return "The name is: " + self.name + " and your Cedula is: " + str(self.cedula)


class aBinary:
    def __init__(self):
        self.root = None

    def add(self, node):

        if self.root is None:
            self.root = node
        else:
            aux = self.root
            father = None

            while aux is not None:
                father = aux
                if int(node.cedula) >= int(aux.cedula):
                    aux = aux.right
                else:
                    aux = aux.left
            if int(node.cedula) >= int(father.cedula):
                father.right = node
            else:
                father.left = node

    def preOrder(self, element):
        if element is not None:
            print(element)
            self.preOrder(element.left)
            self.preOrder(element.right)

    def postOrder(self, element):
        if element is not None:
            self.postOrder(element.left)
            self.postOrder(element.right)
            print(element)

    def inOrder(self, element):
        if element is not None:
            self.inOrder(element.left)
            print(element)
            self.inOrder(element.right)


    def getRoot(self):
        return self.root


if __name__ == "__main__":
    ab = aBinary()
    while True:
        print("-----Menu-----\n" +
              "1. Add\n" +
              "2. PreOrder\n" +
              "3. PostOrder\n " +
              "4. InOrder\n " +
              "5. Exit")
        option = int(input("Enter the option: "))

        if option == 1:
            name = input("enter de name: ")
            cedula = input("enter de cedula: ")
            node = Node(name, cedula)
            ab.add(node)
        elif option == 2:
            print("Pre Order: ")
            ab.preOrder(ab.getRoot())
        elif option == 3:
            print("Post Order: ")
            ab.postOrder(ab.getRoot())
        elif option == 4:
            print("In Order: ")
            ab.inOrder(ab.getRoot())
        elif option == 5:
            break
