# I'ts possible to import a function from another module(file)

from functions import square

for i in range(10):
    print(f"The square of {i} it's {square(i)}.")
