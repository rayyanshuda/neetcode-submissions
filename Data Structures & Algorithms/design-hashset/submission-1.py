class MyHashSet:

    def __init__(self):
        self.data = set()

    def add(self, key: int) -> None:
        # only add if the key is not in the hashset already
        self.data.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)
        

    def contains(self, key: int) -> bool:
        if key in self.data:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)