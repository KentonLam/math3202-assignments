Communication 9
==============================================================================

```
Academic license - for non-commercial use only
Optimize a model with 522 rows, 546 columns and 1964 nonzeros
Variable types: 420 continuous, 126 integer (77 binary)
Coefficient statistics:
  Matrix range     [1e+00, 8e+01]
  Objective range  [1e+03, 2e+05]
  Bounds range     [1e+00, 1e+00]
  RHS range        [2e+00, 5e+01]
Presolve removed 446 rows and 433 columns
Presolve time: 0.00s
Presolved: 76 rows, 113 columns, 802 nonzeros
Variable types: 0 continuous, 113 integer (69 binary)
Found heuristic solution: objective 1.485643e+07

Root relaxation: objective 1.202714e+07, 51 iterations, 0.00 seconds

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0 1.2027e+07    0   23 1.4856e+07 1.2027e+07  19.0%     -    0s
H    0     0                    1.356383e+07 1.2027e+07  11.3%     -    0s
     0     0 1.2512e+07    0    9 1.3564e+07 1.2512e+07  7.76%     -    0s
H    0     0                    1.318347e+07 1.2512e+07  5.10%     -    0s
H    0     0                    1.297404e+07 1.2512e+07  3.56%     -    0s
     0     0 1.2512e+07    0   10 1.2974e+07 1.2512e+07  3.56%     -    0s
     0     0 1.2512e+07    0   10 1.2974e+07 1.2512e+07  3.56%     -    0s
     0     0 1.2538e+07    0   39 1.2974e+07 1.2538e+07  3.36%     -    0s
H    0     0                    1.268775e+07 1.2538e+07  1.18%     -    0s
H    0     0                    1.261326e+07 1.2538e+07  0.59%     -    0s
     0     0 1.2560e+07    0    2 1.2613e+07 1.2560e+07  0.42%     -    0s
     0     0 1.2564e+07    0    9 1.2613e+07 1.2564e+07  0.39%     -    0s
*    0     0               0    1.257602e+07 1.2576e+07  0.00%     -    0s

Cutting planes:
  Gomory: 2
  Cover: 6
  Clique: 2
  MIR: 9
  StrongCG: 4

Explored 1 nodes (108 simplex iterations) in 0.02 seconds
Thread count was 4 (of 4 available processors)

Solution count 7: 1.2576e+07 1.26133e+07 1.26878e+07 ... 1.48564e+07

Optimal solution found (tolerance 1.00e-04)
Best objective 1.257601800000e+07, best bound 1.257601800000e+07, gap 0.0000%
```

## -- GUROBI OUTPUT -- ##
### 12576018.0
```
Optimised for communication 9.
Objective value: 12576018.0
Weekly average: 241846.5
```




## == ANALYSIS NON-ZERO == ##
(variables not printed are 0)

```
Variable Analysis
 variable  =     x *  coeff |     rc | obj low obj high
A[DC1,S5]  =   1.0 *      0 |      - |       -       -
A[DC1,S6]  =   1.0 *      0 |      - |       -       -
A[DC2,S7]  =   1.0 *      0 |      - |       -       -
A[DC2,S8]  =   1.0 *      0 |      - |       -       -
A[DC3,S0]  =   1.0 *      0 |      - |       -       -
A[DC3,S1]  =   1.0 *      0 |      - |       -       -
A[DC3,S2]  =   1.0 *      0 |      - |       -       -
A[DC3,S4]  =   1.0 *      0 |      - |       -       -
A[DC3,S9]  =   1.0 *      0 |      - |       -       -
A[DC5,S3]  =   1.0 *      0 |      - |       -       -
```

```
Variable Analysis
  variable  =     x *  coeff |     rc | obj low obj high
Build[DC1]  =   1.0 *      0 |      - |       -       -
Build[DC2]  =   1.0 *      0 |      - |       -       -
Build[DC3]  =   1.0 *      0 |      - |       -       -
Build[DC5]  =   1.0 *      0 |      - |       -       -
```

