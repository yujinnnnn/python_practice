def speak(volume):
    def whisper(text):
        return text.lower()+'....'
    def yell(text):
        return text.upper()+'!!'
    if volume > 0.5:
        return yell
    else:
        return whisper
    
volume=float(input("Input volume, 0.0~1.0 >>"))
get_speak=speak(volume)
print(get_speak("Hello, Python Program"))