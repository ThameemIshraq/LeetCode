class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for x,y in tickets:
            graph[x].append(y)
        for city in graph:
            graph[city] = sorted(graph[city])
        ans = []
        stack = ['JFK']
        while stack:
            top = stack[-1]
            if not graph[top]:
                ans.append(top)
                stack.pop()
            else:
                stack.append(graph[top][0])
                del graph[top][0]
        return ans[::-1]
