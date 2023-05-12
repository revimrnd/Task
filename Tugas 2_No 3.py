n = int(input('Enter a starting number (greater than 0) or QUIT: '))
print(n)
while n > 1:
    if n % 2 == 0 :
        n = n//2
        print (n)
    else:
        n = 3*n+1
        print (n)