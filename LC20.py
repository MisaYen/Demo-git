class Solution(object):
    def isValid(self, s):
        if len(s) == 1:
            return False
        if s.count('(') != s.count(')') or s.count('[') != s.count(']') or s.count('{') != s.count('}'):
            return False
        if '()' not in s and '[]' not in s and '{}' not in s:
            return False
        for i in range(len(s)):
            if s[i] == "(":
                if ")" not in s[i+1::2]:
                    return False
            if s[i] == "[" :
                if "]" not in s[i+1::2]:
                    return False
            if s[i] == "{" :
                if "}" not in s[i+1::2]:
                    return False
        return True

'''
最佳解 利用Stack的特性!!!
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        if not s:
            return True
        if not(s[0]=="(" or s[0]=="{" or s[0]=="["):
            return False
        for p in s:
            if p=="(" or p=="{" or p=="[":
                stack.append(p)
            else:
                if stack:
                    if p==')' and stack[-1]=='(':
                        stack.pop()
                    elif p=='}' and stack[-1]=='{':
                        stack.pop()
                    elif p==']' and stack[-1]=='[':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if not stack:
            return True
        else:
            return False '''