import Vector as vec

v = vec.Vector(5)           # construct five-dimensional <0,0,0,0,0>
v[1] = 23                   # <0,23,0,0,0> (based on use of __setitem__)
v[-1] = 45                  # <0,23,0,0,45> (also via __setitem__)
print(v[4]) # index ke-4    # print 45 (via __getitem__)
u = v + v                   # <0,46,0,0,90> (via __add__)
print(u)                    # print <0,46,0,90>
total = 0                   
for entry in v:             # implicit iteration via __len__ and __getitem__
    total += entry 
print(total)

