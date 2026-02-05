#tUPLE 
# A tuple is an immutable type of a list (It cannot change)
# To introduce a tuple, we use parenthesis ()

counties = ("Nairobi", "Mombasa", "Nakuru", "Eldoret", "Kajiado", "Meru")

print(counties)
print(type(counties))

# Slicing of tuple
print(counties[3:])

# Accessing items of a tuple by use of indexes
print(counties[5])

# Note: Below will generate an error
# Attribute error
counties.append("Machakos")
print(counties)