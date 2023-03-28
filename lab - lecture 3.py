#### Fix the following errors (in 1-6)!

#1
x = 10
y = 20
print(x + y)

#2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
print(my_list_len)

#3
my_string = 'hello world'
my_string.upper()

#4
z = ['a', 'b', 'c']
z.insert(3, 'd')
print(z)

#5 Why does the x not display 10, followed by the 200?  Fix it so it does.
x = 10
print(x)
y = 20
print(x * y)

#6
fave = 'blue'
color = f'My favorite color is {fave}, what is yours?' 
print(color)

#### Answer the following questions without changing the code given

#7 Make the entries in this list unique
schools = ['harris', 'booth', 'crown', 'harris', 'harris']
schools_1 = set(schools)
print(schools_1)

#8 Change the 'dog' entry to 'cat'
animals = tuple(['bird', 'horse', 'dog', 'fish'])
list_ani = list(animals)
list_ani[2]='cat'
print(list_ani)

#9 Make this string take a name based on a variable (you can modify the code on this one)
name = 'Alice'
welcome = f'Hello {name}, and welcome to Data and Programming!'
print(welcome)

#10 Separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
my_sent = 'I LOVE how spring is super late this year and there are no flowers and it is cold and rainy.'
my_sent_list = my_sent.lower().split()
print(my_sent_list)

