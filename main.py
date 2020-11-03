def print_string():
	print("code started.")

if __name__=='__main__':
	print_string()

c=True
while c:
    n = int(input('Please enter an integer: '))
    if n < 1 or n > 7:
        print("not a day!")
        c=False
    elif n == 1:
        print('Monday')
    elif n == 2:
        print('Tuesday')
    elif n == 3:
        print('Wednesday')
    elif n == 4:
        print('Thursday')
    elif n == 5:
        print('Friday')
    elif n == 6:
        print('Saturday')
    else:
        print('Sunday')