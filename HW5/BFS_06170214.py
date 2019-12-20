from collections import defaultdict 

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 
        self.Queue = []
        self.Stack = []

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    
    def print_adj_ls(self):
        if self.graph == defaultdict(list):
            print(" No Node in graph !")
        else:
            print("adjacency list:")
            for key,val in self.graph.items():
                print(key, ":", val)
                
    def get_Q(self):
        if len(self.Queue) == 0:
            print("no data in queue !")
        else:
            item = self.Queue[0]
            self.Queue = self.Queue[1:]
            return item
        
    def put_Q(self, item):
        self.Queue = self.Queue+[item]
        
    def get_S(self):
        if len(self.Stack) == 0:
            print("no data in stack !")
        else:
            item = self.Stack[-1]
            self.Stack = self.Stack[:-1]
            return item
        
    def put_S(self, item):
        self.Stack = self.Stack+[item]
        
    def BFS(self, s):
        if len(self.graph.keys()) == 0:
            print("no data in Graph !")
        elif s not in self.graph.keys():
            print("start point isn't exist !")
        else:
            out = [s]
            print('output: ',out,'\n')
            for i in self.graph[s]:
                self.put_Q(i)
            while len(out) < len(self.graph.keys()):
                print('Queue: ',self.Queue)
                item = self.get_Q()
                if item is not None:
                    out.append(item)
                    print('add: ',item)
                    print('output: ',out,'\n')
                if (item is None) or (self.graph[item]==None):
                    continue
                for i in self.graph[item]:
                    if (i not in self.Queue) and (i not in out):
                        self.put_Q(i) 
            return out
        
    def DFS(self, s):
        if len(self.graph.keys()) == 0:
            print("no data in Graph !")
        elif s not in self.graph.keys():
            print("start point isn't exist !")
        else:
            self.put_S(s)
            out=[]
            while self.Stack:
                print('Stack: ',self.Stack)
                item = self.Stack[-1]
                if item not in out:
                    out.append(item)
                    for i in self.graph[item]:
                        if (i not in out)&(i not in self.Stack):
                            self.put_S(i)
                else:
                    self.get_S()
                print('output: ',out,'\n')
                    
            return out