```
Variable Analysis
variable  =     x *  coeff |     rc | obj low obj high
```

```
Variable Analysis
variable  =     x *  coeff |     rc | obj low obj high
FT[DC1]  =   2.0 * 234000.0 |      - |       -       -
FT[DC2]  =   2.0 * 234000.0 |      - |       -       -
FT[DC3]  =   8.0 * 234000.0 |      - |       -       -
FT[DC5]  =   2.0 * 234000.0 |      - |       -       -
```

```
Variable Analysis
  variable  =     x *  coeff |     rc | obj low obj high
CA[U0,DC5]  =  11.0 * 14755.0 |      - |       -       -
CA[U1,DC2]  =  20.0 * 14755.0 |      - |       -       -
CA[U3,DC2]  =  20.0 * 5902.0 |      - |       -       -
CA[U4,DC1]  =  42.0 * 14755.0 |      - |       -       -
CA[U4,DC3]  =   2.0 * 14755.0 |      - |       -       -
```


```
Variable Analysis
 variable  =     x *  coeff |     rc | obj low obj high
X[DC3,S0]  =  18.0 * 38048.0 |      - |       -       -
X[DC3,S1]  =   7.0 * 20938.0 |      - |       -       -
X[DC3,S2]  =  21.0 * 36279.0 |      - |       -       -
X[DC5,S3]  =  15.0 * 19372.0 |      - |       -       -
X[DC3,S4]  =  17.0 * 32625.0 |      - |       -       -
X[DC1,S5]  =  10.0 * 74733.0 |      - |       -       -
X[DC1,S6]  =   6.0 * 59827.0 |      - |       -       -
X[DC2,S7]  =   8.0 * 16211.0 |      - |       -       -
X[DC2,S8]  =   7.0 * 29406.0 |      - |       -       -
X[DC3,S9]  =   7.0 * 28884.0 |      - |       -       -
```

