def uppercase(obj):
    def wrapper():
        origin_result = obj()
        modi_result = origin_result.upper()
        return modi_result
    return wrapper

@uppercase
def greet():
    return "Hello"

@uppercase
def hi():
    return f"Long time no see"

print(greet())
print(hi())