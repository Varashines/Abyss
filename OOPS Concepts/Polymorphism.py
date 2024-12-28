class Employee:
    def workingHours(self):
        self.numberofWorkingHours = 40

    def displayWorkingHours(self):
        print(self.numberofWorkingHours)

class Trainee(Employee):
    def workingHours(self):
        self.numberofWorkingHours = 48

    def resetWorkingHours(self):
        super().workingHours()

employee = Employee()
employee.workingHours()
print("Number of working hours of employee: ", end = '')
employee.displayWorkingHours()
trainee = Trainee()
trainee.workingHours()
print("Number of working hours of trainee: ", end = '')
trainee.displayWorkingHours()
trainee.resetWorkingHours()
print("Number of working hours of trainee: ", end = '')
trainee.displayWorkingHours()
