Communication 7
==============================================================================

Academic license - for non-commercial use only
Optimize a model with 480 rows, 497 columns and 1425 nonzeros
Variable types: 420 continuous, 77 integer (77 binary)
Coefficient statistics:
  Matrix range     [1e+00, 8e+01]
  Objective range  [6e+02, 4e+03]
  Bounds range     [1e+00, 1e+00]
  RHS range        [2e+00, 5e+01]
Presolve removed 441 rows and 428 columns
Presolve time: 0.00s
Presolved: 39 rows, 69 columns, 358 nonzeros
Variable types: 0 continuous, 69 integer (69 binary)
Found heuristic solution: objective 163537.00000

Root relaxation: objective 1.324526e+05, 27 iterations, 0.00 seconds

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0 132452.615    0   13 163537.000 132452.615  19.0%     -    0s
H    0     0                    149224.00000 132452.615  11.2%     -    0s
H    0     0                    140776.00000 132452.615  5.91%     -    0s
     0     0     cutoff    0      140776.000 140776.000  0.00%     -    0s

Cutting planes:
  Cover: 7
  MIR: 1

Explored 1 nodes (38 simplex iterations) in 0.01 seconds
Thread count was 4 (of 4 available processors)

Solution count 3: 140776 149224 163537 

Optimal solution found (tolerance 1.00e-04)
Best objective 1.407760000000e+05, best bound 1.407760000000e+05, gap 0.0000%

## -- GUROBI OUTPUT -- ##
### 140776.0
Optimised for communication 7.
Objective value: 140776.0




## == ANALYSIS NON-ZERO == ##
(variables not printed are 0)

Variable Analysis
 variable  =     x *  coeff |     rc | obj low obj high
A[DC1,S5]  =   1.0 *    0.0 |      0 |       0       0
A[DC1,S6]  =   1.0 *    0.0 |      0 |       0       0
A[DC2,S7]  =   1.0 *    0.0 |      0 |       0       0
A[DC2,S8]  =   1.0 *    0.0 |      0 |       0       0
A[DC3,S0]  =   1.0 *    0.0 |      0 |       0       0
A[DC3,S1]  =   1.0 *    0.0 |      0 |       0       0
A[DC3,S2]  =   1.0 *    0.0 |      0 |       0       0
A[DC3,S4]  =   1.0 *    0.0 |      0 |       0       0
A[DC3,S9]  =   1.0 *    0.0 |      0 |       0       0
A[DC5,S3]  =   1.0 *    0.0 |      0 |       0       0

Variable Analysis
  variable  =     x *  coeff |     rc | obj low obj high
Build[DC1]  =   1.0 *    0.0 |      0 |       0       0
Build[DC2]  =   1.0 *    0.0 |      0 |       0       0
Build[DC3]  =   1.0 *    0.0 |      0 |       0       0
Build[DC5]  =   1.0 *    0.0 |      0 |       0       0


Variable Analysis
 variable  =     x *  coeff |     rc | obj low obj high
X[DC3,S0]  =  18.0 * 1312.0 |      0 |       0       0
X[DC3,S1]  =   7.0 *  722.0 |      0 |       0       0
X[DC3,S2]  =  21.0 * 1251.0 |      0 |       0       0
X[DC5,S3]  =  15.0 *  668.0 |      0 |       0       0
X[DC3,S4]  =  17.0 * 1125.0 |      0 |       0       0
X[DC1,S5]  =  10.0 * 2577.0 |      0 |       0       0
X[DC1,S6]  =   6.0 * 2063.0 |      0 |       0       0
X[DC2,S7]  =   8.0 *  559.0 |      0 |       0       0
X[DC2,S8]  =   7.0 * 1014.0 |      0 |       0       0
X[DC3,S9]  =   7.0 *  996.0 |      0 |       0       0



## == CONSTRAINTS == ##

