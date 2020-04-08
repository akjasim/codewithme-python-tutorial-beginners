# Lists in Python

"""
    What is a list?
    Constructing Lists - Two Types
    Indexing in Lists - Normal & Negative
    Slicing
    Change Item Value
    Loop
    Existence Checking
    Length of List
    append(), insert()
    remove(), pop(), del(), clear()
    Copy a list - copy(), list()
    Join lists - +, for loop & append (challenge), extend()
"""

# Constructing an empty list using []
mylist = []
print(mylist)

# Constructing an empty list using list() built-in method.
mylist = list()
print(mylist)

# Indexing in Lists - Normal
mylist = [1, 2.4, 'hi', True, [1, 3]]
print(mylist[3])

# Indexing in Lists - Negative
mylist = [1, 2.4, 'hi', True, [1, 3]]
print(mylist[-3])

# Slicing - Normal
mylist = [1, 2.4, 'hi', True, [1, 3]]
print(mylist[1: 3])

# Slicing - Negative
mylist = [1, 2.4, 'hi', True, [1, 3]]
print(mylist[-4: -1])

# Change Item Value
mylist = [1, 2.4, 'hi', True, [1, 3]]
mylist[2] = 'hello'
print(mylist)

# Looping through list
mylist = [1, 2.4, 'hi', True, [1, 3]]
for i in mylist:
    print(i)

# Existence checking
mylist = [1, 2.4, 'hi', True, [1, 3]]
if 'hi' in mylist:
    print(True)
else:
    print(False)

# Length of list
mylist = [1, 2.4, 'hi', True, [1, 3]]
print(len(mylist))

# append()
mylist = [1, 2.4, 'hi', True, [1, 3]]
mylist.append("hello")
print(mylist)

# insert()
mylist = [1, 2.4, 'hi', True, [1, 3]]
mylist.insert(1, 2)
print(mylist)

# remove()
mylist = [1, 2.4, 'hi', True, [1, 3]]
mylist.remove('hi')
print(mylist)

# pop()
mylist = [1, 2.4, 'hi', True, [1, 3]]
mylist.pop()
print(mylist)

# pop(index)
mylist = [1, 2.4, 'hi', True, [1, 3]]
mylist.pop(2)
print(mylist)

# del keyword
mylist = [1, 2.4, 'hi', True, [1, 3]]
del mylist[2]
print(mylist)

# clear()
mylist = [1, 2.4, 'hi', True, [1, 3]]
mylist.clear()
print(mylist)

# Copying a list - This is not possible as both points to the same list.
mylist = [1, 2.4, 'hi', True, [1, 3]]
newlist = mylist
newlist[2] = 'hello'
print(mylist)
print(newlist)

# copy()
mylist = [1, 2.4, 'hi', True, [1, 3]]
newlist = mylist.copy()
newlist[2] = 'hello'
print(mylist)
print(newlist)

# list()
mylist = [1, 2.4, 'hi', True, [1, 3]]
newlist = list(mylist)
newlist[2] = 'hello'
print(mylist)
print(newlist)

# Joining lists through concatenation (+)
mylist = [1, 2.4, 'hi', True, [1, 3]]
newlist = list(mylist)
print(mylist+newlist)

# Joining lists by using forloop and append()
mylist = [1, 2.4, 'hi', True, [1, 3]]
newlist = list(mylist)
for i in newlist:
    mylist.append(i)
print(mylist)

# Joining lists by using extend()
mylist = [1, 2.4, 'hi', True, [1, 3]]
newlist = list(mylist)
mylist.extend(newlist)
print(mylist)
