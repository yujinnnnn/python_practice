a = ord('A') #ord함수는 문자상수를 아스키코드값으로 변경해주는 함수, type은 int
mask = 0x0f

print("%x & %x = %x" % (a, mask, a&mask))
print("%X | %X = %X" % (a, mask, a|mask))

mask = ord('a') - ord('A') 
b= a^mask
print("%c ^ %d= %c" % (a,mask,b))
a=b^mask
print("%c ^ %d = %c" % (b, mask, a))

a=12345
print(~a)
print(~a +1)