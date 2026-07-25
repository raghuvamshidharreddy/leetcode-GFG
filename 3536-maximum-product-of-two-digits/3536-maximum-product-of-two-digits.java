class Solution {
    public int maxProduct(int n) {
        int f=0,s=0;
        while(n!=0){
            int rem=n%10;
            if(f<rem){
                s=f;
                f=rem;
            }
            else if(rem>s  && rem<=f){
                s=rem;
            }
            n=n/10;
        }
        return s*f;
    }
}