```
Variable Analysis
    variable  =     x *  coeff |     rc | obj low obj high
Y[DC3,S0,U0]  =  18.0 * 6560.0 |      - |       -       -
Y[DC3,S1,U0]  =   7.0 * 3610.0 |      - |       -       -
Y[DC3,S2,U0]  =  21.0 * 6255.0 |      - |       -       -
Y[DC5,S3,U0]  =  29.0 * 3340.0 |      - |       -       -
Y[DC3,S4,U0]  =  17.0 * 5625.0 |      - |       -       -
Y[DC1,S5,U0]  =  10.0 * 12885.0 |      - |       -       -
Y[DC1,S6,U0]  =   6.0 * 10315.0 |      - |       -       -
Y[DC2,S7,U0]  =   8.0 * 2795.0 |      - |       -       -
Y[DC2,S8,U0]  =   7.0 * 5070.0 |      - |       -       -
Y[DC3,S9,U0]  =   7.0 * 4980.0 |      - |       -       -
Y[DC3,S0,U1]  =  18.0 * 6560.0 |      - |       -       -
Y[DC3,S1,U1]  =   7.0 * 3610.0 |      - |       -       -
Y[DC3,S2,U1]  =  21.0 * 6255.0 |      - |       -       -
Y[DC5,S3,U1]  =  15.0 * 3340.0 |      - |       -       -
Y[DC3,S4,U1]  =  17.0 * 5625.0 |      - |       -       -
Y[DC1,S5,U1]  =  10.0 * 12885.0 |      - |       -       -
Y[DC1,S6,U1]  =   6.0 * 10315.0 |      - |       -       -
Y[DC2,S7,U1]  =  31.0 * 2795.0 |      - |       -       -
Y[DC2,S8,U1]  =   7.0 * 5070.0 |      - |       -       -
Y[DC3,S9,U1]  =   7.0 * 4980.0 |      - |       -       -
Y[DC3,S0,U2]  =  19.0 * 7872.0 |      - |       -       -
Y[DC3,S1,U2]  =   7.0 * 4332.0 |      - |       -       -
Y[DC3,S2,U2]  =  21.0 * 7506.0 |      - |       -       -
Y[DC5,S3,U2]  =  15.0 * 4008.0 |      - |       -       -
Y[DC3,S4,U2]  =  17.0 * 6750.0 |      - |       -       -
Y[DC1,S5,U2]  =  10.0 * 15462.0 |      - |       -       -
Y[DC1,S6,U2]  =   6.0 * 12378.0 |      - |       -       -
Y[DC2,S7,U2]  =   8.0 * 3354.0 |      - |       -       -
Y[DC2,S8,U2]  =   7.0 * 6084.0 |      - |       -       -
Y[DC3,S9,U2]  =   7.0 * 5976.0 |      - |       -       -
Y[DC3,S0,U3]  =  18.0 * 2624.0 |      - |       -       -
Y[DC3,S1,U3]  =   7.0 * 1444.0 |      - |       -       -
Y[DC3,S2,U3]  =  21.0 * 2502.0 |      - |       -       -
Y[DC5,S3,U3]  =  15.0 * 1336.0 |      - |       -       -
Y[DC3,S4,U3]  =  17.0 * 2250.0 |      - |       -       -
Y[DC1,S5,U3]  =  10.0 * 5154.0 |      - |       -       -
Y[DC1,S6,U3]  =   6.0 * 4126.0 |      - |       -       -
Y[DC2,S7,U3]  =   8.0 * 1118.0 |      - |       -       -
Y[DC2,S8,U3]  =  30.0 * 2028.0 |      - |       -       -
Y[DC3,S9,U3]  =   7.0 * 1992.0 |      - |       -       -
Y[DC3,S0,U4]  =  18.0 * 6560.0 |      - |       -       -
Y[DC3,S1,U4]  =   7.0 * 3610.0 |      - |       -       -
Y[DC3,S2,U4]  =  21.0 * 6255.0 |      - |       -       -
Y[DC5,S3,U4]  =  15.0 * 3340.0 |      - |       -       -
Y[DC3,S4,U4]  =  21.0 * 5625.0 |      - |       -       -
Y[DC1,S5,U4]  =  54.0 * 12885.0 |      - |       -       -
Y[DC1,S6,U4]  =   6.0 * 10315.0 |      - |       -       -
Y[DC2,S7,U4]  =   8.0 * 2795.0 |      - |       -       -
Y[DC2,S8,U4]  =   7.0 * 5070.0 |      - |       -       -
Y[DC3,S9,U4]  =   7.0 * 4980.0 |      - |       -       -
```


## == CONSTRAINTS == ##

