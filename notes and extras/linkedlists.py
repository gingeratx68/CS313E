class Link(object):
    def __init__(self, data, next=None):
        self.data=data
        self.next=next

class LinkedList(object):
    def __init__(self):
        self.first=None

    #add an item to the beginning of the list
    def insert_first(self, data):
        new_link=Link(data)

        #value is now none
        new_Link.next = self.first
        self.first= new_link

    #add item to the end of the list
    def insert_last(self, data):
        new_link=Link(data)

        current=self.first
        #if linked list empty
        if (current==None):
            self.first=new_link
            return
        #when linked list isnt empty
        while current.next!=None:
            current=current.neck

        current.next=new_link

    #find item in linkedlist
    def find_link(self, data):
        current=self.first
        #if list empty
        if (current==None):
            return None
        

        while (current.data!=data):
            if current.next== None
                return None
            else:
                current=current.next
        return current

    #delete a link with a given data
    def delete_link(self,data):
        previous=self.first
        current=self.first

        if (current==None):
            return None
        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous=current
                current=current.next

        if (current==self.first):
            self.first=current.next
        else:
            #deletes
            previous.next==current.next

        return current
