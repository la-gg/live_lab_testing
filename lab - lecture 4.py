#Convert these objects!

#1
start_list = [[2, 3, 4], [6, 8, 9]]
#turn it into [1,    2,   3, 4   ]


# so we should begin by combining the list

concat_list = sum(start_list, [])
print(concat_list)

# filter out the odds (non-integers)

even_list = [num for num in concat_list if num % 2 == 0]
print(even_list)
# divide the list by two

even_list







#2
import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime(1999, 2, 23),
#              'Sarah':datetime(2001, 9, 1),
#              'Zach': datetime(2005, 8, 8)}

# Capitalize the names, put the dates into date time

