class Country():

    def __init__(self,Phone,Name,Country_code):
        self.Phone = Phone
        self.Name = Name
        self.Country_code = Country_code

class State(Country):
    def __init__(self,Phone,Name,Country_code, state):
        super().__init__(Phone,Name,Country_code)
        self.state = state

class Pincode(State):
    def __init__(self,Phone,Name,Country_code,state,District, pincode):
        super().__init__(Phone,Name,Country_code,state)
        self.District = District
        self.pincode = pincode
    def Contactdetails(self):
        print("Contact Details")
        print(f"{self.District}, {self.state}, {self.Name}, {self.pincode}")
        print(f"{self.Country_code} {self.Phone}")

# country = Country(8074453829,'India','+91')
# state = State(8074453829,'India','+91','Andhra')
pincode = Pincode(8074453829,'India','+91','Andhra','Srikakulam','532185')
pincode.Contactdetails()
print(pincode.pincode)


# This example demonstrates the benefits of multilevel inheritance over having all parameters in a single class:

# 1. Organization and Reusability:  Inheritance allows us to organize related data and behavior into distinct classes.  We can reuse the `Country` and `State` classes in other parts of our code that might not need pincode information. This avoids redundancy and improves maintainability.

# 2. Flexibility and Extensibility:  We can easily add new levels of detail (e.g., City or Street) without modifying existing classes. This hierarchical structure is more adaptable to changing requirements.  If we had all the data in a single class, adding a new level would require modifying that class, potentially affecting all code that uses it.


# 3. Data Encapsulation and Clarity:  By separating data into different classes, we improve code readability and reduce complexity. Each class is responsible for a specific level of information, making it easier to understand and maintain.  A single large class with all parameters would be harder to manage and understand.


# 4. Polymorphism (Not shown directly in this example): Inheritance enables polymorphism, which allows objects of different classes to be treated as objects of a common type.  This is especially useful when dealing with collections or when you want to write generic functions that can operate on objects of related types.
