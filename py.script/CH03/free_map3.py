def outside(word):
    def inside(text):
        print(word,text)
    return inside

fist = outside("주먹")
butterfly = outside("나비")

fist("이 운다.")
butterfly("가 날아간다.")