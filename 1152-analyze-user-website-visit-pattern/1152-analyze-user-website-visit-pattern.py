class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        
        users = {}
        for (time, user, web) in sorted(zip(timestamp, username, website)):
            if user in users:
                users[user].append(web)
            else:
                users[user] = [web]
                
        # have a list of all the websites that each user visits, generate the combos from this will save work then save res in a dictionary
        combs = {}
        
            
        for (user, websites) in users.items():
            webs = set((combinations(websites, 3)))
            for web in webs:
                if web in combs:
                    combs[web] += 1
                else:
                    combs[web] = 1
        
        
        max_pattern, max_score = "", 0
        
        for pattern, score in combs.items():
            if score > max_score or (score == max_score and pattern < max_pattern):
                max_score = score
                max_pattern = pattern
                
        return max_pattern
        