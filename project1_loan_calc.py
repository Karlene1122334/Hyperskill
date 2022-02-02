import argparse
from itertools import count
import math
import sys

# annuity 
# 1. calculation
# 2. if n of para < required, error
# parameter: n periods, pmt payment, p principal, i interest
# calc overpmt(accum ints)
parser = argparse.ArgumentParser()
parser.add_argument("--type",choices=['diff','annuity'])
parser.add_argument("--periods",type=int)
parser.add_argument("--payment",type=int)
parser.add_argument("--principal",type=int)
parser.add_argument("--interest",type=float)

args = parser.parse_args()
parameters = [args.type, args.periods, args.principal, args.payment, args.interest]

#Error check
#at least 4 parameters, and non-negativity
count = 0
for parameter in parameters:
    if parameter != None:
        count =count +1
if count != 4:
    print('Incorrect parameters: at least 4')#4 parameters are required
    sys.exit()
for parameter in parameters[1:4]:
    if parameter == None:
        pass
    elif float(parameter) < 0.00:
        print('Incorrect parameters: non neg')
        sys.exit()
#check types
if args.type not in ['annuity','diff']:
    print("Incorrect parameters: type")
    sys.exit()

#at diff: you cannot put payment because it is what calculated
if args.type == 'diff':
    if args.payment:
        print("Incorrect parameters")
        sys.exit()

# Calculator function
# annuity
if args.type == 'annuity':
    # calculate payback periods 
    if not args.periods:
        args.interest = float(args.interest)/1200
        args.periods = math.log(args.payment/(args.payment - args.interest * args.principal),1+args.interest)
        year = round(args.periods / 12)
        month = math.ceil(args.periods - year * 12)
        print('month:',month, 'year', year, 'periods', args.periods)
        if month < 0:
            year -= 1
            month += 12 
        if month == 0:
            print(f'It will take {year} {"year" if year == 1 else "years"} to repay')
        else:
            print(f'It will take {year} {"year" if year == 1 else "years"}  and {month} months to repay')
        overpayment = math.ceil(args.periods) * args.payment - args.principal
        print(f'overpayment is $ {overpayment}')

    # calculate principal
    elif not args.principal:
        args.interest = args.interest/1200
        args.principal = args.payment /(args.interest * pow(1+args.interest,args.periods) / (pow(1+args.interest,args.periods)-1))
        overpayment = args.periods * args.payment - args.principal
        print(f'principal is {args.principal} dollars')
        print(f'overpayment is $ {overpayment}')

    # calculate monthly payment
    elif not args.payment:
        args.interest = args.interest/1200
        args.payment = math.ceil(args.principal * (args.interest * pow(args.interest+1,args.periods))/(pow(args.interest+1,args.periods)-1))
        overpayment = args.periods * args.payment - args.principal
        print(f'payment annually {args.payment} dollars')
        print(f'overpayment is $ {overpayment}')
        # annuity payments 

# differeitate payment
if args.type == 'diff':
    args.interest = float(args.interest)/1200
    total = 0
    for m in range(args.periods):
        args.payment = math.ceil((args.principal/args.periods + args.interest * (args.principal - m*args.principal/args.periods)))
        total = total+args.payment
        print(f'Month {m+1} payments is $ {args.payment}')
    print(total)
    overpmt = total - args.principal
    print(f'overpayment is ${overpmt}')

    
    
            
