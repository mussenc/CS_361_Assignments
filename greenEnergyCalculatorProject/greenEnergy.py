from argparse import ArgumentParser, Namespace
import requests


def main():
    parser = ArgumentParser()

    subparsers = parser.add_subparsers(dest='command', help='available subcommands')

    # create the subparser for the "homeElectricCost" command
    parser_electricRate = subparsers.add_parser('homeElectricCost', help='Returns the estimated electric cost ($) for a home')
    parser_electricRate.set_defaults(func=homeElectricCost)
    parser_electricRate.add_argument('electricRate', type=float, help='provide a electric rate, use electricRate command to find one')
    parser_electricRate.add_argument('homeSize', type=int, help='provide a SF of a house, use homeSize command calculate this')
    parser_electricRate.add_argument("-v", "--verbose", help="Provides a verbose description", action='store_true')
    
    # create the subparser for the "electricRate" command
    parser_electricRate = subparsers.add_parser('electricRate', help='Returns the electric rate ($/kWh) of specified state')
    parser_electricRate.set_defaults(func=electricRate)
    parser_electricRate.add_argument('state', type=str, help='provide a 2 letter abbreviation of a US state')
    parser_electricRate.add_argument("-v", "--verbose", help="Provides a verbose description", action='store_true')

    # create the subparser for the "homeSize" command
    parser_homeSize = subparsers.add_parser('homeSize', help='Returns a calculate home size (SF)')
    parser_homeSize.set_defaults(func=homeSize)
    parser_homeSize.add_argument('width', type=int, help='provide a width (f) of a house')
    parser_homeSize.add_argument('length', type=int, help='provide a length (f) of a house')
    parser_homeSize.add_argument('floors', type=int, help='provide the number (#) of floors in a house')
    parser_homeSize.add_argument("-v", "--verbose", help="Provides a verbose description", action='store_true')

    # create the subparser for the "greenEnergyTypes" command
    parser_greenEnergyTypes = subparsers.add_parser('greenEnergyTypes', help='Returns a list of green energy types')
    parser_greenEnergyTypes.set_defaults(func=greenEnergyTypes)
    parser_greenEnergyTypes.add_argument("-v", "--verbose", help="Provides a verbose description", action='store_true')

    # create the subparser for the "homeProductOptions" command
    parser_homeProductOptions = subparsers.add_parser('homeProductOptions', help='Returns a list of green energy products')
    parser_homeProductOptions.set_defaults(func=homeProductOptions)
    parser_homeProductOptions.add_argument('type', type=str, help='provide a green energy type')
    parser_homeProductOptions.add_argument('attribute', type=str, help='provide a green energy attribute (productID, cost, power)')
    parser_homeProductOptions.add_argument('symbol', type=str, help='provide a symbol (eq, lt, gt, leq, geq)')
    parser_homeProductOptions.add_argument('value', type=str, help='provide a value')
    parser_homeProductOptions.add_argument("-v", "--verbose", help="Provides a verbose description", action='store_true')

    # use provided commands and arguments
    args = parser.parse_args()
    args.func(args)

def electricRate(args):
    '''Function used to return the average electric rate in a specified US State'''
    
    # uses microservice to provide average electric rate in a specified state
    # rate = ??? in $/kWh
    rate = .14 #place holder value
    if args.verbose:
        print(f"The average electric rate for {args.state} is {rate} $/kWh")
    else:
        print(f"{rate}")
    return rate

    
def homeElectricCost(args):
    '''Function used to return the electric cost for a home'''
    
    # uses microservice to calculate home electric cost
    # electric cost = ??? in $
    low_use_sf = .5 #place holder value
    high_use_sf = 1 #place holder value
    low_cost = round((args.electricRate * low_use_sf * args.homeSize) ,2) #place holder calculation
    high_cost = round((args.electricRate * high_use_sf * args.homeSize) ,2) #place holder calculation

    if args.verbose:
        print(f"The electrical cost for a {args.homeSize} SF house is ${low_cost} to ${high_cost}")
    else:
        print((low_cost + high_cost) / 2)
    return (low_cost + high_cost) / 2


def homeSize(args):
    '''Function used to return the SF of a home'''
    
    # uses microservice to calculate SF
    # sf = ??? in square feet
    sf = args.width * args.length * args.floors #place holder calculation

    if args.verbose:
        print(f"The house is {sf} SF")
    else:
        print(f"{sf}")
    return sf


def greenEnergyTypes(args):
    '''Function used to return the greenEnergyTypes supported in this program'''
    
    # uses microservice to return greenEnergyTypes
    # sf = ??? in square feet
    energy_types = ["wind", "solar"] #place holder calculation

    if args.verbose:
        print(f"The green energy types supported in this program are {energy_types}")
    else:
        print(f"{energy_types}")
    return energy_types

def homeProductOptions(args):
    '''Function use return the green energy productions available in this program'''
    url = f"http://flip1.engr.oregonstate.edu:6363/productsearch?greenEnergyType='{args.type}'&{args.attribute}={args.symbol}{args.value}"
    results = requests.get(url)
    print(results.text)
    return results.text

if __name__ == '__main__':
    main()
