for i in range (int(input("enter the current year : ")),int(input("enter the final year : "))) :
    if(i%4==0) and (i%100!=0) or (i%400==0) :
        print(i,"is a leap year")

