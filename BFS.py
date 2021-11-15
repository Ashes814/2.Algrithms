# 实现广度优先搜索

graph = {}
graph["you"] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

from collections import deque

search_queue = deque()  # Creat a queue
search_queue += graph['you']  # add all your neighbours


def person_is_seller(name): #check if the person is a mango dealer.
    return name[-1] == 'm'


def bfs(search_queue, graph):
    searched = []
    while search_queue:
        person = search_queue.popleft() #pop the first one in queue
        if person not in searched:
            if person_is_seller(person): #check whether the person is a mango seller
                print('{} is a mango seller!!!'.format(person))
                return True
    
            else:
                search_queue += graph[person] #add the person's all neigbours to this queue
                searched.append(person)
    return False

bfs(search_queue, graph)