graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

def dls(node, end, limit, path):
    if node == end:
        return "FOUND", path
        
    if limit == 0:
        return "CUTOFF", []
        
    stop = False
    
    for n in graph[node]:
        if n not in path:
            ans, p = dls(n, end, limit - 1, path + [n])
            
            if ans == "FOUND":
                return "FOUND", p
                
            if ans == "CUTOFF":
                stop = True
                
    if stop == True:
        return "CUTOFF", []
    else:
        return "FAILURE", []

for i in [1, 2, 3, 4]:
    ans, p = dls("A", "G", i, ["A"])
    print(i, ans, p)