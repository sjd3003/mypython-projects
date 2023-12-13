try:
    first_number = int(input("Enter is your first number: "))
    second_number = int(input("Enter your second number: "))
    operator = input("Enter your operator(+,-,*,/): ")

    if operator == "+":
        result = first_number + second_number
        print ("Result:",result)
    elif operator == "-":
        result = first_number - second_number
        print ("Result:",result)
    elif operator == "*":
        result = first_number * second_number
        print ("Result:",result)
    elif operator == "/":
        result = first_number / second_number
        print ("Result:",result)
    else:
        print ("Wrong operator")
except ValueError:
    print("Please Use Integer")
