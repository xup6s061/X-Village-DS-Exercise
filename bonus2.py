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

heap.build_heap([9, 5, 6, 2, 3])
# heap.build_heap(some_listsome_li)
heap.display()

heap.insert(1)
heap.insert(7)
heap.display()

print(heap.del_min())
print(heap.del_min())
heap.display()
