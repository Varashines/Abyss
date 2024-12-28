class Error(Exception):
    pass

class dobException(Error):
    pass

year = int(input("Enter the DOB \n"))
age = 2024 - year

try:
    if age <= 30 and age>= 20:
        print("The age is valid")
    else:
        raise dobException
except dobException:
    print("The age is not Valid")
