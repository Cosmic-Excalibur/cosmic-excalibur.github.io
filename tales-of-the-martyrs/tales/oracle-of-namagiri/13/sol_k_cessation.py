from chal import *
import random
import uuid
import hashlib
from tqdm import trange
import networkx as nx
import matplotlib.pyplot as plt

ct = [2, 1, 1, 3, 1, 1, 3, 2, 1, 4, 1, 2, 3, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 3, 1, 6, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 3, 3, 2, 1, 1, 3, 1, 1, 1, 3, 4, 1, 3, 1, 2, 2, 4, 2, 5, 1, 1, 1, 3, 2, 1, 4, 2, 2, 1, 2, 1, 3, 1, 1, 1, 1, 1, 2, 3, 1, 2, 1, 1, 1, 1, 3, 4, 1, 2, 2, 4, 2, 5, 1, 2, 1, 2, 2, 1, 4, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 4, 3, 1, 2, 1, 3, 1, 3, 3, 2, 1, 3, 1, 6, 2, 1, 1, 2, 1, 2, 1, 3, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 2, 2, 3, 1, 1, 4, 1, 3, 1, 1, 1, 2, 1, 1, 2, 4, 1, 1, 5, 2, 4, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 3, 3, 1, 1, 1, 1, 1, 2, 1, 2, 3, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 5, 1, 1, 1, 3, 1, 1, 2, 3, 1, 2, 2, 2, 1, 3, 3, 1, 1, 2, 1, 1, 4, 3, 1, 3, 4, 1, 1, 1, 2, 1, 3, 1, 6, 1, 2, 1, 1, 3, 2, 3, 1, 2, 2, 1, 3, 2, 1, 2, 2, 2, 3, 3, 3, 1, 1, 2, 4, 1, 1, 1, 1, 1, 4, 2, 1, 4, 1, 2, 3, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 3, 2, 1, 2, 1, 1, 1, 4, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 2, 4, 2, 1, 4, 2, 4, 2, 2, 3, 1, 2, 2, 2, 1, 3, 3, 1, 2, 1, 1, 1, 1, 3, 3, 1, 3, 1, 1, 1, 1, 3, 1, 1, 4, 2, 5, 2, 1, 3, 1, 1, 2, 3, 1, 2, 2, 1, 1, 1, 1, 1, 1, 3, 1, 2, 1, 3, 1, 2, 3, 4, 4, 3, 2, 4, 2, 1, 4, 2, 4, 1, 2, 1, 3, 1, 2, 1, 1, 1, 3, 2, 1, 2, 2, 2, 3, 3, 1, 2, 1, 3, 1, 1, 1, 2, 1, 3, 4, 2, 1, 4, 1, 2, 1, 2, 2, 2, 1, 1, 2, 1, 1, 2, 2, 2, 1, 4, 2, 1, 4, 1, 1, 1, 1, 2, 4, 4, 3, 2, 4, 2, 1, 1, 1, 1, 1, 1, 1, 4, 2, 2, 3, 1, 1, 1, 2, 1, 3, 1, 4, 1, 2, 4, 1, 2, 3, 4, 1, 3, 1, 1, 1, 2, 4, 1, 1, 1, 4, 1, 1, 4, 2, 1, 4, 2, 2, 1, 1, 1, 1, 1, 2, 3, 2, 1, 4, 3, 3, 4, 4, 3, 2, 4, 2, 1, 1, 3, 2, 4, 1, 1, 2, 3, 1, 1, 1, 2, 2, 1, 1, 1, 1, 3, 1, 1, 1, 4, 3, 3, 1, 1, 2, 1, 1, 1, 1, 3, 1, 1, 4, 2, 5, 1, 1, 4, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 4, 3, 1, 1, 1, 1, 3, 4, 3, 1, 1, 4, 1, 6, 2, 1, 1, 1, 3, 1, 1, 3, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 4, 3, 1, 1, 5, 4, 1, 2, 2, 4, 1, 6, 1, 2, 1, 1, 3, 1, 4, 1, 2, 1, 2, 1, 1, 1, 1, 4, 2, 2, 3, 1, 2, 3, 1, 3, 4, 1, 1, 3, 4, 2, 5, 1, 1, 1, 3, 2, 2, 3, 2, 1, 2, 2, 2, 2, 3, 1, 2, 1, 3, 3, 3, 1, 1, 2, 1, 3, 3, 1, 1, 4, 2, 5, 2, 4, 1, 2, 4, 1, 2, 1, 2, 1, 1, 1, 2, 3, 1, 2, 4, 1, 1, 4, 4, 1, 1, 2, 3, 2, 4, 2, 5, 1, 2, 1, 2, 1, 1, 2, 3, 1, 2, 1, 2, 1, 1, 3, 1, 1, 2, 1, 2, 3, 1, 1, 1, 3, 4, 1, 1, 2, 1, 1, 1, 2, 4, 2, 1, 1, 3, 1, 2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 1, 3, 1, 1, 2, 1, 2, 3, 1, 1, 1, 3, 4, 1, 1, 2, 3, 1, 2, 3, 1, 6, 2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 4, 2, 1, 4, 1, 2, 3, 1, 1, 2, 1]
hash = 'd650078ae91d82ebd1d586110960a789c1a15e2cbc053b9daf8d8a4905950720:b840089ce93581869e9c02a7b5aefa7b'

