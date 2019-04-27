"""
MATH3202 Assignment 1 -- Linear Programming
Kenton Lam

Due 29/03/2019 12:00pm
"""

from gurobipy import *
from collections import defaultdict, namedtuple
from collections.abc import Mapping

from itertools import product

def get_elem(matrix, indexes):
    """
    Given indexes = [a, b, c, ...], returns 
    matrix[a][b][c][...].
    """
    obj = matrix
    for ind in indexes:
        obj = obj[ind]
    return obj

def make_tupledict(matrix, *names):
    """Converts a matrix (in list of lists form) to a dictionary with tuples
    as keys.
    
    Arguments:
        matrix {List[List[...]]} -- matrix as list of lists (row-major order).
        names {List[List[Any]]} -- row/column names, in the order they are 
        in the list format.
    
    Returns:
        Dict[Tuple[...], int|float] -- dictionary indexed by name tuples.
    """
    d = tupledict()
    ranges = [range(len(x)) for x in names]
    for r in product(*ranges):
        key = tuple(name[i] for name, i in zip(names, r))
        if len(key) == 1:
            key = key[0]
        d[key] = get_elem(matrix, r)
    return d

### SETS ###

# set of stores
Stores = [f'S{i}' for i in range(10)]
# set of distribution centres
DCs = [f'DC{i}' for i in range(3)]

# comm 4: surge scenario names. S has already been used for stores, so we use U here.
Surges = [f'U{i}' for i in range(5)]

### DATA ###

# == comm 1 ==
# matrix of cost per truckload of transporting from d to s.
# indexed as C[d,s]
Costs = make_tupledict([
    [1828, 1058, 2014, 2134, 1952, 2677, 2548, 2292, 2704, 1153, ],
    [2271, 1746, 2919, 1982, 2704, 2577, 2063, 2807, 2924, 1736, ],
    [807, 1679, 1779, 1428, 1456, 1273, 2160, 559, 1014, 1514, ],
], DCs, Stores)
# required truckloads at each store.
Demands = dict(zip(Stores, [18, 7, 21, 15, 17, 10, 6, 8, 7, 7]))

# == comm 2 ==
# maximum capacity at each distribution centre.
Capacities = dict(zip(DCs, [72, 76, 40]))

# == comm 3 ==
# set of distribution centres on the north-side.
Northside = ['DC0', 'DC2']
# maximum capacity of northside DCs.
NorthsideMax = 88

# == comm 4 ==
# surge demand scenarios for each store.
SurgeDemands = make_tupledict([
    # ['S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9'],
    [18,7,21,29,17,10,6,8,7,7],
    [18,7,21,15,17,10,6,31,7,7],
    [19,7,21,15,17,10,6,8,7,7],
    [18,7,21,15,17,10,6,8,30,7],
    [18,7,21,15,21,54,6,8,7,7]
], Surges, Stores)
# for each surge and store, this is the ratio of surge demand over normal 
# demand. for example: normal demand = 2, surge demand = 3 results in 
# SurgeMultipliers[u, s] = 3/2 = 1.5.
SurgeMultipliers = {
    (u, s): SurgeDemands[u, s] / Demands[s] 
    for s in Stores for u in Surges
}

# == comm 5 ==
# each store is supplied by only one DC.

# == comm 6, 7 == 
NewDCs = [f'DC{i+3}' for i in range(4)]
NewCosts = make_tupledict([
    [1312,722,1251,1929,1125,2264,2565,1718,2161,996],
    [1748,1663,670,2603,814,2606,3299,1890,2316,1862],
    [1273,1776,2489,668,2062,841,1353,1370,1275,1532],
    [2475,2663,3584,1653,3260,1899,936,2648,2434,2441],
], NewDCs, Stores)
NewCapacities = make_tupledict([74, 21, 29, 68], NewDCs)

# == comm 8 ==
FTCost = 4500 
PTCost = 2750
FTCapacity = 9 
PTCapacity = 5

