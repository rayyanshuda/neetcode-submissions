class TrieNode:
    def __init__(self):
        self.children = {}   # maps char to TrieNode
        self.is_end = False  # marks end of a valid word

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                # create a new branch if it doesn't exist yet
                curr.children[char] = TrieNode()

            # step into that child node
            curr = curr.children[char]
        
        # after the loop ends, mark the last node as the end of the word
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.is_end
            if word[index] != ".":
                if word[index] not in node.children:
                    return False
                return dfs(index + 1, node.children[word[index]])
            else:
                # try matching the dot with every child node available
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True # found a path that works
                return False # none of the children match the rest of the word
        return dfs(0, self.root)
            
