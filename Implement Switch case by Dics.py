#Using dics implements of switch case
def Year(choice) :
	switcher = {
		1:'Jan',
		2:'Feb',
		3:'Mar',
		4:'Apr',
		5:'May',
		6:'Jun',
		7:'Jul',
		8:'Aug',
		9:'Sept',
		10:'Oct',
		11:'Num',
		12:'Dec'
	}
	return switcher.get(choice,"Invalid")
print('''Choose anyone :
	1. Jan
	2. Feb
	3. Mar
	4. Apr
	5. May
	6. Jun
	7. Jul
	8. Aug
	9. Sept
	10.Oct
	11.Num
	12.Dec''')
temp = int(input())
print(f"{Year(temp)}")
