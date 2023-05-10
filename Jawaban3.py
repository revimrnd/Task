if __name__=='__main__':
    x = 485
    Year = x//360
    Month = (x-Year*360)//30
    Week = (Month//30)
    Day = (Week//7)
    print(Year)
    print(Month)
    print(Week)
    print(Day)
          
