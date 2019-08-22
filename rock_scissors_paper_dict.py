print('''Please select only one :
		Rock
		Scissors
		Paper''')
while True :
	game_dict = {'Rock':1,'Scissors':2,'Paper':3}
	player_a = str(input("Player_a :"))
	player_b = str(input("Player_b :"))
	a = game_dict.get(player_a)
	b = game_dict.get(player_b)
	diff = a-b

	if diff in [-1 , 2] :
		print("Player a wins.")
		if str(input("Do you want to continue game , Yes or No?\n"))=="Yes" :
			continue
		else :
			print("Game is over now !!!\n")
			break
	elif diff in [-2 , 1] :
		print("Player b wins.")
		if str(input("Do you want to continue game , Yes or No?\n"))=="Yes" :
			continue
		else :
			print("Game is over now !!!")
			break
	else :
		print("Match is draw ! Please continue")
print('')
