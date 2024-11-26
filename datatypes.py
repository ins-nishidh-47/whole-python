'''
datatypes : {tuple, dictionary, list, string, int, boolean, float, floor}
mutable : {dictionary, list}
immutable : {1 - n(mutable)}
'''

'''Defining tuple'''
rand_str: str = "Heloo"

#using tuple function
tup3 = tuple(rand_str) # ("H", "e", "l", "o", "o")

#with variables and nested tuples
tup1: tuple = 1,2,3
tup2: tuple = (3,23,4)
tup2: tuple = (3,23,(23,4,5,6) ,4) #nested tuple


'''Defining dictionary'''

#using curly braces {}
dict1: dict = {"Nishidh": 1, "Rihit": 2} #{key:value}

#using dict function
rand_list: list[tuple] = [("Naina", 1),("Heaven", 2),("Hell", 3)]
dict2 = dict(rand_list) #{'Naina': 1, 'Heaven': 2, 'Hell': 3}
dict3 = dict(nishidh= "value1", key2 = "value2" ) 

#using dict comprehension
my_dict5 = {key: key**2 for key in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#using fromkeys
my_dict4 = dict.fromkeys(["key1", "key2", "key3"], "default_value")

#using zip function : combine to iterables in key: val pair 
keys = ["key1", "key2", "key3"]
values = [1, 2, 3]
my_dict1 = dict(zip(keys, values))

#nested dictionaries
my_dict2 = {"key1": {"subkey1": "value1"}, "key2": {"subkey2": "value2"}}

#using collections module
from collections import defaultdict
my_dict3 = defaultdict(0)  # Default value is 0 for any missing key

'''Defining list'''

#using square brackets
my_list = [1, 2, 3, 4, 5]

#using list constructor
my_list1 = list([1, 2, 3, 4, 5])
empty_list = list() #[]

#Using List Comprehension
my_list3 = [x**2 for x in range(5)]  # Output: [0, 1, 4, 9, 16]

#using repition
my_list = [0] * 5  # Output: [0, 0, 0, 0, 0]

#using range 
my_list = list(range(5))  # Output: [0, 1, 2, 3, 4]

#nested lists 
my_list = [(1, 2), (3, 4), (5, 6)]
nested_list = [[1, 2], [3, 4], [5, 6]]

#using other datatypes
my_list = list((1, 2, 3))
my_list = list("abc")  # Output: ['a', 'b', 'c']
my_list = list({1, 2, 3})
list1 = [1, 2]
list2 = [3, 4]
my_list = list1 + list2  # Output: [1, 2, 3, 4]

#using extend function
my_list = [1, 2]
my_list.extend([3, 4])  # Output: [1, 2, 3, 4]


''' Defining string '''

#using "" or ''
my_string = 'Hello, World!'

#using """""" or ''''''
my_string = '''This is a
multi-line string.'''
my_string = """This is a
multi-line string"""

# using str construcutor
my_string = str(12345)  # Output: '12345'

#using raw strings : use to make the strings raw as it is
my_string = r'C:\Users\Name\Documents'  # Output: 'C:\\Users\\Name\\Documents'

#byte strings
my_string = b'Hello, World!'  # Output: b'Hello, World!'

#unicode stirng
my_string = u'Hello, World!'

#using concatenation
my_string = 'Hello, ' + 'World!'

#formatting

#fstring
name = "Alice"
my_string = f"Hello, {name}!"

#format
my_string = "Hello, {}!".format("World")

#%s
my_string = "Hello, %s!" % "World"

#using escape char
my_string = "Hello, \"World!\"" #Hello, "World!"


''' {int, boolean, float, floor} '''

num1 = 1
print(type(num1), f':{num1}')
num1 = 2.2
print(type(num1), f':{num1}')

bool1 = True
print(type(bool1), f':{bool1}')
bool1 = False
print(type(bool1), f':{bool1}')

