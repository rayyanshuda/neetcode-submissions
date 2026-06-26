class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        prepend each word by the length of it
        add a separator between the length and word to isolate the word 
        (each word will be surrounded by "#" and a number)
        '''
        encoded = []
        for word in strs: 
            length = len(word)
            word1 = str(length) + "#" + word # length#word
            encoded.append(word1)
        
        x = "".join(encoded)
        return x

    def decode(self, s: str) -> List[str]:
        '''
        to separate the words again:
        1. Read the number -> 
        count that many characters after the separator 
        and then append that to a list
        2. continue till you reach the end of the string s in decode
        '''
        decoded = []
        i = 0
        while i < len(s):
            # logic for getting word length
            j = i
            while s[j] != "#":
                j += 1
            word_len = int(s[i:j])

            # getting each word separately
            word = s[j+1:j+word_len+1]
            decoded.append(word)
            i = j + word_len + 1

        return decoded
