from gurobipy import *

def table(row_format, rows):
    s = ''
    for r in rows:
        s += row_format.format(*r) + '\n'
    return s



def run_assignment(comm: int, surge_demands=None): 
    model = Model('WonderMarket Model')

    # set of stores
    Stores = [f'S{i}' for i in range(10)]
    # set of distribution centres
    DCs = [f'DC{i}' for i in range(3)]

    # == comm 1 ==
    # matrix of costs of transporting 1 truckload from d to s
    # indexed as C[d][s]
    Cost = [
        [1828, 1058, 2014, 2134, 1952, 2677, 2548, 2292, 2704, 1153, ],
        [2271, 1746, 2919, 1982, 2704, 2577, 2063, 2807, 2924, 1736, ],
        [807, 1679, 1779, 1428, 1456, 1273, 2160, 559, 1014, 1514, ],
    ]

    # required truckloads at each store.
    Demand = dict(zip(Stores, [18, 7, 21, 15, 17, 10, 6, 8, 7, 7]))

    # == comm 2 ==
    # maximum capacity at each distribution centre.
    Capacity = dict(zip(DCs, [72, 76, 40]))

    # == comm 3 ==
    # set of distribution centres on the north-side.
    Northside = ['DC0', 'DC2']
    # maximum capacity of northside DCs.
    NorthsideMax = 85

    # matrix of truckloads from each DC to each store.
    # indexed as X[d][s]
    X = model.addVars(DCs, Stores, obj=Cost, name='X')

    # adds constraints.
    constrs = {}
    # comm 1: required truckloads at each store.
    constrs['demand'] = model.addConstrs(X.sum('*', s) >= Demand[s] for s in Stores)

    # comm 2: maximum capacity at each distribution centre.
    if comm >= 2:
        constrs['capacity'] = model.addConstrs(X.sum(d, '*') <= Capacity[d] for d in DCs)

    # comm 3: capacity limit on DCs on north side.
    if comm >= 3:
        # together, DC0 and DC2 can only provide 85 truckloads
        # per week.
        constrs['northside'] = model.addConstr(quicksum(X.sum(d, '*') for d in Northside) <= NorthsideMax)
    
    # comm 4: surge demand scenarios.
    if comm >= 4:
        surge_dict = dict(zip(Stores, surge_demands))
        constrs['surge'] = model.addConstrs(
            (X.sum('*', s) >= d for s, d in surge_dict.items()), 
            name=surge_dict)

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
    rows = []
    for s in Stores:
        for d in DCs:
            v = X[d, s]
            # print all non-zero variables.
            if v.x:
                print(f'{v.varName} = {v.x}')
                rows.append((v.varName, v.RC, v.obj, v.SAObjLow, v.SAObjUp))

    import gurobi_pprint
    print()
    gurobi_pprint.print_variable_analysis(X)
    print()
    gurobi_pprint.print_constr_analysis(constrs)
        
def assignment_4():
    print('Starting communication 4 scenarios...')
    print()

    # == comm 4 ==
    # required surge demands at each store.
    Surges = [
        # ['Scenario', 'S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9'],
        [18, 7, 21, 29, 17, 10, 6, 8, 7, 7],
        [18, 7, 21, 15, 17, 10, 6, 31, 7, 7],
        [19, 7, 21, 15, 17, 10, 6, 8, 7, 7],
        [18, 7, 21, 15, 17, 10, 6, 8, 30, 7],
        [18, 7, 21, 15, 18, 54, 6, 8, 7, 7],
    ]

    for i, surge in enumerate(Surges):
        print(f'== SURGE SCENARIO {i} ==')
        run_assignment(4, surge)
        print()
        print()

if __name__ == "__main__":
    assignment_4()