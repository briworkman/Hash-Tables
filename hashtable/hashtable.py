class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function
        Implement this, and/or DJB2.
        """
        h = 14695981039346656037
        for b in str(key).encode():
            h *= 1099511628211
            h ^= b
        return h

    def djb2(self, key):
        """
        DJB2 32-bit hash function
        Implement this, and/or FNV-1.
        """
        hash_value = 5382
        for c in key:
            hash_value = (hash_value * 33) + ord(c)
        return hash_value

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity
        # return self.fnv1(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        index = self.hash_index(key)  # * Find the hash index
        node = self.storage[index]
        if node is None:  # * If there is no node, add one
            self.storage[index] = HashTableEntry(key, value)
            return
        prev = node
        while node is not None and node.key != key:  # * Search the list for the key
            node = node.next
        if prev.key == key:  # * if it's there, replace the value
            prev.value = value
        else:  # * if it's not there, append a new record to the list
            prev.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)  # * Find the hash index
        node = self.storage[index]

        while node.next is not None and node.key != key:  # * Search the list for the key
            next = node.next
            if next.key == key:  # * if found, delete the node from the list
                node.next = next.next
        if node.key == key:
            self.storage[index] = node.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)  # * Find the hash index
        node = self.storage[index]
        while node is not None and node.key != key:  # * search the list for the key
            node = node.next
        if node is None:  # * if not found, return None
            return None
        else:  # * if found, return the value
            return node.value

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Implement this.
        """
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity
        for i in old_storage:
            if i == None:
                continue
            else:
                self.put(i.key)


if __name__ == "__main__":
    ht = HashTable(2)
    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")
    print("")
    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))
    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)
    print(f"\nResized from {old_capacity} to {new_capacity}.\n")
    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))
    print("")
