""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_(root):
    stack = []
    cur = root
    pre = None
    while (stack != [] or cur != None):
        if cur != None:
            stack.append(cur)
            cur = cur.left
        else:
            val = stack.pop()
            if pre != None and pre.data >= val.data:
                return False
            pre = val
            cur = val.right
    return True
