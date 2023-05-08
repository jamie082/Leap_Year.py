print('Leap year yes or no??')
print('By Jamie morrissey')

user_input = input('Enter Input Year: ')
print('Year is: ' + user_input)
'''add Python comment'''

def start_program():
    if (year % 400 == 0) and (year % 100 == 0):
        print("{0} is a leap year".format(year))

    elif (year % 4 == 0) and (year % 100 != 0):
        print("{0} is a leap year".format(year))

    else:
        print("{0} is not a leap year".format(year))
