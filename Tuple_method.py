# # count ('element')
# t  =  (10,20,30,40, 'python', 10)

# print(t.count(10))
# print(t.count(100))
# print(t.count())


# # index (element, start, stop):- 

# t = (10,20,30, 'python',10)
# print(t.index(10))
# print(t.index(10,1))
# print(t.index(10,1,5))

import sys

l =[]
t = ()
print(id (l),id(t))
print(sys.getsizeof(l))



l = [10]
t = (10)
print(sys.getsizeof(l))     
print(sys.getsizeof(t)) 



l = ['python']
t = ('python')
print(sys.getsizeof(l))     
print(sys.getsizeof(t)) 