class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]  #初始化栈stack
        dic ={')':'(','}':'{',']':'['}  #建立字典dict，key为右括号，value为左括号
        for char in s :  #遍历输入字符串s的每个字符char
            if char in dic :  #如果char在dict里（即为右括号）
                top = stack.pop() if stack else '#'  #弹出栈顶字符top
                if top != dic[char] :  #如果栈顶字符不是对应符号的左括号，返回无效
                    return False
            else :  #  如果char不在dict里（即为左括号），将char压入栈中
                stack.append(char)
        return not stack  #最后栈中还有字符，返回无效
