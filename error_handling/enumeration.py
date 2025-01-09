#enumerate 
x=('Masala', 'Dosa', 'Idli', 'Vada')
y=enumerate(x)
print(list(y))

# Output: [(0, 'Masala'), (1, 'Dosa'), (2, 'Idli'), (3, 'Vada')]
# Explanation: enumerate() function adds a counter to an iterable and returns it in a form of enumerate object.
# The output is a list of tuples where the first element of each passed tuple is the index and the second element is the value.