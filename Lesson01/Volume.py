class Box:
    def __init__(self, long, width,high):
        self.long = long
        self.width = width
        self.high = high

    def vol(self):
        return self.long * self.high * self.width


longInput = int(input('Provides the long: '))
widthInput = int(input('Provides the width: '))
highInput = int(input('Provides the high: '))

volume = Box(longInput, widthInput, highInput)
print("The volume is:", volume.vol())
