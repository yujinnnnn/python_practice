def greet(obj):
    hello = obj("Hi, This is a python class")
    print(hello)

def hello(text):
    return text.lower()

greet(hello)