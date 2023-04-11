
# 1. Will the code run, & if so, what will be the data types & values of a & b?
a, b = [10, 11] # will run, a & b will be integers, a = 10, b = 11
a, b = [10] # won't run, there are not enough values
a, b = [10, 11, 12] # won't run, there are too many values, or not enough variables
a, *b = [10, 11] # will run, they both will be integers, a = 10, b = 11 
a, *b = [10] # will run, a is an integer, b is nothing, a = 10, b equals nothing
a, *b = [10, 11, 12] # will run, a is an integer, b is a string, a = 10, b = (11, 12)

# 2. What data type is args & kwargs inside the function, what are the values,
# and how would you use them?
def base_function(*args, **kwargs):
    pass

base_function() # undefined, function placeholder
base_function(['A', 'B']) #list of objects (i.e. not variables), argument which 
# here is a hardcoded list of 'A', 'B'
base_function('Hello', 'World', '!') # string, argument is a hard-coded string
base_function(answer=True, question='No') # boolean, string, kwargs the boolean 
# states whether or not to run a portion of the function, the string is can be changed
base_function('a', 'b', c='value', d=10) #string (argument), string (argument),
# string (key argument), integer (key argument); the arguments are a hard-coded string, 
# the kwargs are able to be changed


# 3. Write a lambda function that is passed into my_func, & performs a valid
# operation on a & b, without editing the contents of my_func at all.

func = lambda a, b: (a + b)^2
    
def my_func(a, b, func):
    value = func(a, b)
    return value

