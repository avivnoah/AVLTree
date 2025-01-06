# AVL Tree Project
- A self-balancing binary search tree
- used rotations to maintain the balance factor of each node.
- Motivation: reduce the worst-case time complexity for search, insert, and delete operations to O(log n).
![354638835-9e4ac839-499b-4deb-8786-12c183aa1fb0](https://github.com/user-attachments/assets/0982bc20-acd4-44a4-9a46-5ecddfda3134)
![354635585-e3b975e9-d8ae-4f0a-911b-a26eb050e98b](https://github.com/user-attachments/assets/fb3ddbe0-2512-4aff-ba82-6f38c2a3b211)
## Methods Description:

```bash
class Node:
    def __init__(self, key, value):
        """
        Fields:
            'key': int
            'value': string
            'parent': AVLNode instance
            'left': AVLNode instance
            'right': AVLNode instance
            'height': int
        Output:
            -
        Description:
            Constructor for AVLNode. if empty, height is -
        Time Complexity:
            Overall O(1), as all methods are constant.
        """
    
    def get_parent(self):
    """
		  Input:
			  self - a node
		  Output:
			  Node's parent
		  Description:
			  Return node's parent
		  Time Complexity:
			  Overall O(1), as all methods are constant.
		"""
  
    def get_height(self):
    """
  		Input:
  			self - a node
  		Output:
  			Node's height
  		Description:
  			Return node's height
  		Time Complexity:
  			Overall O(1), as all methods are constant.
		"""
    def is_real_node(self):
		"""
		Input:
			self - a node
		Output:
		 	False if self is a virtual node, True otherwise.
		Description:
		 	Returns whether self is not a virtual node
		Time Complexity:
		 	Overall O(1), as all methods are constant.
		"""
    
    def find_height(self):
		"""
		Input:
			self - a node
		Output:
			Updated height of self
		Description:
			calculate the height of self using the height of its children
		Time Complexity:
			Overall O(1), as all methods are constant.
		"""
    
    def update_height(self):
		"""
		Input:
			self - a node
		Output: -
		Description:
			update node's height
		Time Complexity:
			Overall O(1), as all methods are constant.
		"""
    
    def successor(self):
		"""
		Input:
			self - a node
		Output:
			the successor of self
		Description:
			if node has a right node, traverse to its left most child(repeatedly), returning it
			otherwise, climb up until we reach the first node that's not the right child of its parent,
			if it has a parent return it, otherwise, return virtual node, as there's no successor(it's the max node)
		Time Complexity:
			O(log n)
			The time complexity for this method is O(log n).
			The method traverses at most two path:
				1. From the node up to the root.
				2. From root to nodes successor.
			The length of each path is at most O(log n).
			Thus,overall the time complexity of this method is O(log n).
		"""
    
    def update_parent(self, up_parent):
		"""
		Input:
			self - a node and up_parent which is the node to be updated as parent of self
		Output: -
		Description:
			update node's parent to be up_parent
		Time Complexity:
			Overall O(1), as all methods are constant.
		"""
    
    def update_left_child(self, up_left):
		"""
		Input:
			self - a node and up_left which is the node to be updated as left child of self
		Output: -
		Description:
			updating self left child to be up_left and up_left parent to be node
		Time Complexity:
			Overall O(1), as all methods are constant.
		"""
    
    def update_right_child(self, up_right):
		"""
		Input:
			self - a node and up_right which is the node to be updated as right child of self.
		Output:
			-
		Description:
			updating self right child to be up_right and up_right parent to be node.
		Time Complexity:
			Overall O(1), as all methods are constant.
		"""
    
    def is_leaf(self):
		"""
		Input:
			self - a node
		Output:
			False if self is not a leaf, True otherwise.
		Description:
			Returns whether self is a leaf
		Time Complexity:
			Overall O(1), as all methods are constant.
		"""
    
    def is_root(self):
		"""
		Input:
			self - a node
		Output:
			False if self is not a root, True otherwise.
		Description:
			Returns whether self is a root
		Time Complexity:
			Overall O(1), as all methods are constant.
		"""
    
    def has_only_left_child(self):
		"""
		Input:
			self - a node
		Output:
			returns True if self has only left child, False otherwise.
		Description:
			Returns whether self has only left child.
		Time Complexity:
			Overall O(1), as all methods are constant.
		"""
    
    def has_only_right_child(self):
		"""
		Input:
			'self': AVLNode instance
		Output:
			returns True if self has only right child, False otherwise.
		Description:
			Returns whether self has only right child.
		Time Complexity:
			Overall O(1), as all methods are constant.
		"""
    
    def node_type(self):
		"""
        Input:
            'self': AVLNode instance
        Output:
            @type: string
            returns the 'type' of a given root
        Description:
            types:
            "leaf" - the node is a leaf
            "virtual node" - the node is a virtual node
            "unary left" - the node is a unary left node(has only left child)
            "unary right" - the node is a unary right node(has only right child)
            "root" - the node is a root
            "just a node" - an ordinary two-child node
        Time Complexity:
            Overall O(1), as all methods are constant.
        """
    
    def get_balance_factor(self):
		"""
        Input:
            'self': AVLNode instance
        Output:
            @type: int
            returns the balance factor of a given root
        Description:
            returns the balance factor of a given root(left subtree size - right subtree size)
        Time Complexity:
            Overall O(1), as all methods are constant.
    """

    
class AVLTree(object):
    def __init__(self, root: AVLNode = AVLNode.virtual_node, max_tree_node: AVLNode = AVLNode.virtual_node,
				 size: int = 0):
        """
        Constructor method that builds an AVL tree with the given root. 
        If the root is virtual or empty, it will be defined as empty.
        """

    def convert_tree(self, tree):
		"""
        Input:
            'self': AVLTree instance
            'tree': AVLTree instance
        Output:
            -
        Description:
            Copies the root, size, and max_tree_node from 'tree' into self.
            Useful when we want to "turn" self into another tree without reconstructing nodes.
        Time Complexity:
            Overall O(1), as all methods are constant, only compares two given nodes.
    """

    def update_max_node(self, node: AVLNode):
		"""
        Input:
            'self': AVLTree instance
            'node': AVLNode instance
        Output:
            -
        Description:
            Updates the tree's max_tree_node if the given 'node' has a larger key.
            If the tree was empty, node becomes the new max by default.
        Time Complexity:
            Overall O(1), as all methods are constant, only compares two given nodes.
        """

    def fix_root(self):
		"""
        Input:
            -
        Output:
            -
        Description:
            If the current root has a parent (due to rotations), ascend until finding the actual root.
            Ensures 'self.root' is truly the topmost node.
        Time Complexity:
            Overall O(log n) in a balanced AVL, worst case O(h).
        """
	def create_root(self, key, val=None):
		"""
        Input:
            'key': int or None
            'val': string or None
        Output:
            -
        Description:
            Creates a new root for the AVLTree. If key is None, the new root is a virtual node and the tree is empty.
            Otherwise, creates a real node as the root and sets tree_size to 1.
        Time Complexity:
            Overall O(1), as all methods are constant.
        """

    def rearrange_parent(self, node, child):
		"""
		Input:
			'self': AVLTree instance
			'node': AVLNode instance
		Output:
			-
		Description:
			Reconnects 'child' into the position formerly occupied by 'node'.
            If 'node' was the root, 'child' becomes the new root.
            Otherwise, we update node's parent's left/right child accordingly.
		Time Complexity:
			Overall O(1), as all methods are constant.
		"""

    def left_rotation(self, node: AVLNode):
		"""
		Input:
			'self': AVLTree instance
			'node': AVLNode instance
		Output:
			-
		Description:
			Performs a left rotation on the given 'node'.
		Time Complexity:
			Overall O(1), as all methods are constant.
		"""

    def right_rotation(self, node: AVLNode):
		"""
		Input:
			'self': AVLTree instance
			'node': AVLNode instance
		Output:
			-
		Description:
			Performs a right rotation on the given 'node'.
		Time Complexity:
			Overall O(1), as all methods are constant.
		"""

    def rebalance_rotation(self, node: AVLNode):
		"""
		Input:
			'self': AVLTree instance
			'node': AVLNode instance
		Output:
			-
		Description:
			Called when a node's balance factor is out of the valid range (-1, 0, 1).
			Determines if it's a left-left, left-right, right-left, or right-right imbalance
			and performs the appropriate rotations to fix the AVL property.
		Time Complexity:
			Overall O(1), as all methods are constant.
		"""

    def search(self, key):
		"""
		Input:
			'self': AVLTree instance
			'key': int
		Output:
			a tuple (x,e) where x is the node corresponding to key (or None if not found),
			and e is the number of edges on the path between the starting node and ending node+1.
		Description:
			searches for a node in the dictionary corresponding to the key, starting at the root
		Time Complexity:
			Overall O(log n) at worst case(as seen in class), potentially faster if the finger is near insertion spot.
		"""
  
    def finger_search(self, key):
		"""
		Input:
			'self': AVLTree instance
			'key': int
		Output:
			a tuple (x,e) where x is the node corresponding to key (or None if not found),
			and e is the number of edges on the path between the starting node and ending node+1.
		Description:
			searches for a node in the dictionary corresponding to the key, starting at the max
		Time Complexity:
			Overall O(log i) at worst case(as seen in class), potentially faster if the finger is near insertion spot.
		"""

    def insert(self, key, val=""):
		"""
		Input:
			'self': AVLTree instance
			'key': int
			'val': string
		Output:
			a 3-tuple (x,e,h) where x is the new node,
			e is the number of edges on the path between the starting node and new node before rebalancing,
			and h is the number of PROMOTE cases during the AVL rebalancing
		Description:
			inserts a new node into the dictionary with corresponding key and value, starting at the root
		Time Complexity:
			Overall O(log n) in the worst case, potentially faster if the finger is near the insertion spot.
		"""
  
    def insertion_rebalance(self, node: AVLNode):
		"""
		Input:
			'self': AVLTree instace
			'node': AVLNode instance
		Output:
			@type: int
			returns the number of times a PROMOTE operation occurred (height increment).
		Description:
			After a new node is inserted, we traverse up from 'node' to the root,
			updating heights and checking balance factors. If any balance factor is out of range,
			we fix it via rebalance_rotation. We keep track of how many times the height
			was promoted (i.e., node.height increased).
		Time Complexity:
			Overall O(log n) - we ascend to the root at most O(log n) steps.
		"""
  
    def finger_insert(self, key=None, val=None):
		"""
		Input:
			'self': AVLTree instance
			'key': int
			'val': string
		Output:
			a 3-tuple (x,e,h) where x is the new node,
			e is the number of edges on the path between the starting node and new node before rebalancing,
			and h is the number of PROMOTE cases during the AVL rebalancing
		Description:
			inserts a new node into the dictionary with corresponding key and value, starting at the max
		Time Complexity:
			Overall O(log n) in the worst case, potentially faster if the finger is near the insertion spot.
		"""

    def find_max(self):
		"""
		Input:
			'self': AVLTree instace
		Output:
			@type: AVLNode instance
			returns the node with the maximum key in the tree
		Description:
			Traverses right children from the root until a virtual node is reached.
            Returns the last real node (the one with the greatest key).
		Time Complexity:
			Overall O(log n) in a balanced AVL, as studied in class.
		"""
  
    def bst_deletion(self, node: AVLNode):
		"""
		Input:
			'self': AVLTree instace
			'node': AVLNode instance
		Output:
			@type: AVLNode instance
			returns the new root of 'self'
		Description:
			Performs a standard BST deletion for 'node' without rebalancing.
			- If the node is a leaf, remove it directly.
			- If the node has one child, link that child to node's parent.
			- If the node has two children, find the successor and swap in place of the node.
			Returns the (possibly updated) root after the BST removal.
		Time Complexity:
			O(1) for linking and removing.
			Overall Finding the successor is O(log n).
		"""
  
    def delete(self, node: AVLNode):
		"""
		Input:
			The method receives tree2 whose keys are either smaller or larger, collectively, than
			the keys in self, and a key that separates them.
			'self': AVLTree instance
			'node': AVLNode instance
		Output:
			@type: AVLNode instance
			returns the new root of 'self'
		Description:
			Deletes 'node' from the AVLTree using bst_deletion for the raw removal,
			then climbs up the ancestors to rebalance if needed (rotations).
			Also updates the max_tree_node if the deleted node was the max.
		Time Complexity:
			bst_deletion costs O(log n)
			O(log n) - removal is O(log n) plus rebalancing up the tree at most O(log n) steps.
		"""
  
    def rebalace_for_join(self, node: AVLNode):
		"""
		Input:
			self: AVLTree instance
			node: AVLNode instance
		Output:
			returns the new tree's root after rebalancing
			return type: AVLTree instance
		Description:
			balances tree similarly to delete's rebalance methodology,
		Time Complexity:
			O(log n).
			The time complexity for this method is O(log n).
			In the worst case, traverse upwards costs O(log n) at most to reach our root.
			changing pointers costs & rotating costs O(1)
			In the end, Rebalance using 'rebalance_rotation' method, which costs O(1).
			Overall, the time complexity of join is O(log n).
		"""

    def join(self, tree2, key, val=""):
		"""
		Input:
			The method receives tree2 whose keys are either smaller or larger, collectively, than
			the keys in self, and a key that separates them.
			'self': AVLTree instance
			'tree2': AVLTree instance
			'key': int
			'val': string (optional)
		Output:
			-
		Description:
			It creates a node with the given key,val and merges the two trees into a single tree.
			The steps(conceptually):
				1) Places x so that one of its children is tree2's root and the other is self's root.
				2) Merges them at a level that matches the smaller tree's height.
				3) Rebalances if needed.
			In the worst case of differing heights, we traverse the taller tree
			to find where the smaller tree can attach. Then we perform pointer changes
			to attach x plus the smaller tree. Finally, we rebalance from x upward to the root.
			The "cost" can be thought of as the height difference + 1.
			Special cases:
				- If one of the trees is empty, this effectively becomes an insertion of key into the non-empty tree.
				- If both trees are empty, we just create a new root with (key, val).
			After the join, tree2 becomes empty.
		Time Complexity:
			O(log n).
			Tree traversal is at most O(log n) as seen in class
			possible rotations are each O(log n).
			Overall, the time complexity of join is O(log n).
		"""

    def split(self, node: AVLNode):
		"""
		Input:
			'self' is the tree we traverse
			'node' is the node to split by
			'self': AVLTree instance
			'node': AVLNode instance
		Output:
			'l_side' is the left side tree after split
			'r_side' is the right side tree after split
			'l_side': AVLTree instance
			'r_side': AVLNode instance
		Description:
			Splits the AVL tree into two AVL trees, 'l_side' and 'r_side', around 'node'.
			The keys < node.key will be in l_side; the keys > node.key will be in r_side.
			steps:
				1. Initialize l_side, r_side
				2. "Remove" 'node' from the chain by ascending to its parent
					and joining subtrees as you go up,
					ensuring keys < node.key go left, keys > node.key go right.
		Time Complexity:
			O(log n).
			The time complexity for this method is O(log n).
			In the worst case, traverse costs O(log n) to reach our desired node.
			changing pointers costs O(1),
			In the end, Rebalance using delete's rebalance method, which costs O(logn).
			Overall, the time complexity of join is O(log n).
		"""

    def avl_to_array(self):
		"""
		Input:
			'self' is the tree we traverse
		Output:
			a sorted list according to key of tuples (key, value) representing the data structure
		Description:
			inorder traversal, costs O(n) as learned in class
		Time Complexity:
			O(n)
		"""
  
    def max_node(self):
		"""
		Input:
			@type: AVLTree
			'self' is the tree we traverse
		Output:
			@type: AVLNode
			The maximal node of 'self'.
		Description:
			returns the biggest node of 'self'
		Time Complexity:
			O(1).
		"""

    def size(self):
		"""
		Input:
			@type: AVLTree
			'self' is the tree we traverse
		Output:
			@type: AVLNode
			The size of 'self'.
		Description:
			returns the size of 'self'
		Time Complexity:
			O(1).
		"""
    def get_root(self):
        """
        Input:
            @type: AVLTree
            'self' is the tree we traverse
        Output:
            @type: AVLNode
            The root of 'self'.
        Description:
            returns the root of 'self'
        Time Complexity:
            O(1).
        """  
```
