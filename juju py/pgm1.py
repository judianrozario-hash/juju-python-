startYear=int(input("enter the start year:"))
endYear=int(input("enter the year:"))
print("list of leap year:")
for year in range(startYear,endYear):
     if((year%4==0)and (year%100!=0)or (year%400==0)):
       print(year)
