"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    if head != None:
        linkList = []
        while head != None:
            if head.data in linkList:
                return True
            else:
                linkList.append(head.data)
                head = head.next
    else:
        return False