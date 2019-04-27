Communication 5
==============================================================================

```
Academic license - for non-commercial use only
Optimize a model with 214 rows, 210 columns and 588 nonzeros
Variable types: 180 continuous, 30 integer (30 binary)
Coefficient statistics:
  Matrix range     [1e+00, 2e+01]
  Objective range  [6e+02, 3e+03]
  Bounds range     [1e+00, 1e+00]
  RHS range        [6e+00, 8e+01]
Presolve removed 189 rows and 182 columns
Presolve time: 0.01s
Presolved: 25 rows, 28 columns, 182 nonzeros
Variable types: 0 continuous, 28 integer (28 binary)
Found heuristic solution: objective 236309.00000
Found heuristic solution: objective 228408.00000

Root relaxation: objective 1.962930e+05, 13 iterations, 0.00 seconds

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0 196293.000    0    4 228408.000 196293.000  14.1%     -    0s
H    0     0                    227673.00000 196293.000  13.8%     -    0s
H    0     0                    219619.00000 196293.000  10.6%     -    0s
     0     0 200881.815    0    8 219619.000 200881.815  8.53%     -    0s
H    0     0                    209917.00000 200881.815  4.30%     -    0s
H    0     0                    209182.00000 200881.815  3.97%     -    0s
H    0     0                    206641.00000 200881.815  2.79%     -    0s
     0     0 201346.793    0    8 206641.000 201346.793  2.56%     -    0s
     0     0 202749.000    0    8 206641.000 202749.000  1.88%     -    0s
     0     0 203393.612    0   12 206641.000 203393.612  1.57%     -    0s
H    0     0                    205688.00000 203393.612  1.12%     -    0s
     0     0 203584.833    0   10 205688.000 203584.833  1.02%     -    0s
     0     0 204974.000    0   10 205688.000 204974.000  0.35%     -    0s

Cutting planes:
  Gomory: 1
  Cover: 3
  Clique: 2
  MIR: 1
  StrongCG: 1

Explored 1 nodes (31 simplex iterations) in 0.05 seconds
Thread count was 4 (of 4 available processors)

Solution count 8: 205688 206641 209182 ... 236309

Optimal solution found (tolerance 1.00e-04)
Best objective 2.056880000000e+05, best bound 2.056880000000e+05, gap 0.0000%
```

## -- GUROBI OUTPUT -- ##
### 205688.0
```
Optimised for communication 5.
Objective value: 205688.0
```




## == ANALYSIS NON-ZERO == ##
(variables not printed are 0)

```
Variable Analysis
 variable  =     x *  coeff |     rc | obj low obj high
A[DC0,S0]  =     0 *      0 |      0 |       0       0
A[DC0,S1]  =   1.0 *      0 |      0 |       0       0
A[DC0,S2]  =     0 *      0 |      0 |       0       0
A[DC0,S3]  =     0 *      0 |      0 |       0       0
A[DC0,S4]  =   1.0 *      0 |      0 |       0       0
A[DC0,S5]  =     0 *      0 |      0 |       0       0
A[DC0,S6]  =     0 *      0 |      0 |       0       0
A[DC0,S7]  =   1.0 *      0 |      0 |       0       0
A[DC0,S8]  =   1.0 *      0 |      0 |       0       0
A[DC0,S9]  =   1.0 *      0 |      0 |       0       0
A[DC1,S0]  =     0 *      0 |      0 |       0       0
A[DC1,S1]  =     0 *      0 |      0 |       0       0
A[DC1,S2]  =     0 *      0 |      0 |       0       0
A[DC1,S3]  =   1.0 *      0 |      0 |       0       0
A[DC1,S4]  =     0 *      0 |      0 |       0       0
A[DC1,S5]  =   1.0 *      0 |      0 |       0       0
A[DC1,S6]  =   1.0 *      0 |      0 |       0       0
A[DC1,S7]  =     0 *      0 |      0 |       0       0
A[DC1,S8]  =     0 *      0 |      0 |       0       0
A[DC1,S9]  =     0 *      0 |      0 |       0       0
A[DC2,S0]  =   1.0 *      0 |      0 |       0       0
A[DC2,S1]  =     0 *      0 |      0 |       0       0
A[DC2,S2]  =   1.0 *      0 |      0 |       0       0
A[DC2,S3]  =     0 *      0 |      0 |       0       0
A[DC2,S4]  =     0 *      0 |      0 |       0       0
A[DC2,S5]  =     0 *      0 |      0 |       0       0
A[DC2,S6]  =     0 *      0 |      0 |       0       0
A[DC2,S7]  =     0 *      0 |      0 |       0       0
A[DC2,S8]  =     0 *      0 |      0 |       0       0
A[DC2,S9]  =     0 *      0 |      0 |       0       0
```


