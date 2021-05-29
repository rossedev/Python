from Monitor import Monitor
from Teclado import Keyboard
from Raton import Mouse
from Computadora import Computer
from Orden import Order

monitor = Monitor("Hp", 34)
keyboard = Keyboard("Usb", "Genius")
mouse = Mouse("Usb", "Crack")
computer1 = Computer("Rose", monitor, keyboard, mouse)

monitor = Monitor("Acer", 28)
keyboard = Keyboard("Cable", "Genius")
mouse = Mouse("WiFi", "Crack")
computer2 = Computer("Print", monitor, keyboard, mouse)

monitor = Monitor("Mac", 18)
keyboard = Keyboard("Wi-Fi", "World")
mouse = Mouse("Usb", "Checken")
computer3 = Computer("Hello", monitor, keyboard, mouse)


computers = [computer1, computer2, computer3]

order = Order(computers)
print(order)