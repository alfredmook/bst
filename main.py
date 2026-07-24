class Node:
    """Node class for binary tree storing student records."""

    def __init__(self, id: int, name: str):
        """Initialize a new node with student record.

        Args:
            id: Student ID (used as sorting key)
            name: Student name
        """
        self.id = id
        self.name = name
        self.left = None
        self.right = None

    def preorder(self) -> list[dict]:
        """Return preorder traversal as list of dicts.

        Returns:
            List of {id, name} dicts in preorder (root, left, right)
        """
        list_of_dicts = [{"id": self.id, "name": self.name}]
        if self.left is not None:
            list_of_dicts.extend(self.left.preorder())
        if self.right is not None:
            list_of_dicts.extend(self.right.preorder())
        return list_of_dicts


    def inorder(self) -> list[dict]:
        """Return inorder traversal as list of dicts.

        Returns:
            List of {id, name} dicts in inorder (left, root, right)
        """
        list_of_dicts = []
        if self.left is not None:
            list_of_dicts.extend(self.left.inorder())
        list_of_dicts.extend([{"id": self.id, "name": self.name}])
        if self.right is not None:
            list_of_dicts.extend(self.right.inorder())
        return list_of_dicts

    def postorder(self) -> list[dict]:
        """Return postorder traversal as list of dicts.

        Returns:
            List of {id, name} dicts in postorder (left, right, root)
        """
        list_of_dicts = []
        if self.left is not None:
            list_of_dicts.extend(self.left.postorder())
        if self.right is not None:
            list_of_dicts.extend(self.right.postorder())
        list_of_dicts.extend([{"id": self.id, "name": self.name}])
        return list_of_dicts


class Tree:
    """Binary search tree for storing and managing student records."""

    def __init__(self):
        """Initialize an empty tree."""
        self.root = None

    def add(self, id: int, name: str) -> None:
        """Add a new student record to the tree.

        Args:
            id: Student ID (used as sorting key)
            name: Student name

        Note:
            If id already exists, this operation should be ignored.
        """
        if self.root is None:
            self.root = Node(id, name)
        else:
            curr_node = self.root
            node_placed = False
            while not node_placed:
                if id > curr_node.id:
                    if curr_node.right is None:
                        curr_node.right = Node(id, name)
                        node_placed = True
                    else:
                        curr_node = curr_node.right
                elif id < curr_node.id:
                    if curr_node.left is None:
                        curr_node.left = Node(id, name)
                        node_placed = True
                    else:
                        curr_node = curr_node.left
                else:
                    node_placed = True


    def find_node(self, id: int):
        """Find a student node by ID.

        Args:
            id: Student ID to search for

        Returns:
            Node object if found, None otherwise
        """
        if self.root is None:
            return None
        node_found = False
        curr_node = self.root
        while not node_found:
            if id == curr_node.id:
                return curr_node
            elif id > curr_node.id:
                if curr_node.right is None:
                    return None
                curr_node = curr_node.right
            elif id < curr_node.id:
                if curr_node.left is None:
                    return None
                curr_node = curr_node.left
        

    def preorder(self) -> list[dict]:
        """Return preorder traversal of tree.

        Returns:
            List of {id, name} dicts in preorder (root, left, right)
        """
        return [] if self.root is None else self.root.preorder()


    def inorder(self) -> list[dict]:
        """Return inorder traversal of tree.

        Returns:
            List of {id, name} dicts in inorder (left, root, right)
        """
        return [] if self.root is None else self.root.inorder()
        

    def postorder(self) -> list[dict]:
        """Return postorder traversal of tree.

        Returns:
            List of {id, name} dicts in postorder (left, right, root)
        """
        return [] if self.root is None else self.root.postorder()
        


# Sample data for testing
if __name__ == "__main__":
    # Create a new tree
    tree = Tree()

    # Add sample student records
    # Format: tree.add(id, name)
    tree.add(50, "Alice")
    tree.add(30, "Bob")
    tree.add(70, "Charlie")
    tree.add(20, "Diana")
    tree.add(40, "Eve")
    tree.add(60, "Frank")
    tree.add(80, "Grace")

    print("Tree created with sample data:")
    print(f"Inorder traversal (sorted by ID): {tree.inorder()}")
    print(f"Preorder traversal: {tree.preorder()}")
    print(f"Postorder traversal: {tree.postorder()}")

    # Test find_node
    print("\nTesting find_node:")
    node = tree.find_node(30)
    if node:
        print(f"Find ID 30: Found node with id={node.id}, name={node.name}")
    else:
        print("Find ID 30: Not found")

    node = tree.find_node(999)
    if node:
        print(f"Find ID 999: Found node with id={node.id}, name={node.name}")
    else:
        print("Find ID 999: Not found")

    print("\nTest complete! Run 'python test_main.py' to run automated tests.")
