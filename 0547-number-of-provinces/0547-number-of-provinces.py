class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        nProvinces = 0
        visited = set()
        
        def dfs(givenNeighborConnections):
            for anotherCity, isConnection in enumerate(givenNeighborConnections):
                if isConnection and anotherCity not in visited:
                    visited.add(anotherCity)
                    dfs(isConnected[anotherCity])
                    
        for city, neighborConnections in enumerate(isConnected):
            if city not in visited:
                nProvinces += 1
                dfs(neighborConnections)
                
        return nProvinces