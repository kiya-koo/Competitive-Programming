#function for checing is the year is leap or not
def is_leap(year):
    
    leep = False    
    if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):   
        leep = True    
    else:  
        leep = False
    return leep 

year = int(input())
print(is_leap(year))
