class Node:
    size= 0
    def __init__(self,item,link):
        self.item = item
        self.next = link
        Node.size += 1
        
def insert_front(item):
    global head
    if Node.size != 0:
        head = Node(item,head)
    else:
        head = Node(item,None)

def print_list():
       p = head
       while p:
           if p.next != None:
            print(f'{p.item} -->', end='')
           else:
            print(p.item)
           p = p.next
        
if __name__ == '__main__':
    insert_front('apple')
    insert_front('cherry')
    insert_front('banana')
    print_list()