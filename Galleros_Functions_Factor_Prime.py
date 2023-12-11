prime_number = []
factors = []


def prime_numbers():
    print("\n{:>60}".format("* " * 25))
    print("{:>11}{:^58}*".format("*", "\033[1;95mP R I M E  N U M B E R S\033[0m"))
    print("{:>60}\n".format("* " * 25))

    while True:
        num_start = int(input("Enter a number [start]: "))
        if num_start < 0:
            print("Enter a non-negative number\n")
            continue
        elif num_start == 0:
            print("\033[91mPROGRAM TERMINATED\033[0M")
            break
        num_end = int(input("Enter a number [end]: "))
        if num_start >= num_end:
            print(f"\033[91mInvalid Input. Enter a number greater than {num_start}\033[0m\n")
        for num in range(num_start, num_end + 1):
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    prime_number.append(num)
        if num_start < num_end:
            print(f"Prime numbers between {num_start} and {num_end} are: \033[93m " + " ".join(map(str, prime_number)), "\033[0m")
            prime_number.clear()
            print()


def small_factor():
    print("\n{:>60}".format("* " * 25))
    print("{:>11}{:^58}*".format("*", "\033[1;95mFind the smallest factor\033[0m"))
    print("{:>60}".format("* " * 25), "\n")

    while True:
        num = int(input("Enter an integer: "))
        print("Press [0] to Exit.")
        if num >= 2:
            for i in range(2, num + 1):
                if num % i == 0:
                    factors.append(i)
        elif num == 0:
            break
        else:
            print("\033[91mInvalid input. Enter a number greater than 2\033[0m\n")
            continue

        smallest_factor = min(factors)
        print(f"The smallest factor other than 1 for {num} is \033[93m{smallest_factor}\033[0m\n")
        factors.clear()


while True:
    print("\n{:<9}".format(""), "_ " * 40)
    message1 = "\033[1;93m{:^68}\033[0m{:>11}".format("P I C K", "|")
    print("{:>10}".format("|"), f"{message1}")
    print("{:>10}{:>12}{:>24}{:>38}{:>6}".format("|", "[0] EXIT", "[1] Small Factor of N", "[2] Prime Numbers within the range", "|"))
    print("{:>10}".format("|"), "_ " * 39 + "|")

    choice = int(input("    Your choose: "))
    if choice == 1:
        small_factor()
    elif choice == 2:
        prime_numbers()
    elif choice == 0:
        print("\n\033[91mPROGRAM TERMINATED\033[0m")
        break
    else:
        print("Choose between [1] and [2] only!")
