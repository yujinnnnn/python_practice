import datetime

def weekday(mo,day):
    week = ["MON","TUE","WED","THU","FRI","SAT","SUN"] 
    return week[datetime.date(2020,mon,day).weekday()]

if __name__== "__main__":
    mon,day = [int(i) for i in input("월과 일을 입력 : ").split()]
    print(weekday(mon,day))