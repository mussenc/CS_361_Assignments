from argparse import ArgumentParser, Namespace
import requests
import json

with open('./constants/electricRates.json') as f:
    electricRateData = json.load(f)

with open('./constants/federalIncentives.json') as f:
    federalIncentivesData = json.load(f)

with open('./constants/greenEnergyType.json') as f:
    greenEnergyType = json.load(f)


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

    # create the subparser for the "financialIncentives" command
    parser_financialIncentives = subparsers.add_parser('financialIncentives', help='Returns a federal incentives for green energy')
    parser_financialIncentives.set_defaults(func=financialIncentives)
    parser_financialIncentives.add_argument("-v", "--verbose", help="Provides a verbose description", action='store_true')

    # create the subparser for the "solarPaybackPeriod" command
    parser_solarPaybackPeriod = subparsers.add_parser('solarPaybackPeriod', help='Returns the number of months to cover the cost of a solar purchase')
    parser_solarPaybackPeriod.set_defaults(func=solarPaybackPeriod)
    parser_solarPaybackPeriod.add_argument('cost', type=float, help='provide the cost of a solar product')
    parser_solarPaybackPeriod.add_argument('hours', type=int, help='provide amount of peak sun hours a day, typically 3-7')
    parser_solarPaybackPeriod.add_argument('electricRate', type=float, help='provide a electric rate, use electricRate command to find one')
    parser_solarPaybackPeriod.add_argument('power', type=int, help='provide a systems power (Watts), use homeProductOptions command to find one')
    parser_solarPaybackPeriod.add_argument("-v", "--verbose", help="Provides a verbose description", action='store_true')

    # create the subparser for the "solarPowerCostRatioPayback" command
    parser_solarPowerCostRatioPayback = subparsers.add_parser('solarPowerCostRatioPayback', help='Returns the ratio of cost/power needed to maintain a payback period')
    parser_solarPowerCostRatioPayback.set_defaults(func=solarPowerCostRatioPayback)
    parser_solarPowerCostRatioPayback.add_argument('hours', type=int, help='provide amount of peak sun hours a day, typically 3-7')
    parser_solarPowerCostRatioPayback.add_argument('electricRate', type=float, help='provide a electric rate, use electricRate command to find one')
    parser_solarPowerCostRatioPayback.add_argument('months', type=int, help='The max number of months the user will not be paid back')
    parser_solarPowerCostRatioPayback.add_argument("-v", "--verbose", help="Provides a verbose description", action='store_true')

    # create the subparser for the "energyTypes" command
    parser_energyTypes = subparsers.add_parser('energyTypes', help='Returns the energy types supported in this CLI')
    parser_energyTypes.set_defaults(func=energyTypes)
    parser_energyTypes.add_argument("-v", "--verbose", help="Provides a verbose description", action='store_true')

    # use provided commands and arguments
    args = parser.parse_args()
    args.func(args)

def electricRate(args):
    '''Function used to return the average electric rate in a specified US State'''
    
    rate = electricRateData[args.state]
    if args.verbose:
        print(f"The average electric rate for {args.state} is {rate} $/kWh")
    else:
        print(f"{rate}")
    return rate

    
def homeElectricCost(args):
    '''Function used to return the electric cost for a home'''
    
    low_use_sf = .5 
    high_use_sf = 1
    low_cost = round((args.electricRate * low_use_sf * args.homeSize) ,2) 
    high_cost = round((args.electricRate * high_use_sf * args.homeSize) ,2) 

    if args.verbose:
        print(f"The electrical cost for a {args.homeSize} SF house is ${low_cost} to ${high_cost}")
    else:
        print((low_cost + high_cost) / 2)
    return (low_cost + high_cost) / 2


def homeSize(args):
    '''Function used to return the SF of a home'''
    sf = args.width * args.length * args.floors

    if args.verbose:
        print(f"The house is {sf} SF")
    else:
        print(f"{sf}")
    return sf


def greenEnergyTypes(args):
    '''Function used to return the greenEnergyTypes supported in this program'''
    energy_types = ["wind", "solar"] 

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

def financialIncentives(args):
    '''Function used to share current federal incentives for purchasing green energy'''
    if args.verbose:
        print(f"The federal incentives in the US are currently...\n {federalIncentivesData}")
    else:
        print(json.dumps(federalIncentivesData, indent=2))
    return federalIncentivesData

def solarPaybackPeriod(args):
    '''Function used to calculate the month of months it will take for a solar product to payback it's cost'''
    power_generated = args.power * args.hours * 30
    power_generated_cost = power_generated * args.electricRate
    periods = (args.cost * 1000) // power_generated_cost
    if args.verbose:
        print(f"THe purchase will take {periods} months to pay back")
    else:
        print(periods)
    return periods

def solarPowerCostRatioPayback(args):
    '''Function used to display the cost/power ratio needed '''
    c_p = args.months * args.hours * 30 * args.electricRate / 1000
    if args.verbose:
        print(f"The cost must be less than {c_p} times the power rating")
    else:
        print(c_p)
    return c_p

def energyTypes(args):
    if args.verbose:
        print(f"The energy types supported in this app...\n {greenEnergyType}")
    else:
        print(json.dumps(greenEnergyType, indent=2))
    return greenEnergyType


if __name__ == '__main__':
    main()
