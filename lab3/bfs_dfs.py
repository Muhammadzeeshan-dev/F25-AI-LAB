graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

visited_bfs = []
q = []

def run_bfs(start, goal):
    q.append(start)
    
    while q:
        print("Q:", q, "| Visited:", visited_bfs)
        current = q.pop(0)
        
        if current not in visited_bfs:
            visited_bfs.append(current)
            
            if current == goal:
                break
                
            for child in graph[current]:
                q.append(child)

print("BFS ")
run_bfs("A", "G")
print("Final BFS Visited:", visited_bfs)
print("\n")


visited_dfs = []
st = []

def run_dfs(start, goal):
    st.append(start)
    
    while st:
        print("Stack:", st, "| Visited:", visited_dfs)
        current = st.pop()
        
        if current not in visited_dfs:
            visited_dfs.append(current)            
            if current == goal:
                break
            for child in reversed(graph[current]):
                st.append(child)

print(" DFS ")
run_dfs("A", "G")
print("Final DFS Visited:", visited_dfs)