# == comm 9 == 
SurgeWeeks = make_tupledict([5, 5, 6, 2, 5], Surges)
NormalWeeks = 52 - SurgeWeeks.sum('*').getValue()
assert NormalWeeks == 29
CasualCost = 2951


def run_assignment_model(comm: int):
    global Surges, SurgeDemands, SurgeMultipliers
    assert 1 <= comm <= 9, "Invalid communication number."
    if comm < 4:
        # for backwards compatibility with previous communications where
        # there were no surges.
        Surges = []
        SurgeDemands = None
        SurgeMultipliers = None

    print_ticks = lambda: print('```')

    print('Communication', comm)
    print('='*78)
    print()

    print_ticks()
    # the gurobi model.
    model = Model('WonderMarket Model')

    # comm 6: we have 4 candidate DC sites. add their data to the existing DCs.
    if comm >= 6:
        OldDCs = list(DCs) # store a copy of existing DCs for constraints.
        DCs.extend(NewDCs) # append new DC sites to DCs for capacity constraints.

        # B[d], where d is a new DC, denotes whether a DC is built at d.
        B = model.addVars(DCs, name='Build', vtype=GRB.BINARY)

        Costs.update(NewCosts)
        for new_dc in DCs:
            # DC could be from old or new DCs.
            caps = NewCapacities if new_dc in NewCapacities else Capacities
            # each new DC's capacity is 0 unless it is built.
            Capacities[new_dc] = B[new_dc]*caps[new_dc]

    # comm 8: each DC now has labour costs.
    if comm >= 8: 
        PTScaledCost = PTCost
        FTScaledCost = FTCost
        # in comm 9, these are employed year-round.
        if comm >= 9:
            PTScaledCost *= 52 
            FTScaledCost *= 52
        P = model.addVars(DCs, name='PT', obj=PTScaledCost, vtype=GRB.INTEGER)
        F = model.addVars(DCs, name='FT', obj=FTScaledCost, vtype=GRB.INTEGER)
        
        # total capacity handled by full-time and part-time teams at each DC.
        FTPTSum = tupledict({ d: FTCapacity*F[d]+PTCapacity*P[d] for d in DCs })
        # this doesn't need to be a variable because it is directly derived 
        # from other variables and is not used in the objective function.

    # comm 9: we need to consider labour during surge scenarios using casual 
    # workers.
    if comm >= 9:
        CasualCosts = {} 
        for surge in Surges:
            for dc in DCs:
            # how much it will cost to employ 1 casual worker for the 
            # duration of a particular surge, at each DC.
                CasualCosts[surge, dc] = SurgeWeeks[surge]*CasualCost
        C = model.addVars(Surges, DCs, name='CA', obj=CasualCosts, vtype=GRB.INTEGER)

    # A[d,s] is a binary variable of whether store s receives deliveries 
    # from DC d. 
    if comm >= 5:
        A = model.addVars(DCs, Stores, name='A', vtype=GRB.BINARY)

    # matrix of truckloads from each DC to each store during NORMAL DEMAND.
    # indexed as X[d,s]. obj=Costs defines the objective coefficient
    # of these variables.
    NormalTCosts = Costs 
    if comm >= 9: # comm 9: consider yearly cost.
        # per truckload cost multiplied by number of normal weeks.
        NormalTCosts = { k: NormalWeeks*v for k, v in Costs.items() }
    X = model.addVars(DCs, Stores, obj=NormalTCosts, name='X')
    # comm 5: binary variables dicate store assignments.
    if comm >= 5:
        model.addConstrs(X[d,s] == A[d,s]*Demands[s] for s in Stores for d in DCs)

    # matrix of truckloads from each DC to each store during each surge.
    # to handle surges, we consider the required demand at each store using
    # a multiplier of its regular demand. this stores the precise amount
    # of truckloads sent from d to s during surge u.
    SurgeTCosts = 0
    if comm >= 9:
        # before comm 9, we ignore surge costs. in comm 9, we need to consider 
        # the cost of each surge which is affected by how long it runs for.
        SurgeTCosts = { (d,s,u): Costs[d,s]*SurgeWeeks[u] 
            for d, s, u in product(DCs, Stores, Surges) }
    Y = model.addVars(DCs, Stores, Surges, name='Y', obj=SurgeTCosts)

    # links X and Y variables. this ensures proportions are kept.
    model.addConstrs(Y[d,s,u] == X[d, s] * SurgeMultipliers[u, s] 
        for s in Stores for d in DCs for u in Surges)

    # dictionary to store our constraints.
    constrs = {}

    # required truckloads for normal demand at each store.
    # constrained using Y variables.
    constrs['n_demand'] = model.addConstrs(
        X.sum('*', s) >= Demands[s] for s in Stores
    )

    if comm >= 2: # comm 2: max capacity at DC for normal demand.
        constrs['n_capacity'] = model.addConstrs(
            X.sum(d, '*') <= Capacities[d] for d in DCs)

    if comm >= 3 and comm < 5: # comm 3: northside capacity limit for normal demand.
        constrs['n_northside'] = model.addConstr(
            quicksum(X.sum(d, '*') for d in Northside) <= NorthsideMax)

    if comm >= 6 and comm < 7: # comm 6: only one new DC can be built.
        constrs['new_dc'] = model.addConstr(B.sum(NewDCs) <= 1)
        # ensure all existing DCs are not destroyed.
        constrs['old_dcs'] = model.addConstr(B.sum(OldDCs) == len(OldDCs))
    
    if comm >= 7: # comm 7: total number of DCs is at most 4 (1 or 2 new)
        constrs['new_dc'] = model.addConstr(B.sum(NewDCs) <= 2)
        constrs['all_dcs'] = model.addConstr(B.sum('*') == 4)

    if comm >= 8: # comm 8: enough labour for truckloads needed.
        # remember that X is normal demand.
        constrs['labour'] = model.addConstrs(X.sum(d, '*') <= FTPTSum[d] for d in DCs)

    # assume only one surge occurs at a time. handle independently.
    for u in Surges:
        constrs[f'{u}'] = surge_constrs = {}

        # comm 1 or 4: required truckloads at each store during each surge.
        surge_constrs['s_demand'] = model.addConstrs(
            Y.sum('*', s, u) >= SurgeDemands[u, s] for s in Stores if SurgeDemands[u,s] != Demands[s])

        # comm 2: maximum capacity at each distribution centre.
        if comm >= 2:
            surge_constrs['s_capacity'] = model.addConstrs(
                Y.sum(d, '*', u) <= Capacities[d] for d in DCs)

        # comm 3: capacity limit on DCs on north side.
        # together, DC0 and DC2 can only provide 85 truckloads
        # per week.
        if comm >= 3 and comm < 5:
            surge_constrs['s_northside'] = model.addConstr(
                quicksum(Y.sum(d, '*', u) for d in Northside) <= NorthsideMax)

        # comm 9: surge labour costs. 
        if comm >= 9:
            surge_constrs['s_labour'] = model.addConstrs(
                Y.sum(d, '*', u) <= FTPTSum[d] + C[u,d] for d in DCs
            )
        
    # minimise total cost of transport. objective function set using obj= above.
    model.modelSense = GRB.MINIMIZE
    model.optimize()
    print_ticks()
    print()
    print('## -- GUROBI OUTPUT -- ##')
    print('###', model.objVal)
    print_ticks()
    print(f'Optimised for communication {comm}.')
    if model.status == GRB.OPTIMAL:
        print('Objective value:', model.objVal)
        if comm >= 9:
            print('Weekly average:', model.objVal / 52)
    elif model.status == GRB.INFEASIBLE:
        print('INFEASIBLE MODEL.')
    else:
        print(f'Optimisation failed (status {model.status}).')
    print_ticks()
    print()
    print()
    # group by surge, then store, then DC.
    x_ = {(d, s): X[d,s] for s in Stores for d in DCs}
    y_ = {(d,s,u): Y[d,s,u] for u in Surges for s in Stores for d in DCs}

    print()
    print()
    print('## == ANALYSIS NON-ZERO == ##')
    print('(variables not printed are 0)')
    # print_variable_analysis(x_, True)
    print()
    if comm >= 5:
        print_ticks()
        print_variable_analysis(A, 1)
        print_ticks()
        print()
    if comm >= 6:
        print_ticks()
        print_variable_analysis(B, 1)
        print_ticks()
        print()
    if comm >= 8:
        print_ticks()
        print_variable_analysis(P, 1)
        print_ticks()
        print()
        print_ticks()
        print_variable_analysis(F, 1)
        print_ticks()
        print()
    if comm >= 9:
        print_ticks()
        print_variable_analysis(C, 1)
        print_ticks()
        print()
    print()
    print_ticks()
    print_variable_analysis(x_, True)
    print_ticks()
    print()
    if comm >= 9:
        print_ticks()
        print_variable_analysis(y_, 1)
        print_ticks()
    print()
    # print_variable_analysis(Z, True)
    print()
    
    print('## == CONSTRAINTS == ##')
    print()
    print_ticks()
    print_constr_analysis(constrs)
    print_ticks()
    
    print()
    print()
    print('## == NORMAL DEMAND ANALYSIS == ##')
    print() 
    print_ticks()
    print('\n'.join([f'X[{d},{s}] = {X[d,s].x}' for s in Stores for d in DCs if X[d,s].x]))
    print('Store sums:', {s: X.sum('*', s).getValue() for s in Stores})
    print('DC sums:', {d: X.sum(d, '*').getValue() for d in DCs})
    if comm >= 8:
        print('FTPT sums:', {k: v.getValue() for k, v in FTPTSum.items() })
    if comm >= 9:
        t_cost = quicksum(X[d,s]*NormalTCosts[d,s] 
            for d,s in X)
        l_cost = quicksum( (F[d]*FTScaledCost + P[d]*PTScaledCost)
            for d in DCs) 
        print('Cost (yearly, with labour):', (t_cost+l_cost).getValue())
        print('  Transport:', t_cost.getValue())
        print('  FT/PT labour:', l_cost.getValue())
    print_ticks()

    print()
    print('## == SURGE ANALYSIS == ##')
    print()
    print('Surge multipliers')
    print_ticks()
    print(SurgeMultipliers)
    print_ticks()
    # prints truckloads for each store during each surge.
    for u in Surges:
        print()
        print('### Surge', u)
        print_ticks()
        print('\n'.join([f'Y[{d},{s},{u}] = {Y[d,s,u].x}' for s in Stores for d in DCs if Y[d,s,u].x]))
        print('Store sums:', {s: Y.sum('*', s, u).getValue() for s in Stores})
        print('DC sums:', {d: Y.sum(d, '*', u).getValue() for d in DCs})
        if comm >= 9:
            print('Casuals:', {d: float(C[u,d].x) for d in DCs if C[u,d].x })

        w_cost = 0
        for d, s in product(DCs, Stores):
            w_cost += Y[d,s,u]*Costs[d,s]
        print('Cost (weekly, no labour):', w_cost.getValue())
        if comm >= 9:
            t_cost = quicksum(Y[d,s,u2]*SurgeTCosts[d,s,u] 
                for d,s,u2 in Y if u2 == u)
            l_cost = quicksum(C[u,d] * CasualCosts[u,d] 
                for d in DCs)
            print('Cost (yearly, with labour):', (t_cost+l_cost).getValue())
            print('  Transport:', t_cost.getValue())
            print('  Casual labour:', l_cost.getValue())
            print('Weekly:', ((t_cost+l_cost)/SurgeWeeks[u]).getValue())
            print('Surge duration:', SurgeWeeks[u])
        print_ticks()

    print()
    print('## == STORE ASSIGNMENTS == ##')
    print_ticks()
    print_assignments(X)
    print_ticks()

    print()
    print_ticks()
    print('Store &', ' & '.join(DCs), r'\\')
    for s in Stores:
        # proportions
        p = [float(X[d,s].x/Demands[s]) for d in DCs]
        p = [str(round(a*100, 2)).rstrip('0').rstrip('.')+'\\%' if a else '' for a in p]
        print(' & '.join([s] + p), r'\\')
    print_ticks()

    print()
    print('This was communication', comm, 'with value', model.objVal)
    
        
