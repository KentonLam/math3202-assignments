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
        constrs['northside'] = model.addConstr(X.sum('DC0', '*') + X.sum('DC2', '*') <= 85)
    
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

    print()
    print('Objective Analysis')
    #      X[DC2,S0]:  0.0 |   807.0 | -1304.0   967.0
    print('var name    rc      obj      objLow  objHigh')
    print(table('{}: {:4} | {:7} | {:7} {:7}', rows))

    print()
    print('Constraint Analysis')
    for name, c_dict in constrs.items():
        print('===', name, '===')
        print('constr       slack  RHSLow RHSUp')
        if not isinstance(c_dict, dict):
            c_dict = {'': c_dict}
        rows = []
        for v, c in c_dict.items():
            rows.append((f'{v} {c.sense} {c.rhs}', c.slack, c.SARHSLow, c.SARHSUp))
        print(table('{:<10} | {:4} | {:>4}  {}', rows))
        

if __name__ == "__main__":
    assignment(3)