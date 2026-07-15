x = [10,20,30,40.0,'python','java']
# python inbuilt functions for list:


print(x)                        # [10, 20, 30, 40, 'python', 'java']
print(type(x))                  # <class 'list'>
print(id(x))                    # 2086549436224
print(len(x))                   # 6
print(max(x))                   # TypeError: '>' not supported between instances of 'str' and 'float'
print(min(x))                   # TypeError: '<' not supported between instances of 'str' and 'float'
print(sum(x))                   # TypeError: unsupported operand type(s) for +: 'float' and 'str'


x = ['10','20','30','40.0','python','java']
print(max(x))                   # python

x = ['10','20','30','40.0','Python','java']
print(max(x))                   # java

x = [1,2,3,4,5,6,7,8,9,10]
print(max(x))                   # 10

x = ['python','pyxhon','java','PHP']
print(max(x))                   # pyxhon


x = ['python','pytthon','java','PHP']
print(max(x))                   # pytthon

x = ['python','python','java','PHP']
print(max(x))                   # python


x = ['z','123']
print(max(x))                   # z



# append()              # add single element at last position.
# extend()              # add multiple elements at last position
# clear()               # clear all elements from given list
# copy()                # create new object with different memory location
# count()               # count frequency of elements
# index()               # find element position
# insert()              # add single element in specific position
# pop()                 # remove element on the basis of tageted index number, bydefault it target last index.
# remove()              # remove targeted element.
# sort()                # arrenge in assending order.
# reverse()             # reverse out all given elements.
# # append()
# l = [11,2,3,4,5]
# x = "python"
# l.append(x)
# print(l)                # O/P:- [11, 2, 3, 4, 5, 'python']
# l = [11,2,3,4,5]
# x = 10
# l.append(x)





              
l = [11,2,3,4,5]
x = [10,'python','java']
l.append(x)
print(l)                
# O/P:- [11, 2, 3, 4, 5, [10, 'python', 'java']]
l = [11,2,3,4,5]
x = (10,'python','java')
l.append(x)
print(l)                
# extend()
l = [11,2,3,4,5]
x = 'python'
l.extend(x)
print(l)                
l = [11,2,3,4,5]
x = 10
l.extend(x)
print(l)                
l = [11,2,3,4,5]
x = 'pyt hon'
l.extend(x)
print(l)                
# O/P:- [11, 2, 3, 4, 5, (10, 'python', 'java')]
# O/P:- [11, 2, 3, 4, 5, 'p', 'y', 't', 'h', 'o', 'n']
# O/P:- TypeError: 'int' object is not iterable
# O/P:- [11, 2, 3, 4, 5, 'p', 'y', 't', ' ', 'h', 'o', 'n']
# insert('position', element):

l = [10,20,30,'python','java']
l.insert(0,100)
print(l)                 
# O/P:- [100, 10, 20, 30, 'python', 'java']


l = [10,20,30,'python','java']
l.insert(-1,100)
print(l)

  
l = [10,20,30,'python','java']
l.insert(-5,100)
print(l)

 
l = [10,20,30,'python','java']
l.insert(-2,100)
print(l)

 
# index(element,start,stop):-
l = [10,20,30,'python','java']
print(l.index(30))                  
# O/P:- 2


# count():-
l = [10,20,30,'python','java',10,20,10]
print(l.count(100))                 
print(l.count(10))                  
# O/P:- 0
# O/P:- 3


l = [10,20,30,'python','java',[10,20,10]]
print(l.count(10))                  
# O/P:- 1


# pop(index_no):- bydefault index_no is -1
l = [10,20,30,'python','java',10,20,10]
l.pop()
print(l)  


                          
# O/P:- [10, 20, 30, 'python', 'java', 10, 20]
l = [10,20,30,'python','java',10,20,10]
l.pop(3)
print(l)                            
# O/P:- [10, 20, 30, 'java', 10, 20, 10]


l = [10,20,30,'python','java',10,20,10]
l.pop(-2)
print(l)                            
# O/P:- [10, 20, 30, 'python', 'java', 10, 10]


# remove(element):-
l = [10,20,30,'python','java',10,20,10]
l.remove(10)
print(l)   

              
# O/P:- [20, 30, 'python', 'java', 10, 20, 10]
l = [10,20,30,'python','java',10,20,10]
l.remove('python')
print(l)  

               
# O/P:- [10, 20, 30, 'java', 10, 20, 10]
# copy():-
l = [10,20,30,'python','java',10,20,10]
l1 = l.copy()
print(l)                 
print(l1)                
print(id(l))             
print(id(l1))            
# clear()
# O/P:- [10, 20, 30, 'python', 'java', 10, 20, 10]
# O/P:- [10, 20, 30, 'python', 'java', 10, 20, 10]
# O/P:- 2605612971904
# O/P:- 2605612855616


l = [10,20,30,'python','java',10,20,10]
l.clear()
print(l,id(l))

del l
print(l)                 
# O/P:- NameError: name 'l' is not defined






# sort():-
l = [10,20,30,'python','java',10,20,10]
l.sort()                # TypeError: '<' not supported between instances of 'str' and 'int'
print(l)



l = [10,20,30,10,20,10]
l.sort()
print(l)                # [10, 10, 10, 20, 20, 30]


l = ['python','java','php','c']
l.sort()
print(l)                # ['c', 'java', 'php', 'python']



# reverse():-
l = ['python','java','php','c']
l.reverse()
print(l)



l = [10,20,30,10,20,10]
l.reverse()             # ['c', 'php', 'java', 'python']
print(l)                # [10, 20, 10, 30, 20, 10]



l = ['python','java','php','c']
l.sort()
print(l)                # ['c', 'java', 'php', 'python']  

 
l.reverse()
print(l)                # ['python', 'php', 'java', 'c']


l = ['python','java','php','c']
l.sort(reverse=True)
print(l)                # ['python', 'php', 'java', 'c']







#  C-R-U-D operations on list data type
l = [ ]
# create (add single element in empty list)
l.append(10)
l.append("python")
l.append([1,2,3,4,5])
l.append((1,2,3,4,5))
l.append({'x':10})

# Read
print(l)        # O/P:- [10, 'python', [1, 2, 3, 4, 5], (1, 2, 3, 4, 5), {'x': 10}]
print(l[1])     # O/P:- python


# update
l[1] = "Java"
print(l)        # O/P:- [10, 'Java', [1, 2, 3, 4, 5], (1, 2, 3, 4, 5), {'x': 10}]


# delete
del l[1]
print(l)        # O/P:- [10, [1, 2, 3, 4, 5], (1, 2, 3, 4, 5), {'x': 10}]
del l
print(l)        # O/P:- NameError: name 'l' is not defined