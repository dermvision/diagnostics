import os
from string import join, lowercase, uppercase

def taxonomy_from_paths(P):
    
    T = {}
    for p in P:
        t = T
        for k in p:
            if k not in t.keys(): t[k] = {}
            t = t[k]
            
    return T

def paths_from_taxonomy(T):
    
    def f(T, p=[]):
        for k in sorted(T.keys()):
            if T[k] == {}: 
                P.append(p+[k])
            else:
                f(T[k], p+[k])
    
    P = []
    f(T)
    
    return P

def save_paths(P, f):
    with open(f, 'wb') as file:
        for p in P: file.write('{}\n'.format(join(p,'/')))

def read_paths(f, path_filter = lambda s: True):

    with open(f, 'rb') as file: P = file.readlines()
    
    P = filter(path_filter, P)
    P = [[k.split('-') for k in p.split('/')] for p in P]
    
    fix = lambda k: filter(lambda c: c in lowercase, k.lower())
    P = [[join(map(fix, k), '-') for k in p] for p in P]
    
    return P

def save_taxonomy(T, p):
    for k in T.keys():
        q = os.path.join(p, k)
        if T[k] == {}:
            with open(q, 'wb') as file: file.write(k)
        else:
            if not os.path.exists(q): os.makedirs(q)
            save_taxonomy(T[k], q)

def read_taxonomy(p):
	# TODO
	return

def remove_leaves(T):
    for k in T.keys():
        if T[k] == {}: 
            del T[k]
        else:
            remove_leaves(T[k])

def capitalize_leaves(T):
    for k in T.keys():
        if T[k] == {}:
            T[k.upper()] = T.pop(k)
        else:
            capitalize_leaves(T[k])