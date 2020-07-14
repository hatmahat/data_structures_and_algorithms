from random import randrange
from min_heap import MinHeap

min_heap = MinHeap()
descending_nums = [n for n in range(10001, 1, -1)]
print("ADDING!")
for el in descending_nums:
    min_heap.add(el)

print("REMOVING!")
min_heap.retrieve_min()