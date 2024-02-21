class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def __iter__(self):
        return iter([task[0] for task in self.queue])

    def push(self, task_name, priority):
        for i in range(len(self.queue)):
            if self.queue[i][1] < priority:
                self.queue.insert(i, (task_name, priority))
                return
        self.queue.append((task_name, priority))

    def pop(self):
        if len(self.queue) == 0:
            raise IndexError

        return self.queue.pop(0)[0]



""""
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
