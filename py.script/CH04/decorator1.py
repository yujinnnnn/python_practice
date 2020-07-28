#base
def null_hi(obj):
    return obj

def greet():
    return "Hello!" 

greet = null_hi(greet)
greet()

#decorater
def null_hi(obj):
    name = input("Input your name >> ")
    print(f'{name}', end='')
    return obj

@null_hi # = greet = null_hi(greet)
def greet():
    return "Hello@"

print(greet())