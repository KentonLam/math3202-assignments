from gurobipy import *
from collections import defaultdict, namedtuple

def table(row_format, rows):
    s = ''
    for r in rows:
        s += row_format.format(*r) + '\n'
    return s

def make_tupledict(matrix, rows, cols):
    d = tupledict()
    for r, row in enumerate(matrix):
        for c, item in enumerate(row):
            d[rows[r], cols[c]] = item
    return d

### DATA ###

# set of stores
Stores = [f'S{i}' for i in range(10)]
# set of distribution centres
DCs = [f'DC{i}' for i in range(3)]

# == comm 1 ==
# matrix of cost per truckload of transporting from d to s.
# indexed as C[d][s]
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
NorthsideMax = 85

# == comm 4 ==
# surge scenario names. S has already been used for stores, so we use U here.
Surges = [f'U{i}' for i in range(5)]
# surge demand scenarios for each store.
SurgeDemands = make_tupledict([
    # ['S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9'],
    [18, 7, 21, 29, 17, 10, 6, 8, 7, 7], # Scenario 1
    [18, 7, 21, 15, 17, 10, 6, 31, 7, 7],
    [19, 7, 21, 15, 17, 10, 6, 8, 7, 7],
    [18, 7, 21, 15, 17, 10, 6, 8, 30, 7],
    [18, 7, 21, 15, 18, 54, 6, 8, 7, 7],
], Surges, Stores)
# for each surge and store, this is the ratio of surge demand over normal 
# demand. for example: normal demand = 2, surge demand = 3 results in 
# SurgeMultipliers[u, s] = 3/2 = 1.5.
SurgeMultipliers = tupledict(
    {(u, s): SurgeDemands[u, s]/Demands[s] for s in Stores for u in Surges}
)

def run_assignment_model(comm: int):
    global Surges, SurgeDemands, SurgeMultipliers
    assert 1 <= comm <= 4, "Invalid communication number."
    if comm < 4:
        # for backwards compatibility with previous communications.
        Surges = ['none']
        SurgeDemands = {('none', s): Demands[s] for s in Stores}
        SurgeMultipliers = defaultdict(lambda: 1)

    # the gurobi model.
    model = Model('WonderMarket Model')

    # matrix of truckloads from each DC to each store during each surge.
    # indexed as X[d,s,u].
    X = model.addVars(DCs, Stores, Surges, name='X')

    # fraction of each store's REGULAR demand to be fulfilled by each 
    # distribution centre. see constrs['fractions'] below.
    # indexed as Y[d,s].
    Y = model.addVars(DCs, Stores, name='Y')

    # total transport cost during each surge scenario.
    Z = model.addVars(Surges, obj=1, name='Z')

    # dictionary to store our constraints.
    constrs = {}

    # link X and Y. 
    # for all s in Stores, the sum of Y[d,s] across d in DCs is always 1.
    # this is because Y is proportions of each store's total normal demand.
    # to handle surges, we consider the required demand at each store using
    # a multiplier of its regular demand. X[d,s,u] stores the precise amount
    # of product from d to s during surge u.
    constrs['fractions'] = model.addConstrs(
        X[d, s, u] / Demands[s] == Y[d, s] * SurgeMultipliers[u, s] 
        for s in Stores for d in DCs for u in Surges
    )

    # to make calculating the objective easier, we compute some totals here,
    # using equality.
    constrs['totals'] = model.addConstrs(
        Z[u] == quicksum(X.sum(d, s, u) * Costs[d, s] for d in DCs for s in Stores)
        for u in Surges
    )

    # assume only one surge occurs at a time. handle independently.
    for u in Surges:
        constrs[f'{u}'] = surge_constrs = {}

        # comm 1 or 4: required truckloads at each store during each surge.
        surge_constrs['s_demand'] = model.addConstrs(
            X.sum('*', s, u) >= SurgeDemands[u, s] for s in Stores)

        if comm >= 2:
            # comm 2: maximum capacity at each distribution centre.
            surge_constrs['capacity'] = model.addConstrs(
                X.sum(d, '*', u) <= Capacities[d] for d in DCs)

        if comm >= 3:
            # comm 3: capacity limit on DCs on north side.
            # together, DC0 and DC2 can only provide 85 truckloads
            # per week.
            surge_constrs['northside'] = model.addConstr(
                quicksum(X.sum(d, '*', u) for d in Northside) <= NorthsideMax)
        
    # minimise total cost of transport.
    model.modelSense = GRB.MINIMIZE
    model.optimize()

    print()
    print(f'Optimised for communication {comm}.')
    if model.status == GRB.OPTIMAL:
        print('Objective value:', model.objVal)
    elif model.status == GRB.INFEASIBLE:
        print('INFEASIBLE MODEL.')
    else:
        print(f'Optimisation failed (status {model.status}).')
    print()
    print()
    # group by surge, then store, then DC.
    x_ = {(d,s,u): X[d,s,u] for u in Surges for s in Stores for d in DCs}
    y_ = {(d, s): Y[d,s] for s in Stores for d in DCs}

    print_variable_analysis(x_)
    print_variable_analysis(y_)
    print_variable_analysis(Z)

    print_constr_analysis(constrs)
    
    print()
    print_assignments(Y)
        
def print_assignments(Y):
    print('Store Assignments')
    print('store |    DC0    DC1    DC2')
    for s in Stores:
        fractions = [Y[d,s].x for d in DCs]
        fractions = map(lambda x: round(x, 4) if x else '', fractions)
        print('{:>5} | {:>6} {:>6} {:>6}'.format(s, *fractions))

# entry point of application.
def main():
    from sys import argv
    if len(argv) < 2:
        comm = 4
    else:
        comm = int(argv[1])
    run_assignment_model(comm)


# helper functions to print constraint and variable analysis.

#region gurobi_pprint
TableSpec = namedtuple('TableSpec', 'title header format generator')

r = lambda i: round(i, 4)
row_generator = {
    'constraints': TableSpec(
        'Constraint Analysis', 
        ('constr', '', 'rhs', 'slack', 'pi', 'rhs low', 'rhs high'),
        '  {:>1} {:>5} | {:>6} {:>6} | {:>7} {:>7}', 
        lambda n, c: (n, c.sense, r(c.rhs), r(c.slack), r(c.pi), r(c.SARHSLow), r(c.SARHSUp))
    ),
    'variables': TableSpec(
        'Variable Analysis', 
        ('variable', 'x', 'coeff', 'rc', 'obj low', 'obj high'),
        '  = {:>5} * {:>6} | {:>6} | {:>7} {:>7}', 
        lambda n, c: (c.varName, r(c.x), r(c.obj), r(c.rc), r(c.SAObjLow), r(c.SAObjUp))),
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

def _print_analysis(constr_dict, mode):
    rows = _dict_to_rows(constr_dict, row_generator[mode].generator)
    max_lens = []
    for i in range(len(rows[0])):
        this_max_len = max(map(lambda a: len(str(a)), (r[i] for r in rows)))
        if i > 0:
            this_max_len = min(this_max_len, 10)
        max_lens.append(this_max_len)
    
    f_str = f'{{:>{max_lens[0]}}}' + row_generator[mode].format

    print(row_generator[mode].title)
    print(f_str.format(*row_generator[mode].header))
    for r in rows:
        print(f_str.format(*r))
    
def print_constr_analysis(constrs):
    return _print_analysis(constrs, 'constraints')

def print_variable_analysis(variables): 
    return _print_analysis(variables, 'variables')
#endregion

if __name__ == "__main__":
    main()