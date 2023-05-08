print('Leap year yes or no??  v. 001')
print('By Jamie morrissey')

user_input = int(input('Enter Input Year: '))
print(user_input)
# add python comment

if (user_input % 400 == 0) and (user_input % 100 == 0):
    print("{0} is a leap year".format(user_input))

elif (user_input % 4 == 0) and (user_input % 100 != 0):
    print("{0} is a leap year".format(user_input))

else:
    print("{0} is not a leap year".format(user_input))