def calculator():

    x = int(input("Enter number: "))
    y = int(input("Enter another number: "))
    function = input("Choose function (add, subtract, multiply, divide): ")

    if function == 'add':
        result = 0
        for i in range(y):
            result += 1
        for i in range(x):
            result += 1
        print("Addition result: ", result)

    elif function == 'subtract':
        result = 0
        if x > y:
            result = x - y
        elif x == y:
            result = 0
        else:
            result = y - x
        print("Subtraction result: ", result)

    elif function == 'multiply':
        result = 0
        for i in range(x):
            result += y
        print("Multiplication result: " , result)

    elif function == 'divide':
        if y == 0:
            print("Can't divide by 0")
        else:
            result = x / y
            print('Division result:', result)

    else:
        print("Invalid operation")

    print("Calculation finished")

if __name__ == "__main__":
    calculator()



