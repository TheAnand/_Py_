import random

nb = random.randint(1,9)
guess = 0
count = 0

while guess != nb and guess != "exit" :

	guess = input("Guess any number : ")

	if guess == "exit" :
		break

	guess = int(guess)

	if guess > nb :
		print("Too high")
	elif guess < nb :
		print("Too low")
	else :
		print("Right")
