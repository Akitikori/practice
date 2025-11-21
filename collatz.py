def collatz(number):
    if (number % 2 == 0):
        return number // 2
    else:
        return 3 * number + 1

try:
    user_value = int(input('>'))
except ValueError:
    print('Please enter a whole number')
    
print(user_value)

while(user_value != 1):
    user_value = collatz(user_value)
    print(user_value)