class Apple:
    manufacturer = "Apple Inc."
    contactwebiste = "www.apple.com/contact"

    def contactDetails(self):
        print("To contact us, please log on to ", self.contactwebiste)

class Macbook(Apple):
    def __init__(self):
        self.yearofManufacture = 2017

    def manufactureDetails(self):
        print(f"This Macbook was manufactured in the year {self.yearofManufacture} by {self.manufacturer} ")

macbook = Macbook()
macbook.manufactureDetails()
macbook.contactDetails()
