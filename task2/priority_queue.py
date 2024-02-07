class PriorityQueue:
    def __init__(self):
        self.elements = []
        self.elements_with_importance = {}
        self.importances = []

    def __len__(self):
        return len(self.elements)    
    
    def __list__(self):
        self.elements.sort(key=lambda x: x[1])
        print(self.elements)

    def push(self, item, importance):
        self.elements.append(item)
        self.elements_with_importance.append((item, importance))
        self.elements.sort()

    def pop(self):
        if not self.elements:
            raise IndexError("Trying to pop from an empty priority queue")
        for i in self.elements_with_importance:
            self.importances.append(i[1])
        sort = (sorted(self.importances))
        highest = sort[0]
        index = 0
        for i in self.elements_with_importance:
            if i[1] ==  highest:
                print(self.elements[index])
                del self.elements_with_importance[index]
                del self.elements[index]   
            index += 1        

    def __empty_pop__(self):
        pass

    def __interation__(self):
        pass



"""
priority_queue = PriorityQueue()
priority_queue.push("Task 1", 3)
priority_queue.push("Task 2", 1)
priority_queue.push("Task 3", 2)

print("Priority Queue Length:", len(priority_queue))

print("Tasks in Priority Order:")
for task in priority_queue:
    print(task)

print("Processing tasks in Priority Order:")
while len(priority_queue) > 0:
    task = priority_queue.pop()
    print("Processing:", task)

"""

