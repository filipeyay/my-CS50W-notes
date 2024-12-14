# Creates an empty set

s = set()

# Add elements to the set

s.add(1)
s.add(2)
s.add(3)
s.add(4)

# In a set the value is not repeated, so the line below is ignored

s.add(1)

# It's also possible to remove a set with

s.remove(1)

print(s)

# To calculate the length we can use len
# NOTE len = short for length

print(f"The set has a total of {len(s)} elements.")
