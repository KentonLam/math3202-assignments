from assignment_dp import *

from sys import exit

def print_solution(x, a, e, l):
    print('Expected profit: $', round(x, 2), sep='')
    print()
    print('Optimal fridges to buy:')
    print('  Alaska:', a)
    print('  Elsa:', e)
    print('  Lumi:', e)

def ask_input(valid, map_, help_str=None):
    while True:
        try:
            params = input('>>> ').strip()
        except (KeyboardInterrupt, EOFError):
            print('\nExiting.')
            exit()
        try:
            if valid(map_(params)):
                return map_(params)
            else:
                raise ValueError(help_str or "Invalid input.")
        except Exception as e:
            print(help_str or e)

def explorer():
    print('Solution Explorer')
    print('=================')
    print('Select communication 2 or 3: ')
    comm = ask_input(lambda i: i in (2, 3), int, "Enter 2 or 3.")
        
    print('Exploring communication', comm)
    print()
    n = comm
    print(f'Enter space separated parameters to V(t, a, e, l).')
    print('t = week, a = Alaska, e = Elsa, l = Lumi.')
    print('a, e and l are the number stored at the start of week t.')
    print('Weeks start at 0. Example: >>> 3 0 0 0')
    print()
    cur_profit = 0
    while True:
        print(f'Current profit: ${cur_profit}')
        user_input = ask_input(
            lambda x: len(x) == 4, 
            lambda s: list(map(int, s.split())), 
            "Enter space-separated numbers: t a e l.")
        w = user_input[0]
        sol = ( (V2, V3)[comm-2] )(*user_input)
        print('Week', user_input[0])
        print()
        print_solution(*sol)
        print()
        if user_input[0] >= 4:
            print('End of trial.')
        else:
            new_store_cost = StoreCost*sum(sol[1:])
            old_store_cost = StoreCost*sum(user_input[1:])
            print(f'Total storage cost: ${new_store_cost+old_store_cost}')
            print(f'  Currently stored: ${old_store_cost}')
            print(f'  Newly bought: ${new_store_cost}')

        print()
        print(f'Enter actual sales in week {w} as')
        print(f'space-separated numbers a e l.')
        sales = ask_input(
            lambda x: len(x) == 3 and all(y >= 0 for y in x), 
            lambda s: list(map(int, s.split())), 
            "Enter space-separated numbers: a e l.")
        profit = [Profits[i]*x for i, x in enumerate(sales)]
        
        print(f'Actual weekly profit: ${sum(profit)}')
        print(f'  Alaska: ${profit[0]}')
        print(f'  Elsa: ${profit[1]}')
        print(f'  Lumi: ${profit[2]}')
        cur_profit += sum(profit)

if __name__ == "__main__":
    explorer()