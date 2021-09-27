gender = input("What is your gender? ")
day = input("What day were you born?(dd): ")
month = input("What month were you born?(mm): ")
year = input("What year were you born?(yyyy): ")

the_year = int(year[-2:])
["1897"]

year_code = (the_year + (the_year//4)) % 7
#print(year_code)

def checkMonthCode(month):
    if month.lower() == 'january' or month.lower() == 'october':
        monthCode = 0
    elif month.lower() == 'february' or month.lower() == 'march' or month.lower() == 'november':
        monthCode = 3
    elif month.lower() == 'april' or month.lower() == 'july':
        monthCode = 6
    elif month.lower() == 'may':
        monthCode = 1
    elif month.lower() == 'june':
        monthCode = 4
    elif month.lower() == 'august':
        monthCode = 2
    else:
        monthCode = 5
    return monthCode

#print(checkMonthCode(month))

century_code = {"1700s":4,"1800s":2,"1900s":0,"2000s":6,"2100s":4,"2200s":2,"2300s":0}

cent = year[0:2]
#print(cent)


for key in century_code:
    #print(key[0:2])
    if key[0:2] == cent:
        cent_code = century_code[key]

#print(cent_code)

def checkLeap(year):
    if month.lower() == "january" or month.lower() == "february":
        if int(year)%400 ==0:
            return 1
        elif int(year)%4 == 0 and int(year)%100 != 0:
            return 1
        else:
            return 0
    else:
        return 0

#print(checkLeap(year))
calculation = (year_code + checkMonthCode(month) + int(cent_code) + int(day) - checkLeap(year)) % 7

#print(calculation)

days={0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"}

mapsName = days[calculation]

name_male = {"Sunday":"Kwasi","Monday":"Kodjo","Tuesday":"Kwabena","Wednesday":"Kwaku","Thursday":"Yaw","Friday":"Kofi","Saturday":"Kwame"}

name_female = {"Sunday":"Akosua","Monday":"Adjoa","Tuesday":"Abenaa","Wednesday":"Akua","Thursday":"Yaa","Friday":"Afia","Saturday":"Amma"}

if gender.lower() == "female" or gender.lower() == "f":
    print("You were born on a ", mapsName, " therefore, your name is ,", name_female[mapsName])

if gender.lower() == "male" or gender.lower() == "m":
    print("You were born on a", mapsName, ",therefore, your Ashanti name is ", name_male[mapsName])
