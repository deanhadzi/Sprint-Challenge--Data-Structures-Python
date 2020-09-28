class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # If the list is empty return None.
        if node == None:
            return None

        # Otherwise star the process of reversing the list.
        node_container = []

        # Step 1 - strip the current linked list and save all items.
        while True:
            # Append the current node.
            node_container.append(node)
            # Increment the current node to next node.
            node = node.get_next()
            # If this is the last node (pointer to None)
            # break the loop
            if node == None:
                break

        # Step 2 - create the new list.
        # Create the new head from the old list tail, by using built in pop method.
        self.head = node_container.pop()
        node = self.head
        # Point the head node to None in case it's List has one node length.
        node.set_next(None)

        # Iterate through the node_container until we have something in it.
        while node_container:
            # Get the next node in order.
            next_node = node_container.pop()
            # Set the pointer of the current node to next node.
            node.set_next(next_node)
            # Reassign the active node to the next node.
            node = next_node
            # Once we grab the last item from the container,
            # set it's pointer to None.
            if len(node_container) == 0:
                node.set_next(None)