Constraint Analysis
           constr      rhs |  slack     pi | rhs low rhs high
      n_demand S0  >  18.0 |   -0.0      0 |       0       0
      n_demand S1  >   7.0 |   -0.0      0 |       0       0
      n_demand S2  >  21.0 |   -0.0      0 |       0       0
      n_demand S3  >  15.0 |   -0.0      0 |       0       0
      n_demand S4  >  17.0 |   -0.0      0 |       0       0
      n_demand S5  >  10.0 |   -0.0      0 |       0       0
      n_demand S6  >   6.0 |   -0.0      0 |       0       0
      n_demand S7  >   8.0 |   -0.0      0 |       0       0
      n_demand S8  >   7.0 |   -0.0      0 |       0       0
      n_demand S9  >   7.0 |   -0.0      0 |       0       0
   n_capacity DC0  <   0.0 |    0.0      0 |       0       0
   n_capacity DC1  <   0.0 |   60.0      0 |       0       0
   n_capacity DC2  <   0.0 |   25.0      0 |       0       0
   n_capacity DC3  <   0.0 |    4.0      0 |       0       0
   n_capacity DC4  <   0.0 |    0.0      0 |       0       0
   n_capacity DC5  <   0.0 |   14.0      0 |       0       0
   n_capacity DC6  <   0.0 |    0.0      0 |       0       0
           new_dc  <   2.0 |    0.0      0 |       0       0
          all_dcs  <   4.0 |    0.0      0 |       0       0
   U0 s_demand S3  >  29.0 |   -0.0      0 |       0       0
U0 s_capacity DC0  <   0.0 |    0.0      0 |       0       0
U0 s_capacity DC1  <   0.0 |   60.0      0 |       0       0
U0 s_capacity DC2  <   0.0 |   25.0      0 |       0       0
U0 s_capacity DC3  <   0.0 |    4.0      0 |       0       0
U0 s_capacity DC4  <   0.0 |    0.0      0 |       0       0
U0 s_capacity DC5  <   0.0 |    0.0      0 |       0       0
U0 s_capacity DC6  <   0.0 |    0.0      0 |       0       0
   U1 s_demand S7  >  31.0 |   -0.0      0 |       0       0
U1 s_capacity DC0  <   0.0 |    0.0      0 |       0       0
U1 s_capacity DC1  <   0.0 |   60.0      0 |       0       0
U1 s_capacity DC2  <   0.0 |    2.0      0 |       0       0
U1 s_capacity DC3  <   0.0 |    4.0      0 |       0       0
U1 s_capacity DC4  <   0.0 |    0.0      0 |       0       0
U1 s_capacity DC5  <   0.0 |   14.0      0 |       0       0
U1 s_capacity DC6  <   0.0 |    0.0      0 |       0       0
   U2 s_demand S0  >  19.0 |   -0.0      0 |       0       0
U2 s_capacity DC0  <   0.0 |    0.0      0 |       0       0
U2 s_capacity DC1  <   0.0 |   60.0      0 |       0       0
U2 s_capacity DC2  <   0.0 |   25.0      0 |       0       0
U2 s_capacity DC3  <   0.0 |    3.0      0 |       0       0
U2 s_capacity DC4  <   0.0 |    0.0      0 |       0       0
U2 s_capacity DC5  <   0.0 |   14.0      0 |       0       0
U2 s_capacity DC6  <   0.0 |    0.0      0 |       0       0
   U3 s_demand S8  >  30.0 |   -0.0      0 |       0       0
U3 s_capacity DC0  <   0.0 |    0.0      0 |       0       0
U3 s_capacity DC1  <   0.0 |   60.0      0 |       0       0
U3 s_capacity DC2  <   0.0 |    2.0      0 |       0       0
U3 s_capacity DC3  <   0.0 |    4.0      0 |       0       0
U3 s_capacity DC4  <   0.0 |    0.0      0 |       0       0
U3 s_capacity DC5  <   0.0 |   14.0      0 |       0       0
U3 s_capacity DC6  <   0.0 |    0.0      0 |       0       0
   U4 s_demand S4  >  21.0 |   -0.0      0 |       0       0
   U4 s_demand S5  >  54.0 |   -0.0      0 |       0       0
