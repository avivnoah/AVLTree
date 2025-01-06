"""A class represnting a node in an AVL tree"""


class AVLNode(object):
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
        Constructor for AVLNode. if empty, height is -1

    Time Complexity:
        Overall O(1), as all methods are constant.
    """
	virtual_node = None

	def __init__(self, key=None, value=None, parent=None):
		self.key = key
		self.value = value
		self.parent = parent
		self.left = AVLNode.virtual_node
		self.right = AVLNode.virtual_node
		self.height = 0 if self.is_real_node() is True else -1

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
		return self.parent

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
		if self is None:
			return -1
		return self.height

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
		if self.key is None:
			return False
		return True

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
		if not self.is_real_node():
			return -1
		return max(self.left.height, self.right.height) + 1

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
		self.height = self.find_height()

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
		curr_node = self
		if not curr_node.right.is_real_node():
			while curr_node.parent and curr_node.parent.right == curr_node:
				curr_node = curr_node.parent
			return curr_node.parent if curr_node.parent else AVLNode.virtual_node
		else:
			curr_node = curr_node.right
			while curr_node.left.is_real_node():
				curr_node = curr_node.left
		return curr_node

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
		self.parent = up_parent

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
		self.left = up_left
		if up_left.is_real_node():
			up_left.parent = self
		self.update_height()

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
		self.right = up_right
		if up_right.is_real_node():
			up_right.parent = self
		self.update_height()

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
		if not self.is_real_node():
			return False
		if not self.right.is_real_node() and not self.left.is_real_node():
			return True
		return False

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
		if not self.parent:
			return True
		return False

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
		return self.left.is_real_node() and not self.right.is_real_node()

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
		return not self.left.is_real_node() and self.right.is_real_node()

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
		if self.is_leaf():
			return "leaf"
		elif not self or not self.is_real_node():
			return "virtual node"
		elif self.has_only_left_child():
			return "unary left"
		elif self.has_only_right_child():
			return "unary right"
		elif self.is_root():
			return "root"
		return "just a node"

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
		# Get the balance factor
		if not self.is_real_node():
			return 0
		return self.left.get_height() - self.right.get_height()


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
	"""
	Constructor, you are allowed to add more fields.
	"""
	if AVLNode.virtual_node is None:
		AVLNode.virtual_node = AVLNode(None, None)

	def __init__(self, root: AVLNode = AVLNode.virtual_node, max_tree_node: AVLNode = AVLNode.virtual_node,
				 size: int = 0):
		"""
        Fields:
            'root': AVLNode instance
            'max_tree_node': AVLNode instance
            'size': int
        Output:
            -
        Description:
            Constructor for AVLTree. If 'root' is a virtual node, the tree is considered empty.
            'max_tree_node' tracks the node with the largest key.
            'size' maintains the current number of real nodes in the tree.

        Time Complexity:
            Overall O(1), as all methods are constant.
        """
		self.root = root
		self.max_tree_node = max_tree_node
		self.tree_size = size

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
		# Make sure those are all the nodes we maintain
		# Turn self to tree
		self.root = tree.root
		self.tree_size = tree.tree_size
		self.max_tree_node = tree.max_tree_node

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
		if not self.max_tree_node.is_real_node() or self.max_tree_node.key < node.key:
			self.max_tree_node = node

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
		# Find the new root
		while self.root.parent:
			self.root = self.root.parent

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
		if key is None:
			new_root = AVLNode.virtual_node
			self.tree_size = 0
		else:
			new_root = AVLNode(key=key, value=val)
			self.tree_size = 1
		self.root = new_root
		self.max_tree_node = new_root

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
		parent = node.parent
		if not parent:
			self.root = child
			child.update_parent(None)
		else:
			if node.key <= parent.key:
				parent.update_left_child(child)
			else:
				parent.update_right_child(child)

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
		right_child = node.right
		self.rearrange_parent(node, right_child)
		node.update_right_child(right_child.left)
		right_child.update_left_child(node)
		right_child.update_height()
		node.update_height()

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
		left_child = node.left
		self.rearrange_parent(node, left_child)
		node.update_left_child(left_child.right)
		left_child.update_right_child(node)
		left_child.update_height()
		node.update_height()

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
		if node.get_balance_factor() == 2:  # left in-balanced
			if node.left.get_balance_factor() == 1:
				self.right_rotation(node)
			else:
				self.left_rotation(node.left)
				self.right_rotation(node)
		else:  # Right in-balanced
			if node.right.get_balance_factor() == -1:
				self.left_rotation(node)
			else:
				self.right_rotation(node.right)
				self.left_rotation(node)

	"""searches for a node in the dictionary corresponding to the key (starting at the root)
		
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
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
		c_node = self.root
		ed_vis = 0
		while c_node.is_real_node():
			if key == c_node.key:
				return (c_node, ed_vis + 1)
			elif key < c_node.key:
				c_node = c_node.left
				ed_vis += 1
			else:
				c_node = c_node.right
				ed_vis += 1
		if not c_node.is_real_node():
			c_node = None
		return (c_node, ed_vis)

	"""searches for a node in the dictionary corresponding to the key, starting at the max
	
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
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
		upwards_path_counter = 0
		climbing_node = self.max_node()
		while climbing_node.parent is not None and key <= climbing_node.parent.key:
			climbing_node = climbing_node.parent
			upwards_path_counter += 1
		result = list(AVLTree(climbing_node).search(key))
		#print("e:",result[1])
		#print("upwards_path_counter:", upwards_path_counter)
		result[1] = result[1] + upwards_path_counter
		return tuple(result)

	"""inserts a new node into the dictionary with corresponding key and value (starting at the root)

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: (AVLNode,int,int)
	@returns: a 3-tuple (x,e,h) where x is the new node,
	e is the number of edges on the path between the starting node and new node before rebalancing,
	and h is the number of PROMOTE cases during the AVL rebalancing
	"""

	# Inside the AVLTree class
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
		self.tree_size += 1
		parent_node = None
		curr_node = self.get_root()  # Trace route to insertion to get the parent
		e = 0  # path counter
		# Case 1: Parent is None(Empty tree)
		if not curr_node:
			self.create_root(key, val)
			return self.root, e, 0

		# Binary search - find the correct spot
		while curr_node.is_real_node():
			parent_node = curr_node
			if key < curr_node.key:
				curr_node = curr_node.left
			else:
				curr_node = curr_node.right
			e += 1
		# Creating new node to insert
		new_node = AVLNode(key, val, parent_node)
		# Case 2: Set the new node as a child of the parent
		if key < parent_node.key:
			parent_node.left = new_node
		else:
			parent_node.right = new_node
		promotions = self.insertion_rebalance(parent_node)
		self.fix_root()  # Fixing root - O(log(n))
		self.update_max_node(new_node)  # Check (& Update if necessary) tree's max node
		# After a new node is added, restore balance
		return new_node, e, promotions

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
		h = 0
		while node:
			balance_factor = node.get_balance_factor()
			if abs(balance_factor) <= 1:
				if node.height < node.find_height():
					h += 1
				node.update_height()
				node = node.get_parent()
			else:
				self.rebalance_rotation(node)
		return h

	"""inserts a new node into the dictionary with corresponding key and value, starting at the max

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: (AVLNode,int,int)
	@returns: a 3-tuple (x,e,h) where x is the new node,
	e is the number of edges on the path between the starting node and new node before rebalancing,
	and h is the number of PROMOTE cases during the AVL rebalancing
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
		self.tree_size += 1
		if not self.root.is_real_node():
			result = list(self.insert(key, val))
			return (result[0], result[1] + 0, result[2])
		upwards_path_counter = 0
		climbing_node = self.max_tree_node
		while climbing_node.parent is not None and key < climbing_node.parent.key:
			climbing_node = climbing_node.parent
			upwards_path_counter += 1
		result = list(AVLTree(climbing_node).insert(key, val))
		if self.max_tree_node.key < key:
			self.max_tree_node = result[0]
		self.fix_root()
		return (result[0], result[1] + upwards_path_counter, result[2])

	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
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
		node = self.root
		parent = node
		while node is not None and node.is_real_node():
			parent = node
			node = node.right
		return parent

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
		# Identify the type of the node to be deleted
		to_be_deleted_type = node.node_type()
		# Case 1: Node is a leaf
		if to_be_deleted_type == "leaf":
			parent = node.parent
			if parent is None:  # The node is the root
				self.root = AVLNode.virtual_node
			else:
				if parent.left == node:
					parent.update_left_child(AVLNode.virtual_node)
				else:
					parent.update_right_child(AVLNode.virtual_node)

		# Case 2: Node has one child (unary)
		elif to_be_deleted_type == "unary left" or to_be_deleted_type == "unary right":
			parent = node.parent
			child = node.left if to_be_deleted_type == "unary left" else node.right

			if parent is None:  # The node is the root
				self.root = child
				self.root.parent = None
			else:
				if parent.left == node:
					parent.update_left_child(child)
				else:
					parent.update_right_child(child)

		# Case 3: Node has two children
		else:
			parent = node.parent
			successor = node.successor()  # Find the successor (smallest node in the right subtree)
			successor_parent = successor.parent

			# Replace successor with its right child
			if successor_parent.left == successor:
				successor_parent.update_left_child(successor.right)
			else:
				successor_parent.update_right_child(successor.right)

			# Re-link the successor in place of the node to be deleted
			if parent is None:  # The node is the root
				self.root = successor
				self.root.parent = None
			else:
				if parent.left == node:
					parent.update_left_child(successor)
				else:
					parent.update_right_child(successor)

			# Update the successor's children
			successor.update_left_child(node.left)
			successor.update_right_child(node.right)
		return self.root

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
		# Delete node from self as in a regular BST ; 'parent' refers to the node's parent
		new_root = self.bst_deletion(node)
		temp = node.parent
		while temp:  #Performing rotations if necessary
			balance_factor = temp.get_balance_factor()
			if abs(balance_factor) <= 1:  #valid balance factor
				if temp.find_height() != temp.get_height():  #height has changed
					temp.update_height()
					temp = temp.get_parent()
				else:  #height has not changed
					temp = temp.get_parent()
			else:  #Invalid balance factor - rotations are needed
				self.rebalance_rotation(temp)
				temp = temp.get_parent()
		if node == self.max_tree_node:
			print("here")
			self.max_tree_node = self.find_max()
		return new_root

	"""joins self with item and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: the key separting self and tree2
	@type val: string
	@param val: the value corresponding to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key,
	or the opposite way
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
		# Delete node from self as in a regular BST ; 'parent' refers to the node's parent
		new_root = node
		temp = node
		while temp:  #Performing rotations if necessary
			balance_factor = temp.get_balance_factor()
			if abs(balance_factor) <= 1:  #valid balance factor
				if temp.find_height() != temp.get_height():  #height has changed
					temp.update_height()
			#else, height has not changed
			else:  #Invalid balance factor - rotations are needed
				self.rebalance_rotation(temp)
			temp = temp.get_parent()
		self.fix_root()
		return self.root

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
		# For split - handle empty trees
		if (tree2.root is None) and (self.root is None):
			root = AVLNode(key, val)
			self.root = AVLTree(root, root, 1)
			return
		elif tree2.root is None or not tree2.root.is_real_node():
			if self.search(key)[0] is None:
				self.insert(key, val)
				print(key)
			return
		elif self.root is None or not self.root.is_real_node():
			if tree2.search(key)[0] is None:
				tree2.insert(key, val)
			self.convert_tree(tree2)
			return

		# self is the highest after this block:
		if self.root.height < tree2.root.height:
			temp_vals = self.root, self.tree_size, self.max_tree_node
			self.convert_tree(tree2)
			tree2.root, tree2.tree_size, tree2.max_tree_node = temp_vals
		## Why does it go right side?
		descending_node = self.root
		x = AVLNode(key, val)
		x.height = tree2.root.height

		# Finding B and Attaching x
		if self.root.key > tree2.root.key:
			if abs(self.root.height - tree2.root.height) <= 1:
				x.left = tree2.root  # x's left son is a
				x.right = self.root  # x's right son is b
				self.root.parent = x  # x is b's parent
				tree2.root.parent = x  # x is a's parent
			else:
				descending_node_parent = descending_node.parent
				while descending_node.height > tree2.root.height:
					descending_node_parent = descending_node
					descending_node = descending_node.left
				x.left = tree2.root  # x's left son is a
				x.right = descending_node  # x's right son is b
				descending_node_parent.left = x  # c's left son is x
				tree2.root.parent = x  # x is a's parent
				x.parent = descending_node_parent  # c is x's parent
				if descending_node.is_real_node():
					descending_node.parent = x  # x is b's parent
		else:
			descending_node_parent = descending_node.parent
			if abs(self.root.height - tree2.root.height) <= 1:
				x.right = tree2.root  # x's left son is a
				x.left = self.root  # x's right son is b
				self.root.parent = x  # x is b's parent
				tree2.root.parent = x  # x is a's parent
			else:
				while descending_node.height > tree2.root.height:
					descending_node_parent = descending_node
					descending_node = descending_node.right
				x.right = tree2.root  # x's right son is a
				x.left = descending_node  # x's left son is b
				descending_node_parent.right = x  # c's right son is x
				tree2.root.parent = x  # x is a's parent
				x.parent = descending_node_parent  # c is x's parent
				if descending_node.is_real_node():
					descending_node.parent = x  # x is b's parent
		# Understand why not +1 as well
		self.tree_size = self.size() + tree2.size() + 1

		tree2.create_root(None)
		self.root = self.rebalace_for_join(x)

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
		curr_node = node
		l_side, r_side = AVLTree(curr_node.left), AVLTree(curr_node.right)
		curr_node = curr_node.parent
		# Find node's successor
		while curr_node is not None:
			left, right = AVLTree(curr_node.left), AVLTree(curr_node.right)
			left.root.parent = right.root.parent = None
			if curr_node.key < node.key:
				l_side.join(left, curr_node.key, node.value)
			else:
				r_side.join(right, curr_node.key, node.value)
			curr_node = curr_node.parent
		return l_side, r_side

	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of tuples (key, value) representing the data structure
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
		if self.root.is_real_node():
			return AVLTree(self.root.left).avl_to_array() + [(self.root.key, self.root.value)] + AVLTree(
				self.root.right).avl_to_array()
		return []

	"""returns the node with the maximal key in the dictionary

	@rtype: AVLNode
	@returns: the maximal node, None if the dictionary is empty
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
		return self.max_tree_node

	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
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
		return self.tree_size

	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
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
		if self.root.is_real_node():
			return self.root
		return None
