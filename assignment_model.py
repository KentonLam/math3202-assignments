from gurobipy import *

def table(row_format, rows):
    s = ''
    for r in rows:
        s += row_format.format(*r) + '\n'
    return s

def assignment(comm: int): 
    model = Model('WonderMarket Model')
    
    # set of stores
    S = [f'S{i}' for i in range(10)]
    # set of distribution centres
    D = [f'DC{i}' for i in range(3)]

    # matrix of costs of transporting 1 truckload from d to s
    # indexed as C[d][s]
    C = [
        [1828, 1058, 2014, 2134, 1952, 2677, 2548, 2292, 2704, 1153, ],
        [2271, 1746, 2919, 1982, 2704, 2577, 2063, 2807, 2924, 1736, ],
        [807, 1679, 1779, 1428, 1456, 1273, 2160, 559, 1014, 1514, ],
    ]

    # maximum capacity at each distribution centre.
    M = dict(zip(D, [72, 76, 40]))

    # required truckloads at each store.
    R = dict(zip(S, [18, 7, 21, 15, 17, 10, 6, 8, 7, 7]))

    # set of distribution centres on the north-side.
    N = ['DC0', 'DC2']
    
    # matrix of truckloads from each DC to each store.
    # indexed as X[d][s]
    X = model.addVars(D, S, obj=C, name='X')

    # adds constraints.
    constrs = {}
    # comm 1: required truckloads at each store.
    constrs['demand'] = model.addConstrs(X.sum('*', s) >= R[s] for s in S)

    # comm 2: maximum capacity at each distribution centre.
    if comm >= 2:
        constrs['capacity'] = model.addConstrs(X.sum(d, '*') <= M[d] for d in D)

    if comm >= 3:
        # together, DC0 and DC2 can only provide 85 truckloads
        # per week.
        constrs['northside'] = model.addConstr(quicksum(X.sum(d, '*') for d in N) <= 85)
    
    # minimise total cost of transport.
    model.modelSense = GRB.MINIMIZE

    model.optimize()

    print()
    print(f'Optimised for communication {comm}.')
    print('Objective value:', model.objVal)
    print()
    rows = []
    for s in S:
        for d in D:
            v = X[d, s]
            # print all non-zero variables.
            if v.x:
                print(f'{v.varName} = {v.x}')
                rows.append((v.varName, v.RC, v.obj, v.SAObjLow, v.SAObjUp))

    import gurobi_pprint
    gurobi_pprint.print_variable_analysis(X)
    print()
    gurobi_pprint.print_constr_analysis(constrs)
        

if __name__ == "__main__":
    assignment(3)