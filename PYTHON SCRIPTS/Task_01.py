def fizzbuzz(fizz="Fizz", buzz="Buzz", lowerbound=1, upperbound=100):

    for i in range(lowerbound, upperbound + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{fizz} {buzz}")
        elif i % 3 == 0:
            print(f"{fizz}")
        elif i % 5 == 0:
            print(f"{buzz}")
        else:
            print(f"{i}")


def main():
    wanttochange = input(
        "Do want to to change the values of Fizz Buzz & the Numbers Range (Yes/No) : "
    )

    if wanttochange.lower() == "yes":
        fizz = input("Enter a string to replace Fizz : ")
        buzz = input("Enter a string to replace Buzz : ")
        while True:
            try:
                lowerbound = int(input("Enter a lower bound for range : "))
                upperbound = int(input("Enter an upper bound for range : "))
                break
            except:
                print("Please enter the valid integer values for the inputs.")
                continue

        fizzbuzz(fizz, buzz, lowerbound, upperbound)
    else:
        fizzbuzz()


if __name__ == "__main__":
    main()
