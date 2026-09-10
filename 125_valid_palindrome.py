"""
Valid Palindrome - solution review
==================================

The implementation is correct for every test case, including the empty string
(size 0 falls into the even branch, where "" == "" holds). Time is O(n); it
uses O(n) extra space for the normalized string and the half-slices.

Observations
------------
1. The even/odd split is unnecessary. The whole check is
   `normalized == normalized[::-1]`. The manual half-slicing - especially the
   reverse bound `size // 2 - 1` with step -1 - is easy to get wrong and forces
   the reader to verify the index arithmetic. Comparing to the full reverse
   handles the middle character (odd case) and the empty/length-1 cases for
   free, so `size == 1` needs no special case either.
2. Implicit `return None`. There is no final `return`; every size other than 1
   happens to be covered by the even or odd branch, but nothing makes that
   obvious, and it contradicts the `-> bool` annotation. A single trailing
   `return <condition>` removes the risk.
3. `if size % 2 != 0` should be `else`, and each
   `if cond: return True else: return False` collapses to `return cond`.
4. O(1) space is achievable. A two-pointer walk over the original string,
   skipping non-alphanumerics in place, avoids building any new string.
5. Minor: trailing whitespace after `return True` on the trivial-case line.

Suggested revision - simple
---------------------------
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]
        return cleaned == cleaned[::-1]

Suggested revision - O(1) extra space (two pointers)
---------------------------------------------------
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Remove non alphanumeric characters and lower the string
        normalized_string: str = "".join([l for l in s if l.isalnum()]).lower()

        # String size
        size: int = len(normalized_string)

        # Trivial case
        if size == 1:
            return True 

        # Even case
        if size % 2 == 0:

            # Palindrome
            if normalized_string[0: size // 2] == normalized_string[-1: size // 2 - 1: -1]:
                return True
            
            # Not palindrome
            else:
                return False

        # Odd case
        if size % 2 != 0:
            
            # Palindrome
            if normalized_string[0: size // 2 + 1] == normalized_string[-1: size // 2 - 1: -1]:
                return True
            
            # Not palindrome
            else:
                return False

if __name__ == "__main__":

    # Case 1
    input1: str = "A man, a plan, a canal: Panama"
    output1: bool = True

    # Case 2
    input2: str = "race a car"
    output2: bool = False

    # Case 3
    input3: str = " "
    output3: bool = True

    assert Solution().isPalindrome(s=input1) == output1, \
        "Case 1 incorrect!"
    assert Solution().isPalindrome(s=input2) == output2, \
        "Case 2 incorrect!"
    assert Solution().isPalindrome(s=input3) == output3, \
        "Case 3 incorrect!"
    
    print(">>> All cases run successfully!")