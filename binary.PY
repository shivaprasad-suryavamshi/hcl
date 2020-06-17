# A binary tree node 
class Node: 
       
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None
       
def findLCA(root, n1, n2): 
      
    if root is None: 
        return None
  
    if root.key == n1 or root.key == n2: 
        return root  
   
    left_lca = findLCA(root.left, n1, n2)  
    right_lca = findLCA(root.right, n1, n2) 
  
    if left_lca and right_lca: 
        return root  
  
    return left_lca if left_lca is not None else right_lca 
  
  
root = Node(2) 
root.left = Node(1) 
root.right = Node(3) 
root.right.left = Node(4) 
root.right.right = Node(5) 
root.right.right.left = Node(6) 
 
print ("LCA(1,3) = ", findLCA(root, 1, 3).key )
print ("LCA(4,5) = ", findLCA(root, 4, 5).key )
print ("LCA(3,5) = ", findLCA(root, 3, 5).key )
print ("LCA(1,6) = ", findLCA(root, 1, 6).key )
