from datetime import datetime

def DayOftheweek(m,d):
    t = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    week_day = datetime(2016,m,d).weekday()
    return str(t[week_day])


print(DayOftheweek(5,24))
