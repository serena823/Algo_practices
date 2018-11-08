
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        st=[]
        for i in s:
            if i == '(':
                st.append(')')
            elif i == '[':
                st.append(']')
            elif i=='{':
                st.append('}')
            elif (not st) or (st.pop() != i):
                return False
        
       
        return (not st)
                          
                