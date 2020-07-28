money, c500, c100, c50, c10 = 0,0,0,0,0
money = int(input("Enter money to exchange >>"))

c500 = money//500
money = money%500
c100 = money//100
money = money%100
c50 = money//50
money = money%50
c10 = money//10
money = money%10 

print(f'500원 {c500}개, 100원 {c100}개, 50원 {c50}개, 10원 {c10}개, 나머지는 {money}원')