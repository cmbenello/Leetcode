class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        # if timestamp < self.key_time_map[key][0][0]:
        #     return ""
        
        times = self.map[key]
        
        l, r = 0, len(times)
        res = ""
        while l < r:
            m = (l + r)//2
            if times[m][0] <= timestamp:
                l = m + 1
                res = times[m][1]
            
            else:
                r = m
            
        
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)