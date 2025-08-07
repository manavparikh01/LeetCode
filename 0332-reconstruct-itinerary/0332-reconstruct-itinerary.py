class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path = defaultdict(list)
        tickets.sort()
        for f, t in tickets[::-1]:
            path[f].append(t)
        main = []
        def dfs(f):
            while path[f]:
                t = path[f].pop()
                dfs(t)
            main.append(f)
        dfs("JFK")
        return main[::-1]
