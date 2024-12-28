class OperatingSystem:
    multitasking = True
    name = "Mac OS"

class Apple:
    webiste = "www.apple.com"
    name = "Apple"

class Macbook(OperatingSystem, Apple):
    def __init__(self) -> None:
        if self.multitasking == True:
            print(self.name)
            print(f"This is a multi tasking system. Visit {self.webiste} for more details")

macbook = Macbook()
