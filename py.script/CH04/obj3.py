#함수의 중첩
#중첩 함수를 감싸는 함수를 외부 또는 부모함수라 함
def speak(text):
    def greet(h):
        return h.title() + '!!'
    print(greet(text))

speak('hi, nested dunction')

#greet 함수가 중첩(내부)함수로 외부에서 실행 시

def speak(text):
    def greet(h):
        return h.title()+'!!'
    return greet(text)

hi=speak('nice to meet you')
print(hi)

