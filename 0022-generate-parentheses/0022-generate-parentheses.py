class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recur(string,nopening,nclosing,res,n):
            if nopening+nclosing==2*n:
                res.add(''.join(string))
                return 
            if nopening<n:
                string.append('(')
                recur(string,nopening+1,nclosing,res,n)
                string.pop()
            if nclosing<nopening:
                string.append(")")
                recur(string,nopening,nclosing+1,res,n)
                string.pop()
        res=set()
        recur([],0,0,res,n)
        return list(res)