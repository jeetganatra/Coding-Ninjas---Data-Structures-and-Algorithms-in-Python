class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    if head is None or head.next is None:
        return head, head
    smallHead, smallTail = reverse(head.next)  
    smallTail.next = head
    head.next = None
    
    return smallHead, head        
        
def kReverse(head, n):
   
  if head is None or head.next is None or n <= 0:
    return head
 
  curr = head
  tail = head

  cnt = 1
  while tail.next is not None:
    if cnt == n:
      break
    cnt += 1
    tail = tail.next
 
  nextHead = tail.next
  tail.next = None
  newHead, newTail = reverse(curr)
  newTail.next = kReverse(nextHead, n)
 
  return newHead


def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
l = kReverse(l, i)
printll(l)
