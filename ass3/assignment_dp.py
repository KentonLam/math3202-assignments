from typing import Tuple

from functools import lru_cache 
from itertools import product
from math import ceil

from sys import exit 
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

Actions1 = range(MAX_SOLD)

def V1(f: int, remaining: int) -> Tuple[int, str]:
    assert remaining >= 0

    if f > MAX_INDEX or remaining == 0:
        return (0, ())
    
    assert 0 <= f <= MAX_INDEX

    running_max = 0 
    running_action = None
    for a in Actions1:
        if a > remaining: break
        x, action = V1(f+1, remaining-a)
        x += Profits[f]*Expected[f][a]
        if x > running_max:
            running_action = (a, ) + action
            running_max = x
    return (running_max, running_action)

def comm_1():
    print(V1(0, 9))


# COMMUNICATION 2
D = list(range(1, 7)) # 1, ..., 6
DemandProbs = [
    [0.13, 0.24, 0.29, 0.23, 0.11, 0],
    [0, 0.14, 0.22, 0.31, 0.24, 0.09],
    [0, 0.1, 0.22, 0.32, 0.23, 0.13]
]
StoreCost = 30
Actions2 = (0, 1, 2, 3, 4, 5, 6)

@lru_cache(maxsize=None)
def V2_fridge(f: int, t: int, s: int):
    if t >= 4:
        # return (-Profits[f]*s, ())
        return (0, 'done')
    
    r_max = 0 
    r_action = None
    for a in Actions2:
        # cost of storing old Fridges + newly bought Fridges
        e_profit = -StoreCost*(s+a) 
        for n, p in zip(D, DemandProbs[f]): # for each possible demand
            sold = min(n, s+a) # Fridges sold is limited by how many we have
            v, _ = V2_fridge(f, t+1, s+a - sold)
            e_profit += p * (Profits[f]*sold + v)
        if e_profit > r_max:
            r_max = e_profit 
            r_action = a 
    return (r_max, r_action)

def V2(t, a, e, l):
    m0, a0 = V2_fridge(0, t, a)
    m1, a1 = V2_fridge(1, t, e)
    m2, a2 = V2_fridge(2, t, l)
    return (m0+m1+m2, a0, a1, a2)

def comm_2():
    sol = V2(0, 0, 0, 0)
    print('Solution:', sol)
    print(V2_fridge.cache_info())

    optimal = (4, 5, 5)

    # verifying optimal strategy for all combinations of input values 
    # to V_2
    for f in F:
        for a in Actions2:
            for t in (0, 1, 2, 3):
                if V2_fridge(f, t, a)[1] != max(optimal[f]-a, 0):
                    print(f'WARNING: fridge {f} with state {a} fails strategy:', V2_fridge(f, t, a))
        print(f'{Fridges[f]}, optimal={optimal[f]}. ', end='')
    print()

# COMMUNICATION 3 
FridgesPerTruck = 7 
TruckCost = 150 
MaxTrucks = 2
MaxStore = 8

# all possible buying options. each fridge can be bought 0 to 14 times
# and the sum of all fridges bought must not exceed 14.
ActionPerms = tuple(
    (i, j, k) 
    for i, j, k in product(range(MaxTrucks*FridgesPerTruck+1), repeat=3)
    if i+j+k <= MaxTrucks*FridgesPerTruck
)

# combines actions with their cost. an action is how many fridges to buy and
# the cost considers the cost of delivering and storing the newly bought fridges.
ActionsWithCosts = tuple(
    (action, -StoreCost*sum(action) - TruckCost*ceil(sum(action)/FridgesPerTruck))
    for action in ActionPerms
)

# all possible permutations of demands and the probability of each. 
# each fridge can be bought 1-7 times (6 options).
DemandsWithProbs = tuple(
    ( (i, j, k), p0*p1*p2 )
    for (i, p0), (j, p1), (k, p2) in product(*[zip(D, DemandProbs[f]) for f in F])
    if p0 and p1 and p2
    # don't add permutations with probability 0 to the list.
)

@lru_cache(maxsize=None)
def capped_demand_probs(c0, c1, c2):
    out = {}
    for (d1, d2, d3), p in DemandsWithProbs:
        key = (min(d1, c0), min(d2, c1), min(d3, c2))
        # after computing the minimum, this permutation may overlap with 
        # a previous permutation. if that happens, collapse and sum their 
        # probabilities for more speed.
        if key not in out:
            out[key] = p 
        else:
            out[key] += p
    return list(out.items())

@lru_cache(maxsize=None)
def compute_profits(d0, d1, d2):
    return Profits[0]*d0 + Profits[1]*d1 + Profits[2]*d2

@lru_cache(maxsize=None)
def V3(t, s0, s1, s2):
    if t == 4:
        return (0, 'done')
    return max(
        # sN is the number of fridge N currently stored.
        # aN is the number of fridge N bought (part of action).
        # dN is the number of fridge N in demand.

        # upfront cost of storing existing fridges as well as newly bought fridges.
        # action_cost contains cost of transporting and storing new fridges.
        (-(s0+s1+s2)*StoreCost + action_cost
        + sum(  # for each demand scenario, compute the profit of that 
                # scenario, weighted by the probability of it occuring.
            p * (compute_profits(d0, d1, d2)
                + V3(t+1, s0+a0-d0, s1+a1-d1, s2+a2-d2)[0])
            for (d0, d1, d2), p in capped_demand_probs(s0+a0, s1+a1, s2+a2)
            # capped_demand_probs() caps dN to the amount we currently have
        ), a0, a1, a2)
        for (a0, a1, a2), action_cost in ActionsWithCosts
        # ensure currently held fridges never exceed 8
        if s0+a0 <= MaxStore and s1+a1 <= MaxStore and s2+a2 <= MaxStore
    )


def comm_3():
    PARAMETERS = (0, 0, 0, 0)

    trim = lambda s: str(s)[:40] + (str(s)[40:] and '...')
    print_trim = lambda label, obj: print(label, f'({len(obj)}):', trim(obj))

    print('Model details:')
    print_trim('  Profits', Profits)
    print_trim('  Demands', D)
    print_trim('  Demand probabilities', DemandProbs)
    print_trim('  Action space', ActionPerms)
    print_trim('  Stochastic event space', DemandsWithProbs)
    print('  Stochastic probability sum:', sum(x[1] for x in DemandsWithProbs))
    start = datetime.now()
    print()
    print('Algorithm start:', start)
    print('  parameters:', PARAMETERS)
    sol = V3(*PARAMETERS)
    end = datetime.now()
    print('  caches:')
    print('    V3', V3.cache_info())
    print('    demand_probs', capped_demand_probs.cache_info())
    print('    profits', compute_profits.cache_info())
    print('Algorithm finish:', end)
    print('Time taken:', end-start)
    print() 
    print('SOLUTION:')
    print(f'V{PARAMETERS} = {sol}')

    # for a in range(6):
    #     for e in range(7):
    #         for l in range(7):
    #             ba, be, bl = V3(1, a, e, l)[1:]
    #             print(a, e, l, ba, be, bl, a+ba, e+be, l+bl)

def main():
    comms = (1, 2, 3)
    for c in comms:
        print('## Communication', c)
        if f'comm_{c}' in globals():
            print('```')
            globals()[f'comm_{c}']() # execute the function for each comm
            print('```')
        else:
            print('**Not found**')
        print()

if __name__ == "__main__":
    main()