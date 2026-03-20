#reversing a number by taking input from the user
num =int(input("enter your number:"))
rev=0
while num>0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("reversed number:", rev)
