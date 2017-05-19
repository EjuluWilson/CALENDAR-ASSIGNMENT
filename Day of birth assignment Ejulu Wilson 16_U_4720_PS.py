#NAME:EJULU WILSON
#REG NO. 16/U/4720/PS
#COURSE: BSC COMPUTER ENGINEERING
import calendar #imports calendar module
from datetime import datetime #imports datetime module 
now=datetime.now()#extracts the current system time and date
current_date=now.date()#extracts current date without time
year=list(str(current_date))#lists the current date
current_day=int(year[-2]+year[-1])#extracts the current day of the month and converts it to an integer
current_month=int(year[5]+year[6])#extracts the current month  and converts it to an integer
year=int(year[0]+year[1]+year[2]+year[3])#extracts the current  and converts it to an integer
print ("To find out what day of the week you were born on, kindly provide the following information:")
age=int(input('your age: '))
mt=int(input('month of birth (1-12): '))
dy=int(input('date of the month (1-31): '))
if mt>current_month:
        yr=year-age-1
elif mt==current_month:
    if dy>current_day:
        yr=year-age-1
    else:
        yr=year-age
else:
    yr=year-age
cal=(calendar.weekday(yr, mt, dy))
day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saterday','Sunday']
print ('You where born on a' , day[cal])


