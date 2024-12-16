# The idea of ​​a 'decorator' is a function that takes a function as input and returns a modified version of that function.


def announce(f):
    def wrapper():
        print("Making an announcement...")
        f()  # executes the linked function, in this case the 'hello' function
        print("World!")

    return wrapper


@announce  # link the function below to the function of 'annouce'
def hello():
    print("Hello ")


hello()
