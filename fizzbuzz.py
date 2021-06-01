def main():
    fizzbuzz()

def fizzbuzz():
    for i in range(100):
        temp = fizzbuzz_loop(i)
        if(temp == 1):
            print("FizzBuzz")
        elif(temp == 2):
            print("Fizz")
        elif(temp == 3):
            print("Buzz")
        else:
            print(i)


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