```
Constraint Analysis
           constr      rhs |  slack     pi | rhs low rhs high
      n_demand S0  >  18.0 |      0      - |       -       -
      n_demand S1  >   7.0 |      0      - |       -       -
      n_demand S2  >  21.0 |      0      - |       -       -
      n_demand S3  >  15.0 |      0      - |       -       -
      n_demand S4  >  17.0 |      0      - |       -       -
      n_demand S5  >  10.0 |      0      - |       -       -
      n_demand S6  >   6.0 |      0      - |       -       -
      n_demand S7  >   8.0 |      0      - |       -       -
      n_demand S8  >   7.0 |      0      - |       -       -
      n_demand S9  >   7.0 |      0      - |       -       -
   n_capacity DC0  <     0 |      0      - |       -       -
   n_capacity DC1  <     0 |   60.0      - |       -       -
   n_capacity DC2  <     0 |   25.0      - |       -       -
   n_capacity DC3  <     0 |    4.0      - |       -       -
   n_capacity DC4  <     0 |      0      - |       -       -
   n_capacity DC5  <     0 |   14.0      - |       -       -
   n_capacity DC6  <     0 |      0      - |       -       -
           new_dc  <   2.0 |      0      - |       -       -
          all_dcs  =   4.0 |      0      - |       -       -
       labour DC0  <     0 |      0      - |       -       -
       labour DC1  <     0 |    2.0      - |       -       -
       labour DC2  <     0 |    3.0      - |       -       -
       labour DC3  <     0 |    2.0      - |       -       -
       labour DC4  <     0 |      0      - |       -       -
       labour DC5  <     0 |    3.0      - |       -       -
       labour DC6  <     0 |      0      - |       -       -
   U0 s_demand S3  >  29.0 |      0      - |       -       -
U0 s_capacity DC0  <     0 |      0      - |       -       -
U0 s_capacity DC1  <     0 |   60.0      - |       -       -
U0 s_capacity DC2  <     0 |   25.0      - |       -       -
U0 s_capacity DC3  <     0 |    4.0      - |       -       -
U0 s_capacity DC4  <     0 |      0      - |       -       -
U0 s_capacity DC5  <     0 |      0      - |       -       -
U0 s_capacity DC6  <     0 |      0      - |       -       -
  U0 s_labour DC0  <     0 |      0      - |       -       -
  U0 s_labour DC1  <     0 |    2.0      - |       -       -
  U0 s_labour DC2  <     0 |    3.0      - |       -       -
  U0 s_labour DC3  <     0 |    2.0      - |       -       -
  U0 s_labour DC4  <     0 |      0      - |       -       -
  U0 s_labour DC5  <     0 |      0      - |       -       -
  U0 s_labour DC6  <     0 |      0      - |       -       -
   U1 s_demand S7  >  31.0 |      0      - |       -       -
U1 s_capacity DC0  <     0 |      0      - |       -       -
U1 s_capacity DC1  <     0 |   60.0      - |       -       -
U1 s_capacity DC2  <     0 |    2.0      - |       -       -
U1 s_capacity DC3  <     0 |    4.0      - |       -       -
U1 s_capacity DC4  <     0 |      0      - |       -       -
U1 s_capacity DC5  <     0 |   14.0      - |       -       -
U1 s_capacity DC6  <     0 |      0      - |       -       -
  U1 s_labour DC0  <     0 |      0      - |       -       -
  U1 s_labour DC1  <     0 |    2.0      - |       -       -
  U1 s_labour DC2  <     0 |      0      - |       -       -
  U1 s_labour DC3  <     0 |    2.0      - |       -       -
  U1 s_labour DC4  <     0 |      0      - |       -       -
  U1 s_labour DC5  <     0 |    3.0      - |       -       -
  U1 s_labour DC6  <     0 |      0      - |       -       -
   U2 s_demand S0  >  19.0 |      0      - |       -       -
U2 s_capacity DC0  <     0 |      0      - |       -       -
U2 s_capacity DC1  <     0 |   60.0      - |       -       -
U2 s_capacity DC2  <     0 |   25.0      - |       -       -
U2 s_capacity DC3  <     0 |    3.0      - |       -       -
U2 s_capacity DC4  <     0 |      0      - |       -       -
U2 s_capacity DC5  <     0 |   14.0      - |       -       -
U2 s_capacity DC6  <     0 |      0      - |       -       -
  U2 s_labour DC0  <     0 |      0      - |       -       -
  U2 s_labour DC1  <     0 |    2.0      - |       -       -
  U2 s_labour DC2  <     0 |    3.0      - |       -       -
  U2 s_labour DC3  <     0 |    1.0      - |       -       -
  U2 s_labour DC4  <     0 |      0      - |       -       -
  U2 s_labour DC5  <     0 |    3.0      - |       -       -
  U2 s_labour DC6  <     0 |      0      - |       -       -
   U3 s_demand S8  >  30.0 |      0      - |       -       -
U3 s_capacity DC0  <     0 |      0      - |       -       -
U3 s_capacity DC1  <     0 |   60.0      - |       -       -
U3 s_capacity DC2  <     0 |    2.0      - |       -       -
U3 s_capacity DC3  <     0 |    4.0      - |       -       -
U3 s_capacity DC4  <     0 |      0      - |       -       -
U3 s_capacity DC5  <     0 |   14.0      - |       -       -
U3 s_capacity DC6  <     0 |      0      - |       -       -
  U3 s_labour DC0  <     0 |      0      - |       -       -
  U3 s_labour DC1  <     0 |    2.0      - |       -       -
  U3 s_labour DC2  <     0 |      0      - |       -       -
  U3 s_labour DC3  <     0 |    2.0      - |       -       -
  U3 s_labour DC4  <     0 |      0      - |       -       -
  U3 s_labour DC5  <     0 |    3.0      - |       -       -
  U3 s_labour DC6  <     0 |      0      - |       -       -
   U4 s_demand S4  >  21.0 |      0      - |       -       -
   U4 s_demand S5  >  54.0 |      0      - |       -       -
U4 s_capacity DC0  <     0 |      0      - |       -       -
U4 s_capacity DC1  <     0 |   16.0      - |       -       -
U4 s_capacity DC2  <     0 |   25.0      - |       -       -
U4 s_capacity DC3  <     0 |      0      - |       -       -
U4 s_capacity DC4  <     0 |      0      - |       -       -
U4 s_capacity DC5  <     0 |   14.0      - |       -       -
U4 s_capacity DC6  <     0 |      0      - |       -       -
  U4 s_labour DC0  <     0 |      0      - |       -       -
  U4 s_labour DC1  <     0 |      0      - |       -       -
  U4 s_labour DC2  <     0 |    3.0      - |       -       -
  U4 s_labour DC3  <     0 |      0      - |       -       -
  U4 s_labour DC4  <     0 |      0      - |       -       -
  U4 s_labour DC5  <     0 |    3.0      - |       -       -
  U4 s_labour DC6  <     0 |      0      - |       -       -
```


