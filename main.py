def insertion_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 1:
        return
    insertion_sort_recursive(arr, n-1)
    last = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = last


arr = [12, 11, 18, 2, 6, 5]
insertion_sort_recursive(arr)
print("Sorted array:", arr)

#ex 2 

class CustomQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")
    
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty!")
            return None
        item = self.queue.pop(0)
        print(f"Dequeued: {item}")
        return item
    
    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty!")
            return None
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

q = CustomQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
print(f"Front of the queue: {q.peek()}")