def hashText(text, salt):
    """
        Basic hashing function for a text using random unique salt.
    """
    return hashlib.sha256(salt.encode() + text).hexdigest() + ':' + salt

def matchHashedText(hashedText, providedText):
    """
        Check for the text in the hashed text
    """
    _hashedText, salt = hashedText.split(':')
    return _hashedText == hashlib.sha256(salt.encode() + providedText).hexdigest()


def build(ct, K):
    graph = dict()
    rounds = []
    tmp = []
    s = -1
    for i, c in enumerate(ct):
        s += c
        if s >= K:
            s %= K
            rounds.append(tmp[:])
            tmp = []
        tmp.append(s)
    rounds.append(tmp[:])
    for idx, round in enumerate(rounds):
        for other in rounds:
            if round == other: continue
            i = 0
            j = 0
            tmp = None
            while 1:
                if j >= len(other): break
                if i >= len(round):
                    if idx < len(rounds) - 1 and tmp:
                        graph.update({tuple(sorted([other[j], tmp])): 0})
                    tmp = other[j]
                    j += 1
                elif other[j] < round[i]:
                    graph.update({tuple(sorted([other[j], round[i]])): 1})
                    if tmp:
                        graph.update({tuple(sorted([other[j], tmp])): 0})
                    tmp = other[j]
                    j += 1
                elif other[j] == round[i]:
                    tmp = None
                    i += 1
                    j += 1
                else:
                    tmp = None
                    i += 1
    return graph

def fuck(graph, K, show = True):
    G = nx.Graph()
    keys = set()
    
    for i, j in graph.items():
        G.add_edge(*i, weight = j)
        keys.add(i[0])
        keys.add(i[1])
    
    remnant = set(range(K)) - keys
    
    if show:
        elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.5]
        esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
         
        pos = nx.spring_layout(G)
        labels = dict((i, str(i)) for i in keys)
         
        nx.draw_networkx_nodes(G, pos, node_size=80)
        nx.draw_networkx_labels(G, pos, labels, font_size=8, font_color='r')
         
        nx.draw_networkx_edges(G, pos, edgelist=elarge, width=2)
        nx.draw_networkx_edges(G, pos, edgelist=esmall, width=1, alpha=0.5, edge_color='b', style='dashed')
        
        plt.axis('off')
        plt.show()

    n = nx.number_connected_components(G)
    components = list(nx.connected_components(G))
    
    print("Connected components:", n)
    print("Remnant:", list(remnant))
    
    for i in range(2**n*2**len(remnant)):
        wheel = [None]*K
        for idx, r in enumerate(remnant):
            wheel[r] = (i >> n >> idx) & 1
        for idx, component in enumerate(components):
            wheel[list(component)[0]] = (i >> idx) & 1
        while None in wheel:
            for edge, weight in graph.items():
                if wheel[edge[0]] != None:
                    a = edge[0]
                    b = edge[1]
                elif wheel[edge[1]] != None:
                    a = edge[1]
                    b = edge[0]
                else:
                    a = None
                if a != None:
                    assert wheel[b] != 1 - (wheel[a] ^ weight)
                    wheel[b] = wheel[a] ^ weight
        c = K_Cessation(wheel)
        pt = c.decrypt(ct)
        pt = decode_ascii_with_random_msb(pt)
        if matchHashedText(hash, pt):
            print()
            print("\x1b[32;1mFound Flag🚩:\x1b[0m")
            print(pt)

K = 64
graph = build(ct, K)
fuck(graph, K, show = True)