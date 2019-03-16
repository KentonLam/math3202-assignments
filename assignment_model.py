from gurobipy import *

def assignment(comm=2): 
    model = Model('WonderMarket Model 1')

    # set of store numbers
    S = [f'S{i}' for i in range(10)]
    # set of distribution centre numbers
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

    # vector of required truckloads at each store.
    R = dict(zip(S, [18, 7, 21, 15, 17, 10, 6, 8, 7, 7]))
    
    # matrix of truckloads from each DC to each store.
    # indexed as X[d][s]
    X = model.addVars(D, S, obj=C, name='X')

    # adds constraints.
    # comm 1: required truckloads at each store.
    model.addConstrs(X.sum('*', s) >= R[s] for s in S)

    # comm 2: maximum capacity at each distribution centre.
    if comm >= 2:
        model.addConstrs(X.sum(d, '*') <= M[d] for d in D)
    
    # minimise total cost of transport.
    model.modelSense = GRB.MINIMIZE

    model.optimize()

    print()
    print(f'Optimised for communication {comm}.')
    print('Objective value:', model.objVal)
    print()
    for s in S:
        for d in D:
            v = X[d, s]
            # print all non-zero variables.
            if v.x:
                print(f'{v.varName} ', v.x)
        print()

if __name__ == "__main__":
    assignment(2)