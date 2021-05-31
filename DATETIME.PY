'''import datetime
today=datetime.datetime.now()
print(today)
print(type(today))'''

#IMPORT ONLY DATE NOT TIME WE SHOULD USE STRFTIME KEYWORD TO DO THIS

import datetime
today=datetime.datetime.now().strftime("%d:%m:%Y") #captial Y is used to print year 4 digits and small y is used to print in 2 digits 

print(today)



# HOW TO GO TO A PATRICULAR DAY DATE OR TWO OR THREE DAYS BACK
# WE USE TIMEDELTA()
'''import datetime
today=datetime.datetime.now()+ datetime.timedelta(1)# + is used for next date and - is used for previous date 
print(today)'''




