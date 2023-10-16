# Sanu K Joseph
class Time:
    def __init__(self):
        self.h=int(input("Enter the hour:"))
        self.m=int(input("Enter the minute:"))
        self.s=int(input("Enter the second:"))
    def __add__(self,time2):
        hour =self.h + time2.h
        minute =self.m + time2.m
        second  =self.s + time2.s
        if hour >=24:
            hour=hour%24
        if minute >=60:
            hour =hour+int(minute/60)
            minute=minute%60   
        if second >=60:
            minute =minute + int(second/60)
            second =second%60  
        print('Total time: {} hour {} minutes and {} seconds'.format(hour,minute,second))
                 
print("First time")
time1=Time()
print("Second time")   
time2=Time()    
print("************")    
time1.__add__(time2)
print("************")  