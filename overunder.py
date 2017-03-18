# Intro tests for experimenting
# print('Hello World')
# print('Guess a Number')
# input('Guess a Number')

# # Generate a random number

# import random

# number = random.randint(1,10)

# # say whether your guess is too high or too low

# guess = input('Guess a Number')
# guess = int(guess)
# print(type(guess))
# print(type(number))

# # if guess < number:
# # 	print('Guess is too low.')
# # 	print('Try again.')
# # elif guess == number:
# # 	print('Congratulations, you have guessed the correct number!')
# # 	print('Your prize will be coming shortly.')
# # else:
# # 	print('Guess is too high.')
# # 	print('Try again.')

# count = 0
# while (count < 9):
#    print ('The count is:', count)
#    count = count + 1

# print ("Good bye!")

# import random

# number = random.randint(1,100)
# guess = -1

# while guess != number:
# 	guess = input('Guess a Number')
# 	guess = int(guess)

# 	if guess < number:
# 		print('This is too low.')
# 		print('Try again.')
# 	elif guess == number:
# 		print('Congratulations, you win.')
# 		print('Click here to get your prize')
# 	else:
# 		print('THis is too high.')
# 		print('Try again.')
	
	# print(guess != number)

# count = 0
# while (count < 6):
# 	print ('You are on team', count)
# 	count = count + 1

# for i in range (10):
# 	print(i)

# sum for all the numbers from 1-10
# sum = 0
# for i in range (11):
# 	# sum = sum + i (same as below equation)
# 	sum += i
# 	# this prints ALL of the answers in the range
# 	print(sum) 
# print(sum) - this prints JUST the final answer

# below is a list
# sum = 0
# a = [1, 2, 5, 6]
# for x in a:
# 	sum += x
# 	print(sum)

# import sys
# print(sys.argv)
# x = int(sys.argv[1])

# for i in range(x):
# 	print(i)

# for x in range(8):
# 	row = ""
# 	for y in range (8):
# 		if (x + y) % 2 == 0:
# 			row += "*"
# 		else:
# 			row += "-"
# 		row += ' '
# 	print(row)

# name = input("What's your name? ")
# # print ("Hello,", name)
# age = input("How old are you? ")
# # print (name, "is", age, "years old.")
# test = "{0} is {1} years old.".format(name, age)
# # string formatting is above
# print (test)

sum = 0
x = [3, 6, 1, 7, 9, 2]
for i in x:
	sum += i
print (sum)