## == NORMAL DEMAND ANALYSIS == ##

```
X[DC3,S0] = 18.0
X[DC3,S1] = 7.0
X[DC3,S2] = 21.0
X[DC5,S3] = 15.0
X[DC3,S4] = 17.0
X[DC1,S5] = 10.0
X[DC1,S6] = 6.0
X[DC2,S7] = 8.0
X[DC2,S8] = 7.0
X[DC3,S9] = 7.0
Store sums: {'S0': 18.0, 'S1': 7.0, 'S2': 21.0, 'S3': 15.0, 'S4': 17.0, 'S5': 10.0, 'S6': 6.0, 'S7': 8.0, 'S8': 7.0, 'S9': 7.0}
DC sums: {'DC0': 0.0, 'DC1': 16.0, 'DC2': 15.0, 'DC3': 70.0, 'DC4': 0.0, 'DC5': 15.0, 'DC6': 0.0}
FTPT sums: {'DC0': 0.0, 'DC1': 18.0, 'DC2': 18.0, 'DC3': 72.0, 'DC4': 0.0, 'DC5': 18.0, 'DC6': 0.0}
```

## == SURGE ANALYSIS == ##

Surge multipliers
```
{('U0', 'S0'): 1.0, ('U1', 'S0'): 1.0, ('U2', 'S0'): 1.0555555555555556, ('U3', 'S0'): 1.0, ('U4', 'S0'): 1.0, ('U0', 'S1'): 1.0, ('U1', 'S1'): 1.0, ('U2', 'S1'): 1.0, ('U3', 'S1'): 1.0, ('U4', 'S1'): 1.0, ('U0', 'S2'): 1.0, ('U1', 'S2'): 1.0, ('U2', 'S2'): 1.0, ('U3', 'S2'): 1.0, ('U4', 'S2'): 1.0, ('U0', 'S3'): 1.9333333333333333, ('U1', 'S3'): 1.0, ('U2', 'S3'): 1.0, ('U3', 'S3'): 1.0, ('U4', 'S3'): 1.0, ('U0', 'S4'): 1.0, ('U1', 'S4'): 1.0, ('U2', 'S4'): 1.0, ('U3', 'S4'): 1.0, ('U4', 'S4'): 1.2352941176470589, ('U0', 'S5'): 1.0, ('U1', 'S5'): 1.0, ('U2', 'S5'): 1.0, ('U3', 'S5'): 1.0, ('U4', 'S5'): 5.4, ('U0', 'S6'): 1.0, ('U1', 'S6'): 1.0, ('U2', 'S6'): 1.0, ('U3', 'S6'): 1.0, ('U4', 'S6'): 1.0, ('U0', 'S7'): 1.0, ('U1', 'S7'): 3.875, ('U2', 'S7'): 1.0, ('U3', 'S7'): 1.0, ('U4', 'S7'): 1.0, ('U0', 'S8'): 1.0, ('U1', 'S8'): 1.0, ('U2', 'S8'): 1.0, ('U3', 'S8'): 4.285714285714286, ('U4', 'S8'): 1.0, ('U0', 'S9'): 1.0, ('U1', 'S9'): 1.0, ('U2', 'S9'): 1.0, ('U3', 'S9'): 1.0, ('U4', 'S9'): 1.0}
```