```
Variable Analysis
 variable  =     x *  coeff |     rc | obj low obj high
X[DC0,S0]  =     0 * 1828.0 |      0 |       0       0
X[DC1,S0]  =     0 * 2271.0 |      0 |       0       0
X[DC2,S0]  =  18.0 *  807.0 |      0 |       0       0
X[DC0,S1]  =   7.0 * 1058.0 |      0 |       0       0
X[DC1,S1]  =     0 * 1746.0 |      0 |       0       0
X[DC2,S1]  =     0 * 1679.0 |      0 |       0       0
X[DC0,S2]  =     0 * 2014.0 |      0 |       0       0
X[DC1,S2]  =     0 * 2919.0 |      0 |       0       0
X[DC2,S2]  =  21.0 * 1779.0 |      0 |       0       0
X[DC0,S3]  =     0 * 2134.0 |      0 |       0       0
X[DC1,S3]  =  15.0 * 1982.0 |      0 |       0       0
X[DC2,S3]  =     0 * 1428.0 |      0 |       0       0
X[DC0,S4]  =  17.0 * 1952.0 |      0 |       0       0
X[DC1,S4]  =     0 * 2704.0 |      0 |       0       0
X[DC2,S4]  =     0 * 1456.0 |      0 |       0       0
X[DC0,S5]  =     0 * 2677.0 |      0 |       0       0
X[DC1,S5]  =  10.0 * 2577.0 |      0 |       0       0
X[DC2,S5]  =     0 * 1273.0 |      0 |       0       0
X[DC0,S6]  =     0 * 2548.0 |      0 |       0       0
X[DC1,S6]  =   6.0 * 2063.0 |      0 |       0       0
X[DC2,S6]  =     0 * 2160.0 |      0 |       0       0
X[DC0,S7]  =   8.0 * 2292.0 |      0 |       0       0
X[DC1,S7]  =     0 * 2807.0 |      0 |       0       0
X[DC2,S7]  =     0 *  559.0 |      0 |       0       0
X[DC0,S8]  =   7.0 * 2704.0 |      0 |       0       0
X[DC1,S8]  =     0 * 2924.0 |      0 |       0       0
X[DC2,S8]  =     0 * 1014.0 |      0 |       0       0
X[DC0,S9]  =   7.0 * 1153.0 |      0 |       0       0
X[DC1,S9]  =     0 * 1736.0 |      0 |       0       0
X[DC2,S9]  =     0 * 1514.0 |      0 |       0       0
```



## == CONSTRAINTS == ##

```
Constraint Analysis
           constr      rhs |  slack     pi | rhs low rhs high
      n_demand S0  >  18.0 |      0      0 |       0       0
      n_demand S1  >   7.0 |      0      0 |       0       0
      n_demand S2  >  21.0 |      0      0 |       0       0
      n_demand S3  >  15.0 |      0      0 |       0       0
      n_demand S4  >  17.0 |      0      0 |       0       0
      n_demand S5  >  10.0 |      0      0 |       0       0
      n_demand S6  >   6.0 |      0      0 |       0       0
      n_demand S7  >   8.0 |      0      0 |       0       0
      n_demand S8  >   7.0 |      0      0 |       0       0
      n_demand S9  >   7.0 |      0      0 |       0       0
   n_capacity DC0  <  72.0 |   26.0      0 |       0       0
   n_capacity DC1  <  76.0 |   45.0      0 |       0       0
   n_capacity DC2  <  40.0 |    1.0      0 |       0       0
   U0 s_demand S3  >  29.0 |      0      0 |       0       0
U0 s_capacity DC0  <  72.0 |   26.0      0 |       0       0
U0 s_capacity DC1  <  76.0 |   31.0      0 |       0       0
U0 s_capacity DC2  <  40.0 |    1.0      0 |       0       0
   U1 s_demand S7  >  31.0 |      0      0 |       0       0
U1 s_capacity DC0  <  72.0 |    3.0      0 |       0       0
U1 s_capacity DC1  <  76.0 |   45.0      0 |       0       0
U1 s_capacity DC2  <  40.0 |    1.0      0 |       0       0
   U2 s_demand S0  >  19.0 |      0      0 |       0       0
U2 s_capacity DC0  <  72.0 |   26.0      0 |       0       0
U2 s_capacity DC1  <  76.0 |   45.0      0 |       0       0
U2 s_capacity DC2  <  40.0 |      0      0 |       0       0
   U3 s_demand S8  >  30.0 |      0      0 |       0       0
U3 s_capacity DC0  <  72.0 |    3.0      0 |       0       0
U3 s_capacity DC1  <  76.0 |   45.0      0 |       0       0
U3 s_capacity DC2  <  40.0 |    1.0      0 |       0       0
   U4 s_demand S4  >  21.0 |      0      0 |       0       0
   U4 s_demand S5  >  54.0 |      0      0 |       0       0
U4 s_capacity DC0  <  72.0 |   22.0      0 |       0       0
U4 s_capacity DC1  <  76.0 |    1.0      0 |       0       0
U4 s_capacity DC2  <  40.0 |    1.0      0 |       0       0
```


