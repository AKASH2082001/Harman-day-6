print("select an option from the given menu")

while True:
    print("1.Addtion of two number")
    print("2.subratction of two number")
    print("3.multiplication of two number")
    print("4.division of two number")
    print("5.exit")

    choice = int(input("enter your choice"))

    if choice == 1:
        a = int(input("enter the value of a"))
        b = int(input("enter the value of b"))
        c = a + b
        print(c)

    elif choice == 2:
        a = int(input("enter the value of a"))
        b = int(input("enter the value of b"))
        c = a - b
        print(c)

    elif choice == 3:
        a = int(input("enter the value of a"))
        b = int(input("enter the value of b"))
        c = a * b
        print(c)

    elif choice == 4:
        a = int(input("enter the value of a"))
        b = int(input("enter the value of b"))
        c = a / b
        print(c)

    elif choice == 5:
        break

    else:
        print("invalid choice")