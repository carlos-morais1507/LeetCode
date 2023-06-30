class Solution:
    def isPalindrome(self, s: str) -> bool:
        tempStr = ""
        
        for char in s:
            if char.isalnum():
                tempStr += char.lower()
        
        return tempStr[::-1] == tempStr
        
        
    
    