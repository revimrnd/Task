
text = input("Enter your text\n")
text = str.upper(text)
for x in text:
    if(x == ' '):
        print(' ', end='')
    elif(ord(x)-ord('A')+4 >= 26 ):
        print(chr(ord(x)-26+4), end='')
    else:
        print(chr(ord(x)+4), end='')