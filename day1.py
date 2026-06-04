#function to add two numbers
def add (x , y):
    return x + y
#function to subtract two numbers
def subtract (x , y):
    return x - y
#function to multiplication two numbers
def multi (x , y):
    return x * y
#function to divide two numbers
def div(x , y):
     if y == 0: return "invalid number"
     else:  
       return x / y
     
def Calculator():
    print("selection options")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

    while True:
        # Take the input from the user
        choice = input("Enter Choice: ")

        if choice in ['1','2','3','4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1 , num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1 , num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multi(num1 , num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {div(num1 , num2)}")
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            continue

        nextcalcu = input("Do you want to perform another calculation ? (yes/no) ")
        if nextcalcu.lower() != 'yes':
            print("exiting calculator")
            break

# start the calculator
Calculator()
        