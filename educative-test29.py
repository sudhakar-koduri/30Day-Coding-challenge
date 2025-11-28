class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# from ds_v1.LinkedList.LinkedList import ListNode

def reverse_between(head, left, right):

  skip = left - 1
  curr_node = head
  previous = None
  while curr_node and skip >= 1:
     previous = curr_node
     curr_node = curr_node.next
     skip -= 1

  if not curr_node:
     return head
  
  rev_st = previous
  lt_st = curr_node
  for _ in range(left, right+1):
     next_node = curr_node.next
     curr_node.next = previous
     previous = curr_node
     curr_node = next_node
     next_val = None 
     if not curr_node:
        break

  if left == 1:
     head = previous
     lt_st.next = curr_node
  else:
    if rev_st:
        if rev_st.next:
            rev_st.next.next = curr_node
        rev_st.next = previous

  curr_node=head 
  res = []
  trails = 10
  while trails > 0 and curr_node:
    trails -= 1
    res.append(curr_node.val)
    curr_node = curr_node.next
  print(res)
  return head

def build_list():
    head = ListNode(-1)
    prev = head
    for x in [7,4,6,1,5,8]:
        curr = ListNode(x)
        prev.next = curr
        prev = curr
    return head.next
reverse_between(build_list(), 2,5)
reverse_between(build_list(), 1,6)
reverse_between(build_list(), 3,6)

# Using dummy node as head
# Function to reverse the sublist within the linked list
def reverse_between_sol(head, left, right):
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    curr = prev.next

    for _ in range(right - left):
        next_node = curr.next
        curr.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node

    return dummy.next