### Surge U0
```
Y[DC3,S0,U0] = 18.0
Y[DC3,S1,U0] = 7.0
Y[DC3,S2,U0] = 21.0
Y[DC5,S3,U0] = 29.0
Y[DC3,S4,U0] = 17.0
Y[DC1,S5,U0] = 10.0
Y[DC1,S6,U0] = 6.0
Y[DC2,S7,U0] = 8.0
Y[DC2,S8,U0] = 7.0
Y[DC3,S9,U0] = 7.0
Store sums: {'S0': 18.0, 'S1': 7.0, 'S2': 21.0, 'S3': 29.0, 'S4': 17.0, 'S5': 10.0, 'S6': 6.0, 'S7': 8.0, 'S8': 7.0, 'S9': 7.0}
DC sums: {'DC0': 0.0, 'DC1': 16.0, 'DC2': 15.0, 'DC3': 70.0, 'DC4': 0.0, 'DC5': 29.0, 'DC6': 0.0}
Casuals: {'DC5': 11.0}
Cost (weekly, no labour): 150128.0
Cost (yearly, with labour): 912945.0
  Transport: 750640.0
  Casual labour: 162305.0
Weekly: 182589.0
Surge duration: 5
```

### Surge U1
```
Y[DC3,S0,U1] = 18.0
Y[DC3,S1,U1] = 7.0
Y[DC3,S2,U1] = 21.0
Y[DC5,S3,U1] = 15.0
Y[DC3,S4,U1] = 17.0
Y[DC1,S5,U1] = 10.0
Y[DC1,S6,U1] = 6.0
Y[DC2,S7,U1] = 31.0
Y[DC2,S8,U1] = 7.0
Y[DC3,S9,U1] = 7.0
Store sums: {'S0': 18.0, 'S1': 7.0, 'S2': 21.0, 'S3': 15.0, 'S4': 17.0, 'S5': 10.0, 'S6': 6.0, 'S7': 31.0, 'S8': 7.0, 'S9': 7.0}
DC sums: {'DC0': 0.0, 'DC1': 16.0, 'DC2': 38.0, 'DC3': 70.0, 'DC4': 0.0, 'DC5': 15.0, 'DC6': 0.0}
Casuals: {'DC2': 20.0}
Cost (weekly, no labour): 153633.0
Cost (yearly, with labour): 1063265.0
  Transport: 768165.0
  Casual labour: 295100.0
Weekly: 212653.0
Surge duration: 5
```

### Surge U2
```
Y[DC3,S0,U2] = 19.0
Y[DC3,S1,U2] = 7.0
Y[DC3,S2,U2] = 21.0
Y[DC5,S3,U2] = 15.0
Y[DC3,S4,U2] = 17.0
Y[DC1,S5,U2] = 10.0
Y[DC1,S6,U2] = 6.0
Y[DC2,S7,U2] = 8.0
Y[DC2,S8,U2] = 7.0
Y[DC3,S9,U2] = 7.0
Store sums: {'S0': 19.0, 'S1': 7.0, 'S2': 21.0, 'S3': 15.0, 'S4': 17.0, 'S5': 10.0, 'S6': 6.0, 'S7': 8.0, 'S8': 7.0, 'S9': 7.0}
DC sums: {'DC0': 0.0, 'DC1': 16.0, 'DC2': 15.0, 'DC3': 71.0, 'DC4': 0.0, 'DC5': 15.0, 'DC6': 0.0}
Casuals: {}
Cost (weekly, no labour): 142088.0
Cost (yearly, with labour): 852528.0
  Transport: 852528.0
  Casual labour: 0.0
Weekly: 142088.0
Surge duration: 6
```

