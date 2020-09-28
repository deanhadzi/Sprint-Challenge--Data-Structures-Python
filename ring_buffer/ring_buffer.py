class RingBuffer:
    def __init__(self, capacity):
        # Capacity will be used as a measurement in logical expression.
        self.capacity = capacity
        # Create container to keep our data in place.
        self.container = []
        # Create the index pointer to the oldest item in the container.
        self.oldest_item = 0

    def append(self, item):
        # If the length of the container is smaller than capacity,
        # add items in order.
        if len(self.container) < self.capacity:
            self.container.append(item)

        elif len(self.container) == self.capacity:
            # If the container is full, start replacing the items,
            # begin at 0th index and then increment it.
            self.container[self.oldest_item] = item
            # Increment the index by 1.
            self.oldest_item += 1
            # If the oldest item equals capacity, reset it back to zero
            # so we don't exceed the capacity.
            if self.oldest_item == self.capacity:
                self.oldest_item = 0

    def get(self):
        # Simply return the container.
        return self.container
