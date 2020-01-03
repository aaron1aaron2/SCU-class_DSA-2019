from collections import defaultdict 

#Class to represent a graph 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self,u,v,w): 
        self.graph_matrix[u][v]=w
        self.graph_matrix[v][u]=w
    
    def Dijkstra(self, s): 
        walked=[]
        result={node:0 for node in range(self.V)}
        cur = s
        while len(walked)<self.V:
            walked.append(cur)
            can_walk =[(n,c) for n,c in enumerate(self.graph[cur]) if (c!=0) and (n not in walked)]
            
            if len(can_walk)!=0:
                next_node = can_walk[0]
                
            for n,c in can_walk:
                new_cost = result[cur]+c
                if (result[n]==0) or (new_cost<result[n]):
                    result[n] = new_cost
                elif result[n]+c<result[cur]:
                    result[cur]=result[n]+c
            search = [(n,c)for n,c in result.items() if (c!=0) and (n not in walked)]
            
            if len(search)!=0:
                next_node = search[0]
                for n,c in search:
                    if c <next_node[1]:
                        next_node = (n,c)
                cur = next_node[0] 
                
        result={str(k):v for k,v in result.items()} # 把輸出的 key轉成字串

        return result
            
    def Kruskal(self):
        result = dict()
        group = []
        adj_w_dt = {idx:sorted([(cost,col)for col,cost in enumerate(row) if cost!=0]) for idx,row in enumerate(self.graph_matrix)}
        cur_edge = True
        while cur_edge:
            cur_edge = None # cur_edge = (row_idx,(cost,col_idx))

            for row,cost_ls in adj_w_dt.items():
                if len(cost_ls) ==0:
                    continue
                elif (cur_edge == None) :
                    cur_edge = (row,cost_ls[0])
                elif (cur_edge[1][0]>cost_ls[0][0]):
                    cur_edge = (row,cost_ls[0])
                    
            if cur_edge:
                adj_w_dt[cur_edge[0]].pop(0)
                if (cur_edge[0] in group) and (cur_edge[1][1] in group):
                    pass
                else:
                    group.extend([node for node in [cur_edge[0],cur_edge[1][1]] if node not in group])
                    name = '{}-{}'.format(cur_edge[0],cur_edge[1][1])
                    result[name] = cur_edge[1][0]
        return result