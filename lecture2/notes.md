## Variables

The role of the variable is to store data. Be it **text**, **integer numbers** (negative or positive) or **decimal numbers** (negative or positive), and others as well such as **boolean** (True or False) and **lists**.

```python
name = "Nikdra"
age = 49
weight = 70.2

print(name)
print(age)
print(weight)
```

The problem with the above code is that the code will interpret the results of `print` as `String`. This conversion can also be called `cast`. To change this we can do:

```python
name = "Nikdra"
age = 49
weight = 70.2

print(name) # It is not necessary to specify the name as it is already a string
print(int(age))
print(float(weight))
```

## Input

Input allows us to store user input.

```python
name = input("Type your name: ")
age = input("Type your age: ")
weight = input("Type your weight: ")

print(name)
print(int(age))
print(float(weight))
```

## Type

Sometimes it is extremely useful for debugging code if we can see what type of value we are working with. And for this we can use `type`.

```python
name = "Nikdra"
age = 49
weight = 70.2

print(type(name))
print(type(age))
print(type(weight))

# RESULT:
# <class 'str'>
# <class 'int'>
# <class 'float'>
```

## Operators

Operators are used to perform mathematical calculations. Since we have the basis for the calculation, the interpreter is able to solve it for us.

```python
addition = 1 + 1
subtraction = 2 - 3
multiplication = 4 * 4
division = 30 / 3
power = 7 ** 2

print("Addition: ", addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)
print("Division: ", division)
print("Power: ", power)
```

## Conditions

When we add conditions to our script, we make it more dynamic. A condition can affect the flow of our program. Let's look at an example to make it easier to understand. Let's create a variable containing an input so that the person can enter their age. If their age is 18 or greater, they will receive an approval message. If they don't meet the condition, they will receive a failure message.

```python
age = int(input("What's your age: "))

if age >= 21:
    print("You CAN enter.")
else:
    print("You CANNOT enter")
```

It is also important to pay attention to `indentation`, which in this example is the space before `print`. In Python, `indentation` is the consistent spacing at the beginning of lines of code, used to delimit blocks of code. In practice, this would be equivalent to entering 1 tab or 4 spaces. However, most modern code editors do this automatically.

## Else If

In Python, `else if` is called `elif` and it is used to insert more conditions within a block of instructions. And by using `and` you can still add one more condition to the `if`. Example:

```python
age = int(input("What's your age: "))

if age >= 21 and age <= 99:
    print("You are of legal age")
elif age < 21 and age >= 1:
    print("You are a minor")
elif age >= 100 and age <= 500:
    print("You should be dead")
elif age > 500:
    print("Stop lying")
else:
    print("You haven't been born yet")
```

## Lists

Lists in Python are a set of data stored in a variable. In the example below, we will create a simple list and access the value of the list using curly braces.

### Data structure

- list - Sequence of mutable values
- tuple - Sequence of immutable values
- set - Collection of unique values
- dict - Collection of key-value pairs

```python
number_list = [1, 2, 3]

print(number_list[0])
print(number_list[1])
print(number_list[2])
```

You can see that we start counting the list from 0. Where 0 is the first position in the list. This is called the `index`.

You can also manipulate the values ​​in the list using the keys to access the original value. Example:

```python
number_list = [1, 2, 3]

number_list[0] = 5 # Now the first item in the list goes from value '1' to value '5'

print(number_list[0])
print(number_list[1])
print(number_list[2])
```

The list can store several types of values, such as `Strings` and `Float` in addition to numbers.

We can also create empty lists and later assign values ​​using the `append` method. Example:

```python
empty_list = []

empty_list.append("Hello")
empty_list.append("World")

print(empty_list)
```

Another example of a list where we extract the total number of items from the list with the `len` method, the smallest value with the `min` method and the largest value with the `max` method.

```python
numbers = [10, 9, 8, 7, 6]

print("Total: ", len(numbers)) # total items
print("Lowest value: ", min(numbers)) # lowest value
print("Highest value: ", max(numbers)) # highest value
```

#### Other methods to use with lists

| Method  | Parameter      | Result     | Description                                              |
| ------- | -------------- | ---------- | -------------------------------------------------------- |
| append  | item           | mutator    | Adds a new item to the end of the list                   |
| insert  | position, item | mutator    | Inserts a new item at the given position                 |
| pop     | none           | hybrid     | Remove and return the last item                          |
| pop     | position       | hybrid     | Remove and return the item from the position             |
| sort    | none           | mutator    | Sort the list                                            |
| reverse | none           | mutator    | Sort the list in reverse order                           |
| index   | item           | return idx | Returns the position of the first occurrence of the item |
| count   | item           | return ct  | Returns the number of occurrences of the item            |
| remove  | item           | mutator    | Remove the first occurrence of the item                  |

