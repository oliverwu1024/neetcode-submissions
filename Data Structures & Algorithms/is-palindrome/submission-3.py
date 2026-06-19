class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back =len(s) - 1

        while front < back:
            while front < back and s[front].isalnum()==False:
                front+= 1
            while front < back and s[back].isalnum()==False:
                back -= 1
            if s[front].lower() != s[back].lower():
                return False
            front+=1
            back-=1
        return True