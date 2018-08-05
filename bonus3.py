
some_listsome_li  = [
    65, 81, 65, 19, 6, 28, 86, 40, 72, 27,
    76, 46, 22, 98, 49, 57, 52, 46, 47, 14,
    29, 15, 59, 74, 61, 47, 20, 33, 89, 99,
    65, 82, 84, 63, 93, 1, 42, 13, 54, 58,
    84, 17, 5, 18, 14, 14, 19, 42, 60, 77,
    17, 29, 2, 42, 42, 31, 47, 67, 15, 16,
    71, 56, 98, 46, 18, 20, 14, 36, 42, 23,
    87, 7, 5, 5, 52, 78, 76, 91, 92, 88, 38,
    66, 13, 18, 68, 96, 23, 51, 77, 93, 35,
    18, 9, 64, 51, 76, 76, 96, 5, 18
]

class MinHeap:
    def __init__(self):
        self.heap = []

    # build a new heap from a list of keys
    def build_heap(self, keys):
        self.heap = keys
        num = len(self.heap)
        for i in range(num//2, 0, -1):
            index = i
            next_level = 2 * i
            while next_level <= num:
                if next_level + 1 <= num:
                    if self.heap[index-1] >= self.heap[next_level-1] and self.heap[next_level-1] <= self.heap[next_level]:
                        temp = self.heap[index-1]
                        self.heap[index-1] = self.heap[next_level-1]
                        self.heap[next_level-1] = temp
                        index = next_level
                        next_level = index * 2

                    elif self.heap[index-1] >= self.heap[next_level] and self.heap[next_level-1] >= self.heap[next_level]:
                        temp = self.heap[index-1]
                        self.heap[index-1] = self.heap[next_level]
                        self.heap[next_level] = temp
                        index = next_level + 1
                        next_level = index * 2
                    else:
                        next_level *= 2
                else:
                    if self.heap[index-1] >= self.heap[next_level-1]:
                        temp = self.heap[index-1]
                        self.heap[index-1] = self.heap[next_level-1]
                        self.heap[next_level-1] = temp
                        index = next_level
                        next_level = index * 2
                    else:
                        next_level *= 2

    # add a new item to the heap
    def insert(self, item):
        self.heap.append(item)
        num = len(self.heap)
        for i in range(num//2, 0, -1):
            index = i
            next_level = 2 * i
            while next_level <= num:
                if next_level + 1 <= num:
                    if self.heap[index-1] >= self.heap[next_level-1] and self.heap[next_level-1] <= self.heap[next_level]:
                        temp = self.heap[index-1]
                        self.heap[index-1] = self.heap[next_level-1]
                        self.heap[next_level-1] = temp
                        index = next_level
                        next_level = index * 2

                    elif self.heap[index-1] >= self.heap[next_level] and self.heap[next_level-1] >= self.heap[next_level]:
                        temp = self.heap[index-1]
                        self.heap[index-1] = self.heap[next_level]
                        self.heap[next_level] = temp
                        index = next_level + 1
                        next_level = index * 2
                    else:
                        next_level *= 2
                else:
                    if self.heap[index-1] >= self.heap[next_level-1]:
                        temp = self.heap[index-1]
                        self.heap[index-1] = self.heap[next_level-1]
                        self.heap[next_level-1] = temp
                        index = next_level
                        next_level = index * 2
                    else:
                        next_level *= 2

    # return the item with the minimum key value, removing the item from the heap
    def del_min(self):
        min = self.heap[0]
        num = len(self.heap) -1
        self.heap[0] = self.heap[num]
        del self.heap[num]
        num = len(self.heap)
        for i in range(num//2, 0, -1):
            index = i
            next_level = 2 * i
            while next_level <= num:
                if next_level + 1 <= num:
                    if self.heap[index-1] >= self.heap[next_level-1] and self.heap[next_level-1] <= self.heap[next_level]:
                        temp = self.heap[index-1]
                        self.heap[index-1] = self.heap[next_level-1]
                        self.heap[next_level-1] = temp
                        index = next_level
                        next_level = index * 2

                    elif self.heap[index-1] >= self.heap[next_level] and self.heap[next_level-1] >= self.heap[next_level]:
                        temp = self.heap[index-1]
                        self.heap[index-1] = self.heap[next_level]
                        self.heap[next_level] = temp
                        index = next_level + 1
                        next_level = index * 2
                    else:
                        next_level *= 2
                else:
                    if self.heap[index-1] >= self.heap[next_level-1]:
                        temp = self.heap[index-1]
                        self.heap[index-1] = self.heap[next_level-1]
                        self.heap[next_level-1] = temp
                        index = next_level
                        next_level = index * 2
                    else:
                        next_level *= 2
        return min
    
    # print the minimum heap on the screen
    def display(self):
        print(self.heap)

heap = MinHeap()
heap.build_heap(some_listsome_li)
heap.display()
sort_heap = []
for i in range(0, len(some_listsome_li)):
    sort_heap.append(heap.del_min())
print(sort_heap)
