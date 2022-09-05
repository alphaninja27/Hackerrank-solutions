def insert(self, val):
        #Enter you code here.
        new_node = Node(val)
        
        # Check if the tree is empty
        if self.root is None:
            # Tree is empty
            self.root = new_node
            return self.root
        else:
            # Tree is not empty
            current_node = self.root
            parent_node = None
            
            # Traverse the tree starting from the root node
            # until find the right position for the node
            while current_node is not None:
                if new_node.info >current_node.info:
                    #  Node's value is greater than current node

                    parent_node = current_node
                    current_node = current_node.right
                    direction = 'right'
                elif new_node.info <= current_node.info:
                    # Node's value is less than or 
                    # equal to the current node

                    parent_node = current_node
                    current_node = current_node.left
                    direction = 'left'
                    
            # Found the right position. Node goes here
            if direction == 'right':
                parent_node.right = new_node
            else:
                parent_node.left = new_node
            
        return self.root