## Loops

Repetition is used to execute a block of instructions repeatedly.
`for`: Loop that goes through sequences, repeating actions for each element.
`while`: Loop that executes actions while the condition is true.

In the example below we want to create a program that simulates a teacher giving grades to 5 students, entering the student's number and then his grade.

`x` is a temporary variable that changes according to the execution of the loop. In this case, `x` will start at 0 and go up to 4, since the `range` was defined as 5.
For example: `- range(5) = [0, 1, 2, 3, 4, 5]`

Program using `for`:

```python
grades = []

for x in range(5):
    number_student = input("Nº: ")
    average = float(input("Grade: "))
    result = [number_student, avarage] # creates a list where 'number_student' occupies position 0 and 'media' occupies position 1
    grades.append(result) # we place the variable 'result' inside the list of notes

print("Grades: ", len(grades))

for n in grades:
    number_student = n[0] # displays the student number
    grade = n[1] # displays the student's grade corresponding to his/her number
    print(f"The student {number_student}, had avarage grade of {grade}.")
```

Using `while` the idea is the same. We define `counter = 1`, because this way the counter counts from 1 to 5. If it is defined as 0 it will also count 0, and the program would be executed 6 times (0, 1, 2, 3, 4, 5,). Then we leave almost everything the same with the difference that at the end of the execution we need to specify that the `counter` variable will count + 1. Therefore, the second time the program runs it will be like this: `counter = 2`. And so on, until it reaches `counter = 5` and the program ends.

Program using `while`:

```python
grades = []

counter = 1

while counter <= 5:
    number_student = input("Nº: ")
    grade = float(input("Grade: "))
    result = [number_student, grade]
    grades.append(result)

    counter = counter + 1

print("Grades: ", len(grades))
```

## Dictionaries

**Dictionaries** or **objects** are structures that store `key` and `value`.

```python
variable = {
    "key": "value,
}
```

Example using the first code as a base:

```python
person = {
    "name": "Nikdra",
    "age": 49,
    "weight": 70.2
}

print(person["name"])
print(person["age"])
print(person["weight"])
```

Let's move on to another more complex example, with an emphasis on the enemy list. In this enemy list, we will create a list called "npcs" and within it we will insert 4 dictionaries.

```python
# player info

player = {
    "name": "Nikdra",
    "level": 1,
    "hp": 100,
    "xp": 0,
    "attack": 5,
}

# enemies list
npcs = [
    {"name": "Zombie", "attack": 2, "hp": 50, "xp": 5},
    {"name": "Skeleton", "attack": 5, "hp": 100, "xp": 10},
    {"name": "Gollen", "attack": 10, "hp": 150, "xp": 15},
    {"name": "Dragon", "attack": 25, "hp": 200, "xp": 20},
]
```

## Functions

Functions are reusable blocks of code that perform specific tasks. Instead of repeating code to get a result, we can create functions, and then call these functions when necessary.

To illustrate, let's create a program where we create a function with 2 parameters and add these parameters. Then we can call this function as many times as we want and add the values ​​we want. Here's the code:

```python
def my_function(value1, value2):
    return value1 + value2

result = my_funtion(10, 10) # using the algorithm defined in the function we can add 10 + 10 in this example

print(f"Result: {result}")
```

## Putting it into practice

Let's create a chat program.

- Import the `os` library.

- Create an empty list to store messages. Then create an input to receive the username.

- Now create a loop. Use a method from the library that was imported to clear the terminal `os.system("clear")`. Check for messages and, if there are any, set them to display.

- Make a division to separate the information. To make the code execution more beautiful.

- Create an input to receive the user's message and check if it is the word "end". Then add a `break`, so that if it is the word "end" it ends the execution of the loop.

- Create an execution so that if it is not the word "end" the message is added to the list.

The final code should look like this:

```python
import os

message = []

name = input("Type your name: ") # receives the user name input

while True:
    os.system("clear") # clear the terminal (windows command should be "cls")
    if len(message) > 0: # verify if theres messages
        for m in message: # if theres messages, prints it
            print(m["name"], "-", m["text"])
    print("_________________________")

    # receives user text input
    text = input("Message: ")
    if text == "end": # if the user type "end" it will break the loop
        break

    # if the user don't type "end" then the message is added to the list
    menssage.append(
        {"name": name, "text": text,}
    )
```
