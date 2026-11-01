print("Logic Box");

print(" Welcome to the Pattern Generator and Number Analyzer!")

while True:

    print("\nMenu Options:")
    print("1. Generate a Right-Angled Triangle")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    # Option 1: Pattern Generator
    if choice == "1":

        rows = int(input("Enter the number of rows: "))

        while rows <= 0:
            print("Invalid input! Rows must be positive.")
            rows = int(input("Enter the number of rows: "))

        print("\nRight-Angled Triangle Pattern:")

        for i in range(1, rows + 1):
            for j in range(1, i + 1):
                print("*", end=" ")
            print()

    # Option 2: Number Analyzer
    elif choice == "2":

        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))

        while end <= start:
            print("Invalid range! Ending number must be greater than start.")
            end = int(input("Enter the ending number again: "))

        total = 0

        print("\nNumber Analysis:")

        for num in range(start, end + 1):

            total += num

            if num % 2 == 0:
                print(num, "is Even")
            else:
                print(num, "is Odd")

            if num == 0:
                pass

        print("\nSum of all numbers:", total)

    # Option 3: Exit
    elif choice == "3":

        print("\nThank you for using the Student Data Organizer!")
        print("Program exited successfully. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")
        continue


