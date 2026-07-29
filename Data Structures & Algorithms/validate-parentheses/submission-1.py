class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to store opening brackets
        stack = []

        # Matching opening bracket for each closing bracket
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        # Traverse each character in the string
        for c in s:

            # If it's a closing bracket
            if c in pairs:

                # No opening bracket available to match
                if not stack:
                    return False

                # Get the last opening bracket
                top = stack.pop()

                # Check if brackets match
                if top != pairs[c]:
                    return False

            # It's an opening bracket
            else:
                stack.append(c)

        # Valid only if no unmatched opening brackets remain
        return not stack