def print_assignments(Y):
    """Prints a neatly formatted proportion table."""
    num = int(len(Y)/len(Stores))
    print('Store Assignments')
    print('store |' + ''.join(f'    DC{i}' for i in range(num)))
    fmt = ' {:>6}'*num
    for s in Stores:
        fractions = [Y[d,s].x/Demands[s] for d in DCs]
        # if the variable is 0, don't print anything. makes table easier to read.
        fractions = map(lambda x: round(x, 4) if x else '', fractions)
        print(('{:>5} |'+fmt).format(s, *fractions))

def table(fmt, rows):
    """Formats a table with the given row format."""
    s = ''
    for r in rows:
        s += fmt.format(*r)
    return s

# entry point of application.
def main():
    from sys import argv
    if len(argv) < 2:
        comm = 9
    else:
        comm = int(argv[1])
    run_assignment_model(comm)


# helper functions to print constraint and variable analysis.

#region gurobi_pprint

TableSpec = namedtuple('TableSpec', 'title header format generator empty')

r = lambda i: round(i, 4) if i else '0'
row_generator = {
    'constraints': TableSpec(
        'Constraint Analysis', 
        ('constr', '', 'rhs', 'slack', 'pi', 'rhs low', 'rhs high'),
        '  {:>1} {:>5} | {:>6} {:>6} | {:>7} {:>7}', 
        lambda n, c: (n, c.sense, r(c.rhs), r(c.slack), '-', '-', '-'),
        lambda t: t[2] in (0, '0')
    ),
    'variables': TableSpec(
        'Variable Analysis', 
        ('variable', 'x', 'coeff', 'rc', 'obj low', 'obj high'),
        '  = {:>5} * {:>6} | {:>6} | {:>7} {:>7}', 
        lambda n, c: (c.varName, r(c.x), r(c.obj), '-', '-', '-'),
        lambda t: t[1] in (0, '0')
    )
}

