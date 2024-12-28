my_list = [1,2,3,4,5,6]
iterator = iter(my_list)
print(type(iterator))

try:
    print(next(iterator))
except StopIteration:
    print("There are no elements in the iterator")
