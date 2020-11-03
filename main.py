def print_string():
    print("code started.")


if __name__ == '__main__':
    print_string()

fibo_n = int(input("enter a number for the fibonacci series:\n"))

n1, n2 = 0, 1
count = 0

print("Fibonacci sequence:")
while count < fibo_n:
    print(n1)
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count += 1
