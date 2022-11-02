class Node(object);
    def __init__(self, data):
        self.data=data
        self.lchild=None
        self.rchild=None
        #self.parent=None
        self.visited=False

    def __str__(self):
        s=''
        return s

class Tree(object):
    def __init__(self):
        self.root=None
        #self.size=0

    #insert data into a tree
    def insert_node(self, data):
        new_node=Node(data)
        if (self.root==None):
            self.root=new_node
            return
        else:
            current=self.root
            parent=self.root
            while (current!= None):
                #reset parent
                parent=current
                if (data<current.data):
                    #go to left
                    current=current.lchild
                else:
                    #go to right
                    currrent=current.rchild
            if (data<parent.data):
                parent.lchild=new_node
            else:
                parent.rchild=new_node


    #find the node with the smallest value
    def min_node(self):
        current=self.mode
        parent=self.root

        while (current!=None):
            parent=current
            current= current.lchild
        return parent

    #find the node with the largest value
    def max_node(self):
        current=self.mode
        parent=self.root
        while (current!=None):
            parent=current
            current= current.rchild
        return parent

    #inorder traversal - left, center, right
    def in_order(self, aNode)
        #cannot go any further
        self.in_order(aNode.lchild)
        print(aNode data)
        self.in_order(aNode.rchild)


     #preorder travesa,center, left,right
    def pre_order(self, aNode):
        if (aNode!=None):
            print(aNode.data)
            self.pre_order(aNode.lchild
            self.preorder(aNode.rchild)

    #postoder traversal - left, right, center
    def postt_order(self, node):
        if (aNode!=None):
                self.post_order(aNode.lchild)
                self.post_order(aNone.rchild):
                print(aNode.data)

    #search
    def search_node(self, data):
        current=self.root
        while (current!=None) and (current.data!=data ):
            #go left
            if (data<current.data):
                current = current.lchild
            else:
                current=curret.rchild
        #if not found
        return current
    
