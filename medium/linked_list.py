# ----------------------
# Problem HR : Remove Consecutive Duplicates from Sorted Linked List
# ----------------------

def deleteDuplicates(head):
    if not head or not head.next:
        return head
    curr = head
    while curr and curr.next:
        next_node = curr.next
        if curr.data == next_node.data:
            temp = next_node.next
            curr.next = temp
        else:
            curr = curr.next
        
    return head

# Delete duplicates from a list. 
# This runs in O(n) time complexity, with constant O(1) space.
        