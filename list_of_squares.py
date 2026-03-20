#generating squares and store them in a list 
n=int(input("Enter the number till when you wanna generate the squares:"))

square=[]
i=0
while i<=n:
    square.append(i*i)
    i=i+1

print(square)