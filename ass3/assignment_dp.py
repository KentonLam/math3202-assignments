from typing import Tuple

from functools import lru_cache 
from itertools import product
from math import ceil

from datetime import datetime

import numpy as np


Fridges = ['Alaska', 'Elsa', 'Lumi']
F = tuple(range(len(Fridges)))

# COMMUNICATION 1
Profits = [140, 147, 198]
Expected = [
    [0, 1, 3.1, 3.6, 3.8],
    [0, 0, 2.5, 4.2, 4.6],
    [0, 0.2, 2.9, 4.1, 4.1]
]

MAX_INDEX = len(Fridges)-1
MAX_SOLD = len(Expected[0])

def solve_1(index: int, remaining: int) -> Tuple[int, str]:
    assert remaining >= 0

    if index > MAX_INDEX or remaining == 0:
        return (0, ())
    
    assert 0 <= index <= MAX_INDEX

    running_max = 0 
    running_action = None
    for i in range(MAX_SOLD):
        if i > remaining: break
        x, action = solve_1(index+1, remaining-i)
        x += Profits[index]*Expected[index][i]
        if x > running_max:
            running_action = (i, ) + action
            running_max = x
    return (running_max, running_action)

def comm_1():
    print(solve_1(0, 8))


# COMMUNICATION 2
Demands = [
    [0.13, 0.24, 0.29, 0.23, 0.11, 0],
    [0, 0.14, 0.22, 0.31, 0.24, 0.09],
    [0, 0.1, 0.22, 0.32, 0.23, 0.13]
]
StoreCost = 30
Actions = (0, 1, 2, 3, 4, 5, 6)

@lru_cache(maxsize=None)
def V2(f: int, t: int, s: int):
    if t == 4:
        # return (-Profits[f]*s, ())
        return (0, 'done')
    
    r_max = 0 
    r_action = None
    for a in Actions:
        # cost of storing old Fridges + newly bought Fridges
        e_profit = -StoreCost*(s+a) 
        for i, p in enumerate(Demands[f]): # for each possible demand
            n = i+1 # n = max number of Fridges sold

            sold = min(n, s+a) # Fridges sold is limited by how many we have
            v, _ = V2(f, t+1, s+a - sold)
            e_profit += p * (Profits[f]*sold + v)
        if e_profit > r_max:
            r_max = e_profit 
            r_action = a 
    return (r_max, r_action)

def comm_2():
    total = 0
    for f in F:
        sol = (V2(f, 0, 0))
        total += sol[0]
        print(Fridges[f], sol)
    print()
    print('Profit:', total)
    print(V2.cache_info())

# COMMUNICATION 3 
FridgesPerTruck = 7 
TruckCost = 150 
MaxTrucks = 2
MaxStorePerType = 8



@lru_cache(maxsize=None)
def get_actions(s):
    t = []
    for a in range(s+1):
        for b in range(s-a+1):
            t.append((a, b, s-a-b))
    return t

def get_all_actions(max_sum):
    t = []
    for s in range(0, max_sum+1):
        t.extend(get_actions(s))
    return t

Permutations = np.stack(get_all_actions(MaxTrucks*FridgesPerTruck))

# all possible permutations of demands. each fridge can be bought 1-6 times.
DemandPerms = np.stack(product(range(1, 7), range(1, 7), range(1, 7)))

ProbPerms = [] 
for demand in DemandPerms:
    p = 1 
    for i, n in enumerate(demand):
        p *= Demands[i][n-1]
    ProbPerms.append(p)
ProbPerms = np.array(ProbPerms)

non_zero = ProbPerms.nonzero() # indices whose probabilities are non-zero
DemandPerms = DemandPerms[non_zero] # filter to non-zero probabilities
ProbPerms = ProbPerms[non_zero]

Profits = np.array(Profits)

@lru_cache(maxsize=None)
def V3(t, s):
    if t == 4:
        return (0, 'done')

    s = np.array(s)

    # print(' '*t, t, s)
    r_max = 0 
    r_action = None
    for action in Permutations: # a is a list of fridges to buy
        current = s + action
        if current.max() > 8:
            continue
        # cost of storing held fridges and truck costs
        e_profit = -current.sum()*StoreCost - 150*ceil(action.sum()/FridgesPerTruck)
        for i, demand in enumerate(DemandPerms): # for each possible demand
            p = ProbPerms[i]

            sold = np.minimum(demand, current) # element-wise minimum
            v, _ = V3(t+1, tuple(current - sold))
            profit = np.dot(Profits, sold)
            e_profit += p * (profit + v)
        if e_profit > r_max:
            r_max = e_profit 
            r_action = action
    return (r_max, r_action)

def comm_3():
    start = datetime.now()
    print('Start:', start)
    print()
    print(V3(0, (0, 0, 0)))
    end = datetime.now()
    print(V3.cache_info())
    print()
    print('End:', end)
    print('Time taken:', end-start)

def main():
    comms = (1, 2, 3)
    for c in comms:
        print('## Communication', c)
        if f'comm_{c}' in globals():
            print('```')
            globals()[f'comm_{c}']() # execute the function comm_"c"
            print('```')
        else:
            print('**Not found**')
        print()

if __name__ == "__main__":
    main()