"""
My Thought Process:
• The problem asks whether the string reads the same forwards and backwards.
• We don't need extra space because we can compare both ends directly.
• Since we need to process the left and right sides together, I immediately recognized the Two Pointer pattern.
• I also noticed that spaces and special characters should be ignored, so I skipped them before comparing.
• Finally, I compared the lowercase versions of both characters to make the comparison case-insensitive."""

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # We use two pointers.
        # left starts from the beginning.
        # right starts from the end.
        # We move both pointers towards the middle while comparing characters.

        left = 0
        right = len(s) - 1

        # Keep checking until both pointers meet or cross.
        while left < right:

            # Skip any character on the left that is not a letter or digit.
            while left < right and not s[left].isalnum():
                left += 1

            # Skip any character on the right that is not a letter or digit.
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare both characters after converting them to lowercase.
            # If they don't match, the string is not a palindrome.
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers inward.
            left += 1
            right -= 1

        # If every comparison matched, it is a palindrome.
        return True

"""
Pattern Recognized:
I recognized this as a Two Pointer problem because I needed to compare characters from both ends of the string while moving towards the center. Since the comparison only depends on the leftmost and rightmost characters at each step, using two pointers is the most efficient approach.

Approach:
1. Place one pointer at the beginning and one at the end.
2. Skip any characters that are not letters or digits.
3. Compare both characters after converting them to lowercase.
4. If they are different, return False.
5. Otherwise, move both pointers inward and continue.
6. If all comparisons match, return True.

Time Complexity: O(n)
Space Complexity: O(1)
"""
