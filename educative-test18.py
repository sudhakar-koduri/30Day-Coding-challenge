# Definition for a Linked List node
class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# from linked_list import LinkedList
# from linked_list_node import LinkedListNode

def merge_two_lists(head1, head2):
    head = LinkedListNode(-1) 
    root = head
    while head1 != None and head2 != None:
        if head1.data < head2.data :
            head.next = head1
            head1 = head1.next
        else:
            head.next = head2
            head2 = head2.next
        head = head.next    
    if head1 :
        head.next = head1 
    if head2 :
        head.next = head2    
    return root.next

list1 = [1,12,21,34,38,43,45,53,58,62,68,74,78,85,94]
head1 = LinkedListNode(list1[0])  
current = head1
for i in range(1, len(list1)):
    new_node = LinkedListNode(list1[i])
    current.next = new_node
    current = new_node
list2 = [7,25,40,47,56,69,83]
head2 = LinkedListNode(list2[0])  
current = head2
for i in range(1, len(list2)):
    new_node = LinkedListNode(list2[i])
    current.next = new_node
    current = new_node
head = merge_two_lists(head1 , head2)
while head:
    print(head.data," ")
    head = head.next