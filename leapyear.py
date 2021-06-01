def main():
    year = int(input("Enter a year: "))
    temp = leap_year(year)
    if(temp == 1):
        print("Is a leap year")
    else:
        print("Is not a leap year")

if __name__ == "__main__":
    main()
