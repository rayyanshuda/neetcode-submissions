class TrieNode:
    def __init__(self):
        self.children = {}   # maps char to TrieNode
        self.is_end = False  # marks end of a valid word

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                # Create a new branch if it doesn't exist yet
                curr.children[char] = TrieNode()

            # Step into that child node
            curr = curr.children[char]
        
        # after the loop ends, mark the last node as the end of the word
        curr.is_end = True


    def search(self, word: str) -> bool:
        curr = self.root 

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
    
            

        
        