U4 s_capacity DC0  <   0.0 |    0.0      0 |       0       0
U4 s_capacity DC1  <   0.0 |   16.0      0 |       0       0
U4 s_capacity DC2  <   0.0 |   25.0      0 |       0       0
U4 s_capacity DC3  <   0.0 |    0.0      0 |       0       0
U4 s_capacity DC4  <   0.0 |    0.0      0 |       0       0
U4 s_capacity DC5  <   0.0 |   14.0      0 |       0       0
U4 s_capacity DC6  <   0.0 |    0.0      0 |       0       0


## == NORMAL DEMAND ANALYSIS == ##

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

## == SURGE ANALYSIS == ##

Surge multipliers
{('U0', 'S0'): 1.0, ('U1', 'S0'): 1.0, ('U2', 'S0'): 1.0555555555555556, ('U3', 'S0'): 1.0, ('U4', 'S0'): 1.0, ('U0', 'S1'): 1.0, ('U1', 'S1'): 1.0, ('U2', 'S1'): 1.0, ('U3', 'S1'): 1.0, ('U4', 'S1'): 1.0, ('U0', 'S2'): 1.0, ('U1', 'S2'): 1.0, ('U2', 'S2'): 1.0, ('U3', 'S2'): 1.0, ('U4', 'S2'): 1.0, ('U0', 'S3'): 1.9333333333333333, ('U1', 'S3'): 1.0, ('U2', 'S3'): 1.0, ('U3', 'S3'): 1.0, ('U4', 'S3'): 1.0, ('U0', 'S4'): 1.0, ('U1', 'S4'): 1.0, ('U2', 'S4'): 1.0, ('U3', 'S4'): 1.0, ('U4', 'S4'): 1.2352941176470589, ('U0', 'S5'): 1.0, ('U1', 'S5'): 1.0, ('U2', 'S5'): 1.0, ('U3', 'S5'): 1.0, ('U4', 'S5'): 5.4, ('U0', 'S6'): 1.0, ('U1', 'S6'): 1.0, ('U2', 'S6'): 1.0, ('U3', 'S6'): 1.0, ('U4', 'S6'): 1.0, ('U0', 'S7'): 1.0, ('U1', 'S7'): 3.875, ('U2', 'S7'): 1.0, ('U3', 'S7'): 1.0, ('U4', 'S7'): 1.0, ('U0', 'S8'): 1.0, ('U1', 'S8'): 1.0, ('U2', 'S8'): 1.0, ('U3', 'S8'): 4.285714285714286, ('U4', 'S8'): 1.0, ('U0', 'S9'): 1.0, ('U1', 'S9'): 1.0, ('U2', 'S9'): 1.0, ('U3', 'S9'): 1.0, ('U4', 'S9'): 1.0}

### Surge U0
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
Cost (weekly, no labour): 150128.0

### Surge U1
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
Cost (weekly, no labour): 153633.0

### Surge U2
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
Cost (weekly, no labour): 142088.0

### Surge U3
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
Cost (weekly, no labour): 164098.0

### Surge U4
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
Cost (weekly, no labour): 258664.0

## == STORE ASSIGNMENTS == ##
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

Store & DC0 & DC1 & DC2 & DC3 & DC4 & DC5 & DC6 \\
S0 &  &  &  & 100.0% &  &  &  \\
S1 &  &  &  & 100.0% &  &  &  \\
S2 &  &  &  & 100.0% &  &  &  \\
S3 &  &  &  &  &  & 100.0% &  \\
S4 &  &  &  & 100.0% &  &  &  \\
S5 &  & 100.0% &  &  &  &  &  \\
S6 &  & 100.0% &  &  &  &  &  \\
S7 &  &  & 100.0% &  &  &  &  \\
S8 &  &  & 100.0% &  &  &  &  \\
S9 &  &  &  & 100.0% &  &  &  \\

This was communication 7 with value 140776.0