def _dict_to_rows(constrs_list, generator, prefix=''):
    if not isinstance(constrs_list, dict):
        return [generator(prefix, constrs_list)]
    if prefix:
        p = prefix + ' '
    else:
        p = ''
    out = []
    for k, v in constrs_list.items():
        rows = _dict_to_rows(v, generator, p+str(k))
        out.extend(rows)
    return out

def _print_analysis(constr_dict, mode, drop_empty=False):
    rows = _dict_to_rows(constr_dict, row_generator[mode].generator)
    max_lens = []
    for i in range(len(rows[0])):
        this_max_len = max(map(lambda a: len(str(a)), (r[i] for r in rows)))
        if i > 0:
            this_max_len = min(this_max_len, 10)
        max_lens.append(this_max_len)
    
    # f_str_list = list(map(lambda l: f'{{:>{l}}}', max_lens))
    # f_str_list[0] = f'{{:>{max_lens[0]}}}'
    # f_str_list[1] = '{:2}'
    
    f_str = f'{{:>{max_lens[0]}}}' + row_generator[mode].format

    print(row_generator[mode].title)
    print(f_str.format(*row_generator[mode].header))
    for r in rows:
        if drop_empty and row_generator[mode].empty(r):
            continue
        # print(f_str)
        # print(r)
        print(f_str.format(*r))

def print_constr_analysis(constrs, drop_zero=False):
    """Prints constraint sensitivity analysis in a table format."""
    return _print_analysis(constrs, 'constraints', drop_zero)

def print_variable_analysis(variables, drop_zero=False): 
    """Prints variable sensitivity analysis in a table format."""
    return _print_analysis(variables, 'variables', drop_zero)

#endregion

if __name__ == "__main__":
    main()