print("Leap Year")
year = int(input("Which year do you want to check: "))
div_4 = (year%4)
div_100 = (year%100)
div_400 = (year%400)
if div_4 == 0 and (div_100 != 0 or div_400 == 0):
    print("The Year",year," is leap year :)")
elif div_4 != 0:
    print("The Year",year," is not leap year :(")
     
