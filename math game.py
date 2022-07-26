def mathgame():
    global name
    global num1
    import random

    if num1 == 0:
        number = random.randint(0,9999)
        num1 = number
    else:
        number = num1
    print(f'Your Number is: {number}\n')

    guess = int(input('Add or Subtract: '))

    if guess<0:
        ans = number + guess 
        print(f'\n{number} - {guess} = {ans}')
    else:
        ans = number + guess 
        print(f'\n{number} + {guess} = {ans}')
    
    j = ''
    a = str(ans)
    z = a[0]
    length = len(a)

    while length!=0:
        j += z
        length -= 1

    if int(ans) != int(j) :
        print('\nThat is Incorrect!\n') 
        print('Try again!\n')
        mathgame()
    elif int(ans) == int(j):
        print(f'That is Correct!\nWell Done {name}!\n')
        choice()
    return ''

def choice():
    global num1
    print('\nPress 1 to restart\nPress 2 to exit\n')
    choice = int(input('Enter choice: '))
    if choice == 1:
        num1 = 0
        mathgame()
    elif choice == 2:
        print("\nGood Game. Have a Nice day!\n")
        exit()
    else:
        print("Enter a valid selection!",choice())

num1 = 0
name = input('Enter your Name: ')
print('\nHow To Play?\n\nAdd or subtract a number of your choice to create a repeating number.\nFor eg. 1111 or 888 or 44 \n')
mathgame()