from typing import Tuple

from functools import lru_cache 
from itertools import product
from math import ceil

from datetime import datetime

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

ActionPerms = tuple(
    (i, j, k) 
    for i, j, k in product(range(15), repeat=3)
    if i+j+k <= MaxTrucks*FridgesPerTruck
)

# all possible permutations of demands and the probability of each. 
# each fridge can be bought 1-7 times.
DemandProbPerms = tuple(
    ( (d0+1, d1+1, d2+1), Demands[0][d0]*Demands[1][d1]*Demands[2][d2] )
    for d0, d1, d2 in product(range(6), repeat=3)
    if Demands[0][d0] and Demands[1][d1] and Demands[2][d2]
    # don't add permutations with probability 0 to the list.
)

@lru_cache(maxsize=None)
def capped_demand_probs(c0, c1, c2):
    out = {}
    for (d1, d2, d3), p in DemandProbPerms:
        key = (min(d1, c0), min(d2, c1), min(d3, c2))
        if key not in out:
            out[key] = p 
        else:
            out[key] += p
    return list(out.items())

@lru_cache(maxsize=None)
def V3(t, s0, s1, s2):
    if t == 4:
        return (0, 'done')
    return max(
        # profit
        ((-(s0+s1+s2+a0+a1+a2)*StoreCost - 150*ceil((a0+a1+a2)/FridgesPerTruck)
        + sum(
            p * (Profits[0]*d0 + Profits[1]*d1 + Profits[2]*d2
                + V3(t+1, s0+a0-d0, s1+a1-d1, s2+a2-d2)[0])
            for (d0, d1, d2), p in capped_demand_probs(s0+a0, s1+a1, s2+a2)
        ), a0, a1, a2)
        for a0, a1, a2 in ActionPerms
        if s0+a0 <= 8 and s1+a1 <= 8 and s2+a2 <= 8),
    )


def comm_3():
    PARAMETERS = (0, 0, 0, 0)

    print('Model details:')
    print('  Action space:', len(ActionPerms))
    print('  Stochastic probability sum:', sum(x[1] for x in DemandProbPerms))
    print('  Stochastic event space:', len(DemandProbPerms))
    start = datetime.now()
    print()
    print('Algorithm start:', start)
    print('  initial parameters:', PARAMETERS)
    print('  solution:', V3(*PARAMETERS))
    end = datetime.now()
    print('  V3 cache:', V3.cache_info())
    print('  capped_demand_probs cache:', capped_demand_probs.cache_info())
    print('Algorithm finish:', end)
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