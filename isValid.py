class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[] #空栈
        dic ={')':'(','}':'{',']':'['} # 字典，
        for char in s :
            if char in dic :
                top = stack.pop() if stack else '#'
                if top != dic[char] :
                    return False
            else :
                stack.append(char)
        return not stack
