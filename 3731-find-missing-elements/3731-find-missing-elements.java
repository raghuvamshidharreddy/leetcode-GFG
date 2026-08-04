class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        HashSet<Integer> h1=new HashSet<>();
        HashSet<Integer> h2=new HashSet<>();
        for(int num:nums){
            h1.add(num);
        }
        int max=Integer.MIN_VALUE;
        int min=Integer.MAX_VALUE;
        for(int num:nums){
            max=Math.max(num,max);
            min=Math.min(num,min);
        }
        for(int i=min;i<=max;i++){
            h2.add(i);
        }
        Set<Integer> difference=new HashSet<>(h2);
        difference.removeAll(h1);
        List<Integer> l= new ArrayList<>();
        for(int num:difference){
            l.add(num);
        }
        Collections.sort(l);
        return l;
    }
}