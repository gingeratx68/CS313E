class Queue(object):
    def __init__(self):
        self.queue=[[

    #add item to the end of the queue
    def enqueue (self, item):
        self.queue.append(item)

    #remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    #check if queue is empty
    def is_empty(self):
        return (len(self.queue)==0)

    #return the number of elements in the queue
    def size(self):
        return (len(self.queue()))
