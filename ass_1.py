import gurobipy as g 

def assignment_1(): 
    model = g.Model('WonderMarket Model 1')

    # set of store numbers
    S = range(10)
    # set of distribution centre numbers
    D = range(3)

    # matrix of costs of transporting 1 truckload from d to s
    # indexed as C[d][s]
    C = [
        [1828, 1058, 2014, 2134, 1952, 2677, 2548, 2292, 2704, 1153, ],
        [2271, 1746, 2919, 1982, 2704, 2577, 2063, 2807, 2924, 1736, ],
        [807, 1679, 1779, 1428, 1456, 1273, 2160, 559, 1014, 1514, ],
    ]

    # vector of required truckloads at each store.
    R = [18, 7, 21, 15, 17, 10, 6, 8, 7, 7]
    
    # matrix of truckloads from each DC to each store.
    # indexed as X[d][s]
    X = [[model.addVar(name=f'DC{d} to S{s}') for s in S] for d in D]
    
    # adds constraints
    for s in S:
        # required truckloads at each store.
        model.addConstr(g.quicksum(X[d][s] for d in D) >= R[s])
    
    # minimise total cost of transport.
    model.setObjective(
        g.quicksum(g.quicksum(C[d][s]*X[d][s] for d in D) for s in S),
        g.GRB.MINIMIZE
    )

    model.optimize()

    for s in S:
        for d in D:
            v = X[d][s]
            # print all non-zero variables.
            if v.x:
                print(v.varName, v.x)

if __name__ == "__main__":
    assignment_1()