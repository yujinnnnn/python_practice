def uppercase(obj):
    def wrapper(*args, **kwargs): #*args: 여분의 위치인자를 튜플로, **kwargs: 여분의 키워드 인자를 딕셔너리로 수집
        print(f'Trace:calling {obj.__name__}()', end='')
        print(f'with {args},{kwargs}')
        original_result = obj(*args, **kwargs)
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def intro(name, greeting):
    return f'Hi, {name}, {greeting}'

print(intro("Mee", "Have a good time"))