import numpy as np
import pandas as pd
df=pd.read_csv(r"C:\Users\DELL\Downloads\Bank_Personal_Loan_Modelling.csv")
df.drop(['ID','ZIP Code'],axis=1,inplace=True)
x=df.drop('Personal Loan',axis=1).values
y=df['Personal Loan'].values.reshape(-1,1)

NV = 10

def formPheremoneMatrix(graph):
    
    nv = len(graph)
    pheremones = np.ones((nv,nv))
        
    return pheremones
           
def chooseNextVertex(graph, pheremones, currPos):
    graph = 1/graph
    denominator = np.dot(graph[currPos], pheremones[currPos])
    numerator = graph[currPos] * pheremones[currPos]
    
    probabilities = numerator/denominator
    
    
    rouletteWheel = np.cumsum(probabilities)
    
    rouletteBall = np.random.random()
    
    nextVertex = np.where(rouletteWheel >= rouletteBall)[0][0]
    
    return nextVertex

def traverse(graph, pheremones, start, end):
    curr = start
    path = [curr]
    cost = 0
    prev = start
    
    while curr != end:
        nextVertex = chooseNextVertex(graph, pheremones, curr)
        
        while nextVertex == prev:
            nextVertex = chooseNextVertex(graph, pheremones, curr)
        
        cost += graph[curr][nextVertex]
        path += [nextVertex]
        prev = curr
        curr = nextVertex
        
    
    return path, cost
    
    

def releaseGeneration(graph, pheremones, start, end, size = 10):
    paths = []
    costs = []
    for i in range(size):
        p, c = traverse(graph, pheremones, start, end)
        paths += [p]
        costs += [c]
    costs = np.array(costs)    
    
    return paths, costs
    
def updatePheremones(paths, costs, pheremones, decay = 0):
    pheremones = (1-decay)*pheremones
    
    costs = 1/costs
    for p in range(len(paths)):
        path = paths[p]
        for i in range(len(path) - 1):
            pheremones[path[i]][path[i+1]] += costs[p]
    
    return pheremones
            

def generateProblem():
    graph = np.full(len(x), len(y), np.inf)
    
    for i in x:
        for j in range y:
            if x < density:
                if i!=j:
                    w = np.random.randn()
                    graph[i][j] = w
                    graph[j][i] = w
                    
    return graph

graph = generateProblem()


ph = formPheremoneMatrix(graph)
print(graph)


gen = 0
SIZE = 100

for i in range(100):
    p,c = releaseGeneration(graph, ph, 0, 7, SIZE)
    ph = updatePheremones(p, c, ph, decay = 0)
    gen += 1

    print("==============================",gen,"==============================")   
    c = np.array(c)
    unique, counts = np.unique(c, return_counts=True)
    print(unique)
    print(counts)
    
    if len(np.where(counts > SIZE//2)[0]) == 1:
        break
    

    
    
    
    
    
    