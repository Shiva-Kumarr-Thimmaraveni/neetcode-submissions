class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for char in s:
            if char.isalpha():
                word += char
            if char.isdigit():
                word += char
        if word.lower() == word[::-1].lower():
            return True
        else:
            return False