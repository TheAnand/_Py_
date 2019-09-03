from datetime import date
def Age(Bd) :
	today = date.today()
	age = today.year - Bd.year - ((today.month, today.day)<(Bd.month , Bd.day))
	return age
year = int(input("Enter Birthday Year :"))
month = int(input("Enter Month of Birthday :"))
day = int(input("Enter Day of Birthday :"))
Temp = Age(date(year,month,day))
print(Temp)
