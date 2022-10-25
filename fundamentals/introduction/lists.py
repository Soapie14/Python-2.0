# play around with the drawers!
drawers = ['documents', 'envelopes', 'pens']

# Print the second value from the list (envelopes)
#print(drawers[1])

# Change "pens" to "useless manuals"

#drawers[2] = "useless manuals"

# Change the first value to whatever is the second value

#drawers[0] = drawers[1]

# What should the list look like now?

#print(drawers)
# Print the list! Does it match your prediction?

some_nums = [44,56,2,3,12,19,6]
#print("Get started by writing your own code!")

# Some optional challenges to assess and refine your understanding:

# Print the length of the list.
#print(len(some_nums))

# Use antoher python built-in function and print the result.

# Remove an item from the list. Remember to verify that it was removed.

some_nums.pop()
#print(some_nums)

# Utilize a method from the documentation and print the result.

#some_nums.sort()
#print(some_nums)

# Challenge: Write a for loop to print all integers from 1 to 20, including 20.

#for i in range(1, 21):
#    print(i)

countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]

# Challenge 1: Fix the range!
for integer in range(0, 4):
    print("Index:", integer)
    # Challenge 2: print the index here
    print("Country:", countries[integer])
    # Challenge 3: print the country here
 
# Looping over values only...
for country in countries:
    print("Country: ", country)
    # Challenge 4: print the country here