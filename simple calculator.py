
def addition(n_1, n_2):
    if n_1 == 'None' or n_2 == 'None':
        print('Press "n" and add your desired numbers\n')
    else:
        print(f'The sum of {n_1} and {n_2} is ', n_1+n_2)
        break 

def subtraction(n_1, n_2):
    if n_1 == 'None' or n_2 == 'None':
        print('Press "n" and add your desired numbers\n')
    else:
        print(f'The difference of {n_1} and {n_2} is ', n_1-n_2)
        return

def multiplication(n_1, n_2):
    if n_1 == 'None' or n_2 == 'None':
        print('Press "n" and add your desired numbers\n')
    else:
        print(f'The product of {n_1} and {n_2} is ', n_1*n_2)
        return

def division(n_1, n_2):
    if n_1 == 'None' or n_2 == 'None':
        print('Press "n" and add your desired numbers\n')
    else:
        print(f'The division of {n_1} and {n_2} is ', n_1/n_2)
        return

def remainder(n_1, n_2):
    if n_1 == 'None' or n_2 == 'None':
        print('Press "n" and add your desired numbers\n')
    else:
        print(f'The remainder of {n_1} and {n_2} is ', n_1%n_2)
        return

def power(n_1, n_2):
    if n_1 == 'None' or n_2 == 'None':
        print('Press "n" and add your desired numbers\n')
    else:
        print(f'The exponentiation of {n_1} and {n_2} is ', n_1**n_2)
        return

def calculator(y):
    n = 0
    while n == 0:
        if y == 'a':
            addition(n_1, n_2)
        elif y == 's':
            subtraction(n_1, n_2)
        elif y == 'm':
            multiplication(n_1, n_2)
        elif y == 'd':
            division(n_1, n_2)
        elif y == 'r':
            remainder(n_1, n_2)
        elif y == 'e':
            power(n_1, n_2)
        else:
            print('invalid entry\n')

    
n_1 = 'None'
n_2 = 'None'
while n_1 == 'None' and n_2 == 'None':
    print('First Number = None, Second Number = None')
    print('n- Enter new numbers\n')
    print('a- Addition')
    print('s- Subtraction')
    print('m- Multiplication')
    print('d- Division')
    print('r- Remainder')
    print('e- Exponentiation\n')
    print('x- Exit program')
    y = input('Select an option: ')

    if y == 'n':
        n_1 = float(input('Number 1:'))
        n_2 = float(input('Number 2:'))
        y = input('Select an option: ')
        calculator(y)
    elif y == 'x':
        print('program closed')
        break
    else:
        calculator(y)
