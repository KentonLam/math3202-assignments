from assignment_dp import *

from sys import exit


print_fridges = lambda l: print(f'  A={l[0]}, E={l[1]}, L={l[2]}')
print_dollars = lambda l: print(f'  A=${l[0]}, E=${l[1]}, L=${l[2]}')


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
    n = comm
    # print(f'| Enter how many fridges you have stored at the start of each week')
    # print(f'| as space-separated numbers a e l.')
    # print(f'| Example: >>> 0 0 0 for no fridges.')
    # print()

    

    cur_profit = 0
    cur_fridges = (0, 0, 0)
    w = 1
    while True:
        
        print()
        # user_input = ask_input(
        #     lambda x: len(x) == 3, 
        #     lambda s: list(map(int, s.split())), 
        #     "| Enter space-separated numbers: a e l.")
        sol = ( (V2, V3)[comm-2] )(w-1, *cur_fridges)
        
        print('============'*2)
        print('Week', w)
        print()
        print('Expected total profit: $', round(sol[0]+cur_profit, 2), sep='')
        print('  Current profit: $', round(cur_profit, 2), sep='')
        print('  Expected future profit: $', round(sol[0], 2), sep='')
        print()
        print('Optimal fridges to buy:')
        print_fridges(sol[1:])
        print()
        
        new_store_cost = StoreCost*sum(sol[1:])
        old_store_cost = StoreCost*sum(cur_fridges)
        print(f'Week storage cost: ${new_store_cost+old_store_cost}')
        print(f'  Currently stored: ${old_store_cost}')
        print(f'  Newly bought: ${new_store_cost}')
        cur_fridges = [x+y for x, y in zip(cur_fridges, sol[1:])]

        print()
        print('Available fridges: ')
        print_fridges(cur_fridges)
        print()
        print(f'| Enter actual sales in week {w} as')
        print(f'| space-separated numbers a e l.')
        sales = ask_input(
            lambda x: len(x) == 3 and all(m>= y >= 0 for m, y in zip(cur_fridges, x)), 
            lambda s: list(map(int, s.split())), 
            "| Enter space-separated numbers: a e l.\n| Cannot exceed available fridges.")
        profit = [Profits[i]*x for i, x in enumerate(sales)]
        
        print(f'Profit in week {w}: ${sum(profit)}')
        print_dollars(profit)
        cur_fridges = [x-y for x, y in zip(cur_fridges, sales)]
        cur_profit += sum(profit)
        print(f'Cumulative profit: ${cur_profit}')
        print()
        print('Leftover fridges:')
        print_fridges(cur_fridges)
        w += 1
        if w >= 5:
            break 
        input('Press enter to compute next week...')
    print()
    print('4 weeks elapsed.')
    print(f'TOTAL PROFIT: ${cur_profit}')

if __name__ == "__main__":
    explorer()