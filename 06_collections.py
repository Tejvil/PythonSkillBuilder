# collections
import collections
from collections import Counter
from collections import namedtuple
from collections import deque

# containers:
#     list
#     set
#     dict
#     tuple
# types:
#     Counter
#     deque
#     namedtuple
#     ordereddict
#     defaultdict



# Counter:
c= Counter("vivobook")
print(c)
c= Counter(["a","a","b","c","c"])
print(c)
c=Counter({"a":1, "b":2})
print(c)
c=Counter(cats=4, dogs=7)
print(c)    
# print(list(c.elements()))
# print(c.most_common(1))

c=Counter(a=4, b=2, c=0, d=-2)
d=Counter(["a","b","c","d"])

# c.subtract(d)
# print(c)
# c.update(d)
# print(c)
# c.clear()
# print(c)

print(c+d)
print(c-d)
print(c&d)
print(c|d)

print("*************************************")

# NamedTuple
Point = namedtuple('Point',"x y z")
Newp = Point (3,4,5)
print(Newp)                   #this works as any other tuple
print(Newp.x,Newp.y,Newp.z)
print(Newp[2])
print(Newp._fields)
print(Newp._replace(y=9))

print("*************************************")

# Deque
d = deque("HELLO")
d.append("4")
d.appendleft(5)
d.pop()
d.popleft()
d.clear()
d.extend("999")
d.extend("hey")
d.extend("what!!")
d.rotate(2)
# print(d)
q = deque("HELLO", maxlen=5)
q.append(2)
# q.extend([3,4,5])
print(q)

print("*************************************")

