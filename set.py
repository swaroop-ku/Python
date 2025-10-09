s = {1,2,3}
print(type(s))
print(s)

s.add(5)
print(s)

s.discard(3)
print(s)

s.clear()
print(s)

s1 = {1,2,6}
s2 = {4,5,6}
print(s1.union(s2)) #union of two sets
print(s1.intersection(s2))  #intersecton of sets
print(s1.difference(s2))    #difference

#frozen set
f = frozenset([1,2,3])
print(type(f))
print(f)