## == NORMAL DEMAND ANALYSIS == ##

```
X[DC2,S0] = 18.0
X[DC0,S1] = 7.0
X[DC2,S2] = 21.0
X[DC1,S3] = 15.0
X[DC0,S4] = 17.0
X[DC1,S5] = 10.0
X[DC1,S6] = 6.0
X[DC0,S7] = 8.0
X[DC0,S8] = 7.0
X[DC0,S9] = 7.0
Store sums: {'S0': 18.0, 'S1': 7.0, 'S2': 21.0, 'S3': 15.0, 'S4': 17.0, 'S5': 10.0, 'S6': 6.0, 'S7': 8.0, 'S8': 7.0, 'S9': 7.0}
DC sums: {'DC0': 46.0, 'DC1': 31.0, 'DC2': 39.0}
```

## == SURGE ANALYSIS == ##

Surge multipliers
```
{('U0', 'S0'): 1.0, ('U1', 'S0'): 1.0, ('U2', 'S0'): 1.0555555555555556, ('U3', 'S0'): 1.0, ('U4', 'S0'): 1.0, ('U0', 'S1'): 1.0, ('U1', 'S1'): 1.0, ('U2', 'S1'): 1.0, ('U3', 'S1'): 1.0, ('U4', 'S1'): 1.0, ('U0', 'S2'): 1.0, ('U1', 'S2'): 1.0, ('U2', 'S2'): 1.0, ('U3', 'S2'): 1.0, ('U4', 'S2'): 1.0, ('U0', 'S3'): 1.9333333333333333, ('U1', 'S3'): 1.0, ('U2', 'S3'): 1.0, ('U3', 'S3'): 1.0, ('U4', 'S3'): 1.0, ('U0', 'S4'): 1.0, ('U1', 'S4'): 1.0, ('U2', 'S4'): 1.0, ('U3', 'S4'): 1.0, ('U4', 'S4'): 1.2352941176470589, ('U0', 'S5'): 1.0, ('U1', 'S5'): 1.0, ('U2', 'S5'): 1.0, ('U3', 'S5'): 1.0, ('U4', 'S5'): 5.4, ('U0', 'S6'): 1.0, ('U1', 'S6'): 1.0, ('U2', 'S6'): 1.0, ('U3', 'S6'): 1.0, ('U4', 'S6'): 1.0, ('U0', 'S7'): 1.0, ('U1', 'S7'): 3.875, ('U2', 'S7'): 1.0, ('U3', 'S7'): 1.0, ('U4', 'S7'): 1.0, ('U0', 'S8'): 1.0, ('U1', 'S8'): 1.0, ('U2', 'S8'): 1.0, ('U3', 'S8'): 4.285714285714286, ('U4', 'S8'): 1.0, ('U0', 'S9'): 1.0, ('U1', 'S9'): 1.0, ('U2', 'S9'): 1.0, ('U3', 'S9'): 1.0, ('U4', 'S9'): 1.0}
```

### Surge U0
```
Y[DC2,S0,U0] = 18.0
Y[DC0,S1,U0] = 7.0
Y[DC2,S2,U0] = 21.0
Y[DC1,S3,U0] = 29.0
Y[DC0,S4,U0] = 17.0
Y[DC1,S5,U0] = 10.0
Y[DC1,S6,U0] = 6.0
Y[DC0,S7,U0] = 8.0
Y[DC0,S8,U0] = 7.0
Y[DC0,S9,U0] = 7.0
Store sums: {'S0': 18.0, 'S1': 7.0, 'S2': 21.0, 'S3': 29.0, 'S4': 17.0, 'S5': 10.0, 'S6': 6.0, 'S7': 8.0, 'S8': 7.0, 'S9': 7.0}
DC sums: {'DC0': 46.0, 'DC1': 45.0, 'DC2': 39.0}
Cost (weekly, no labour): 233436.0
```

