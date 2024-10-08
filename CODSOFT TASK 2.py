def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    return x % y

def exponentiation(x, y):
    return x ** y

def floordivision(x,y):
    return x//y



def main():
    print("Welcome to the Simple Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. modulus")
    print("6. exponentiation")
    print("7. floordivision")

    # Take input from the user
    operation = input("Enter operation (1/2/3/4/5/6/7): ")

    if operation in ('1', '2', '3', '4', '5', '6', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif operation == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif operation == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif operation == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif operation == '5':
            print(f" {num1} % {num2} = {modulus(num1, num2) }")
        elif operation == '6':
            print(f" {num1} ** {num2} = {exponentiation(num1, num2)}")
        elif operation == '7':
            print(f" {num1} // {num2} = {floordivision(num1, num2)}")

    else:
        print("Invalid operation!")


if __name__ == "__main__":
    main()
