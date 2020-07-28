print("%10d %10d"%(23, 1234))
print("%10s %10.3f"%("우리나라", 35.6789))
print("%-10d %-10s"%(1234, "Python"))
print("%020d" %128)
print("%-010d"% 123)
 
print() #줄 바꿈
name="Computer"
print("name: %4s"%name) # %s는 문자열 출력해주는 코드이다. 4칸보다 많아도 출력해줌
print("%.4s"%name)
print("%15.6s"%name)

print()
char='C'
print("%c"%char) 
print("%c"%"한")
print("%c" %67) # %c는 문자 1개를 출력하는 코드이기 때문에 숫자는 출력 불가