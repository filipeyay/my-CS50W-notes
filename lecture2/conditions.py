# Specify 'int' at the beginning because otherwise the input will be interpreted as 'string'

n = int(input("Type a number: "))

if n > 0:
    print("n is greater than zero")
elif n < 0:  # elif = else if
    print("n is less than zero")
else:  # end the condition with the only possible option
    print("n is equal to zero")