### Surge U3
```
Y[DC3,S0,U3] = 18.0
Y[DC3,S1,U3] = 7.0
Y[DC3,S2,U3] = 21.0
Y[DC5,S3,U3] = 15.0
Y[DC3,S4,U3] = 17.0
Y[DC1,S5,U3] = 10.0
Y[DC1,S6,U3] = 6.0
Y[DC2,S7,U3] = 8.0
Y[DC2,S8,U3] = 30.0
Y[DC3,S9,U3] = 7.0
Store sums: {'S0': 18.0, 'S1': 7.0, 'S2': 21.0, 'S3': 15.0, 'S4': 17.0, 'S5': 10.0, 'S6': 6.0, 'S7': 8.0, 'S8': 30.0, 'S9': 7.0}
DC sums: {'DC0': 0.0, 'DC1': 16.0, 'DC2': 38.0, 'DC3': 70.0, 'DC4': 0.0, 'DC5': 15.0, 'DC6': 0.0}
Casuals: {'DC2': 20.0}
Cost (weekly, no labour): 164098.0
Cost (yearly, with labour): 446236.0
  Transport: 328196.0
  Casual labour: 118040.0
Weekly: 223118.0
Surge duration: 2
```

### Surge U4
```
Y[DC3,S0,U4] = 18.0
Y[DC3,S1,U4] = 7.0
Y[DC3,S2,U4] = 21.0
Y[DC5,S3,U4] = 15.0
Y[DC3,S4,U4] = 21.0
Y[DC1,S5,U4] = 54.0
Y[DC1,S6,U4] = 6.0
Y[DC2,S7,U4] = 8.0
Y[DC2,S8,U4] = 7.0
Y[DC3,S9,U4] = 7.0
Store sums: {'S0': 18.0, 'S1': 7.0, 'S2': 21.0, 'S3': 15.0, 'S4': 21.0, 'S5': 54.0, 'S6': 6.0, 'S7': 8.0, 'S8': 7.0, 'S9': 7.0}
DC sums: {'DC0': 0.0, 'DC1': 60.0, 'DC2': 15.0, 'DC3': 74.0, 'DC4': 0.0, 'DC5': 15.0, 'DC6': 0.0}
Casuals: {'DC1': 42.0, 'DC3': 2.0}
Cost (weekly, no labour): 258664.0
Cost (yearly, with labour): 1942540.0
  Transport: 1293320.0
  Casual labour: 649220.0
Weekly: 388508.0
Surge duration: 5
```

## == STORE ASSIGNMENTS == ##
```
Store Assignments
store |    DC0    DC1    DC2    DC3    DC4    DC5    DC6
   S0 |                         1.0                     
   S1 |                         1.0                     
   S2 |                         1.0                     
   S3 |                                       1.0       
   S4 |                         1.0                     
   S5 |           1.0                                   
   S6 |           1.0                                   
   S7 |                  1.0                            
   S8 |                  1.0                            
   S9 |                         1.0                     
```

```
Store & DC0 & DC1 & DC2 & DC3 & DC4 & DC5 & DC6 \\
S0 &  &  &  & 100\% &  &  &  \\
S1 &  &  &  & 100\% &  &  &  \\
S2 &  &  &  & 100\% &  &  &  \\
S3 &  &  &  &  &  & 100\% &  \\
S4 &  &  &  & 100\% &  &  &  \\
S5 &  & 100\% &  &  &  &  &  \\
S6 &  & 100\% &  &  &  &  &  \\
S7 &  &  & 100\% &  &  &  &  \\
S8 &  &  & 100\% &  &  &  &  \\
S9 &  &  &  & 100\% &  &  &  \\
```

This was communication 9 with value 12576018.0
