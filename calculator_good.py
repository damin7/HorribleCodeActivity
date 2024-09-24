def add(a,b):
    return a + b

def subtract(a,b):
    return a- b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b != 0:
        return a/b
    else:
        print("Can't divide by 0")

def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    function = input("Choose function(add, subtract, multiply, divide): ")

    if function == "add":
        result = add(x,y)

    elif function == "subtract":
        result = subtract(x,y)

    elif function == "multiply":
        result = multiply(x,y)

    elif function == "divide":
        result = divide(x,y)
    else:
        result = "Invalid operation."

    print("Result:", result)

if __name__ == "__main__":
    main()