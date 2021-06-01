def main():
    year = int(input("Enter a year: "))
    temp = leap_year(year)
    if(temp == 1):
        print("Is a leap year")
    else:
        print("Is not a leap year")

def leap_year(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

if __name__ == "__main__":
    main()