### Surge U1
```
Y[DC2,S0,U1] = 18.0
Y[DC0,S1,U1] = 7.0
Y[DC2,S2,U1] = 21.0
Y[DC1,S3,U1] = 15.0
Y[DC0,S4,U1] = 17.0
Y[DC1,S5,U1] = 10.0
Y[DC1,S6,U1] = 6.0
Y[DC0,S7,U1] = 31.0
Y[DC0,S8,U1] = 7.0
Y[DC0,S9,U1] = 7.0
Store sums: {'S0': 18.0, 'S1': 7.0, 'S2': 21.0, 'S3': 15.0, 'S4': 17.0, 'S5': 10.0, 'S6': 6.0, 'S7': 31.0, 'S8': 7.0, 'S9': 7.0}
DC sums: {'DC0': 69.0, 'DC1': 31.0, 'DC2': 39.0}
Cost (weekly, no labour): 258404.0
```

### Surge U2
```
Y[DC2,S0,U2] = 19.0
Y[DC0,S1,U2] = 7.0
Y[DC2,S2,U2] = 21.0
Y[DC1,S3,U2] = 15.0
Y[DC0,S4,U2] = 17.0
Y[DC1,S5,U2] = 10.0
Y[DC1,S6,U2] = 6.0
Y[DC0,S7,U2] = 8.0
Y[DC0,S8,U2] = 7.0
Y[DC0,S9,U2] = 7.0
Store sums: {'S0': 19.0, 'S1': 7.0, 'S2': 21.0, 'S3': 15.0, 'S4': 17.0, 'S5': 10.0, 'S6': 6.0, 'S7': 8.0, 'S8': 7.0, 'S9': 7.0}
DC sums: {'DC0': 46.0, 'DC1': 31.0, 'DC2': 40.0}
Cost (weekly, no labour): 206495.0
```

### Surge U3
```
Y[DC2,S0,U3] = 18.0
Y[DC0,S1,U3] = 7.0
Y[DC2,S2,U3] = 21.0
Y[DC1,S3,U3] = 15.0
Y[DC0,S4,U3] = 17.0
Y[DC1,S5,U3] = 10.0
Y[DC1,S6,U3] = 6.0
Y[DC0,S7,U3] = 8.0
Y[DC0,S8,U3] = 30.0
Y[DC0,S9,U3] = 7.0
Store sums: {'S0': 18.0, 'S1': 7.0, 'S2': 21.0, 'S3': 15.0, 'S4': 17.0, 'S5': 10.0, 'S6': 6.0, 'S7': 8.0, 'S8': 30.0, 'S9': 7.0}
DC sums: {'DC0': 69.0, 'DC1': 31.0, 'DC2': 39.0}
Cost (weekly, no labour): 267880.0
```

### Surge U4
```
Y[DC2,S0,U4] = 18.0
Y[DC0,S1,U4] = 7.0
Y[DC2,S2,U4] = 21.0
Y[DC1,S3,U4] = 15.0
Y[DC0,S4,U4] = 21.0
Y[DC1,S5,U4] = 54.0
Y[DC1,S6,U4] = 6.0
Y[DC0,S7,U4] = 8.0
Y[DC0,S8,U4] = 7.0
Y[DC0,S9,U4] = 7.0
Store sums: {'S0': 18.0, 'S1': 7.0, 'S2': 21.0, 'S3': 15.0, 'S4': 21.0, 'S5': 54.0, 'S6': 6.0, 'S7': 8.0, 'S8': 7.0, 'S9': 7.0}
DC sums: {'DC0': 50.0, 'DC1': 75.0, 'DC2': 39.0}
Cost (weekly, no labour): 326884.0
```

## == STORE ASSIGNMENTS == ##
```
Store Assignments
store |    DC0    DC1    DC2
   S0 |                  1.0
   S1 |    1.0              
   S2 |                  1.0
   S3 |           1.0       
   S4 |    1.0              
   S5 |           1.0       
   S6 |           1.0       
   S7 |    1.0              
   S8 |    1.0              
   S9 |    1.0              
```

```
Store & DC0 & DC1 & DC2 \\
S0 &  &  & 100\% \\
S1 & 100\% &  &  \\
S2 &  &  & 100\% \\
S3 &  & 100\% &  \\
S4 & 100\% &  &  \\
S5 &  & 100\% &  \\
S6 &  & 100\% &  \\
S7 & 100\% &  &  \\
S8 & 100\% &  &  \\
S9 & 100\% &  &  \\
```

This was communication 5 with value 205688.0
