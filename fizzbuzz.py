def main():
    fizzbuzz()




def fizzbuzz_loop(i):
    if(i % 3 == 0 and i % 5 == 0):
        return 1
    elif(i % 3 == 0):
        return 2
    elif(i % 5 == 0):
        return 3
    else: 
        return 4


if __name__ == "__main__":
    main()
