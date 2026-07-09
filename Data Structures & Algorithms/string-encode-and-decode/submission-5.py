class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''.join(str(len(word)) + "#" + word for word in strs)
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        # go thru the word
        # get the prefix number for length of encoded word
        # save that many characters to a list (append it)
        decoded_strs = []
        i = 0
        while i < len(s):
            start_of_number = i
            while s[i] != "#":
                i += 1
            length = int(s[start_of_number:i])
            word_start = i + 1
            decoded_strs.append(s[word_start:word_start + length])
            i = word_start + length
        return decoded_strs
