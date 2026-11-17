class RecentCounter:

    def __init__(self):
        self.rc=0
        self.temp=[]

    def ping(self, t: int) -> int:
        t_r=[t-3000,t]
        self.temp.append(t)
        count=0
        for i in self.temp:
            if i>=t_r[0] and i<=t_r[1]:
                count+=1
        return count



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)