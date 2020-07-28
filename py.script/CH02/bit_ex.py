num1 =10; num2 =3
result1= num2 << 3
result2= num1 >> 3
print("{}\t{}".format(result1,result2))

num1 %= 4
result3 = num1**4
print('%d, %d'% (num1, result3))
 
result4 = result1 >= result3
result5 = result1 > 30 or result1 <= 10 and result1==24
print(result4,',',result5)