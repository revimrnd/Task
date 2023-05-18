thefield = [" ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]

print("Welcome, this is your field")

def drawfield(thefield):
    print(thefield[0] + "|" + thefield[1] + "|" + thefield[2])
    print('-+-+-')
    print(thefield[3] + "|" + thefield[4] + "|" + thefield[5])
    print('-+-+-')
    print(thefield[6] + '|' + thefield[7] + '|' + thefield[8])
drawfield(thefield)


