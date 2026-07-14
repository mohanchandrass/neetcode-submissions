class Solution:
    def isValid(self, s: str) -> bool:

        hmap = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        stack =[]

        for ch in s:
            if ch in "({[":
                stack.append(ch)

            elif ch in ")}]":
                if not stack:
                    return False

                elif hmap[stack[-1]] == ch :
                    stack.pop()
                    
                else : 
                    return False

            
        
        if not stack:
            return True
        else:
            return False


        
        
    
        

        