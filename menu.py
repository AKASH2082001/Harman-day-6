print("select an option from the menu")

while True:
    print("1.Add an employee")
    print("2.search an employee")
    print("3.update an employee")
    print("4.Delete an employee")
    print("5.exit")

    choice = int(input("enter a choice: "))

    if choice == 1:
        print("select an option to enter an employee data")

    elif choice == 2:
        print("select an option to search an employee data")

    elif choice == 3:
        print("select an option to update an employee data")

    elif choice == 4:
        print("select an option to delete an employee data")

    elif choice == 5:
        break

    else:
        print("invalid choice")

