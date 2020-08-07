# COMP 202 A1: Part 2
# Footprint of utilities & university
# Author: Ye Yuan
#Student ID:260921269

import doctest
from unit_conversion import *

INCOMPLETE = -1

######################################### Utilities

def fp_from_gas(monthly_gas):
    '''(num) -> float
    Calculate metric tonnes of CO2E produced annually
    based on monthly natural gas bill in $.

    Source: https://www.forbes.com/2008/04/15/green-carbon-living-forbeslife-cx_ls_0415carbon.html#1f3715d01852
        B.) Multiply your monthly gas bill by 105 [lbs, to get annual amount] 

    >>> fp_from_gas(0)
    0.0
    >>> round(fp_from_gas(100), 4)
    4.7627
    >>> round(fp_from_gas(25), 4)
    1.1907
    '''
    annually_gas_in_lbs=monthly_gas*105#multiply the input value of monthly_gas with 105lbs per dollar annually to get the annually total in lbs
    annually_gas_in_kilograms=pound_to_kg(annually_gas_in_lbs)#by calling the conversion function to transfer the pounds to kilograms
    annually_gas_in_tonnes=kg_to_tonnes(annually_gas_in_kilograms)#by calling the conversion function to transfer the kilograms to tonnes
    return annually_gas_in_tonnes#return the value of annually_gas_in_tonnes



def fp_from_hydro(daily_hydro):
    '''(num) -> float
    Calculate metric tonnes of CO2E produced annually
    based on average daily hydro usage.

    To find out your average daily hydro usage in kWh:
        Go to https://www.hydroquebec.com/portail/en/group/clientele/portrait-de-consommation
        Scroll down to "Annual total" and press "kWh"

    Source: https://www.hydroquebec.com/data/developpement-durable/pdf/co2-emissions-electricity-2017.pdf
        0.6 kg CO2E / MWh

    >>> fp_from_hydro(0)
    0.0
    >>> round(fp_from_hydro(10), 4)
    0.0022
    >>> round(fp_from_hydro(48.8), 4)
    0.0107
    '''
    annually_hydro_in_kWh=daily_to_annual(daily_hydro)#by calling the conversion function to transfer the daily value to the annual value
    annually_hydro_in_MWh=annually_hydro_in_kWh/1000#dividing the annual value in kWh by 1000 to change its unit in MWh
    annually_kg_from_hydro=annually_hydro_in_MWh*0.6#multiply the hydro value in MWh with 0.6 to get the CO2E in kilograms
    annually_tonnes_from_hydro=kg_to_tonnes(annually_kg_from_hydro)#by calling the conversion function to change the unit from kilograms to tonnes
    return annually_tonnes_from_hydro#return the value of annually_tonnes_from_hydro



def fp_of_utilities(daily_hydro, monthly_gas):
    '''(num, num, num) -> float
    Calculate metric tonnes of CO2E produced annually from
    daily hydro (in kWh) and gas bills (in $) and monthly phone data (in GB).

    >>> fp_of_utilities(0, 0)
    0.0
    >>> round(fp_of_utilities(100, 0), 4)
    0.0219
    >>> round(fp_of_utilities(0, 100), 4)
    4.7627
    >>> round(fp_of_utilities(50, 20), 4)
    0.9635
    '''
    annually_hydro=fp_from_hydro(daily_hydro)#by calling the existed function fp_from_hydro to get the annually CO2E from hydro
    annually_gas=fp_from_gas(monthly_gas)#by calling the existed function fp_from_gas  to get the annually CO2E from gas
    annually_total=annually_hydro+annually_gas#then add the above two results to get the CO2E in total
    return annually_total#return the annually_total


#################################################


def fp_of_studies(annual_uni_credits):
    '''(num, num, num) -> flt
    Return metric tonnes of CO2E from being a student, based on
    annual university credits.

    Source: https://www.mcgill.ca/facilities/files/facilities/ghg_inventory_report_2017.pdf
        1.12 tonnes per FTE (30 credit) student

    >>> round(fp_of_studies(0), 4)
    0.0
    >>> round(fp_of_studies(30), 4)
    1.12
    >>> round(fp_of_studies(18), 4)
    0.672
    '''
    value_of_FTE=annual_uni_credits/30#divide the annual_uni_credits with 30 credits to get the proportion of input value to 1 FTE
    tonnes_of_student=value_of_FTE*1.12#multiply the proportion value with 1.12 tonnes per FTE
    return tonnes_of_student#return the value of tonnes_of_student


#################################################

if __name__ == '__main__':
    doctest.testmod()
