class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # two pointer approach
        # one pointer at start, one pointer at end
        # while left pointer is less than right pointer
        # create a temporary variable
        # hold the left value there
        # set left value to right value
        # set right value to temporary var
        # move left up, move right down

        left = 0
        right = len(s) - 1
        while left < right:
            temp = s[left]
            s[left] =  s[right]
            s[right] = temp
            left += 1
            right -= 1
        