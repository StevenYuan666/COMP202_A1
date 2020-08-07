# COMP 202 A1: Part 4
# Footprint of computing and diet
# Author: Ye Yuan
#Student ID:260921269

import doctest
from unit_conversion import *

INCOMPLETE = -1

######################################
#create several helper functions
#seperate to 5 specific functions to help achieve the purpose of fp_of_computing
def online_use(daily_online_use):#create a new function to calculate the CO2E of daily online use
    '''(num) -> flt
    calculate and return the metric tonnes of CO2E of daily online use
    the average hours of daily online use is given as argument
    source:each hours spent on online use emits 55 grams CO2E
    >>> round(online_use(0),4)
    0.0
    >>> round(online_use(3),4)
    0.0603
    >>> round(online_use(24),4)
    0.4821
    '''
    annual_online_use=daily_to_annual(daily_online_use)#by calling the conversion function to change the daily online use duration to annual duration
    annual_online_use_in_kg=annual_online_use*55/1000#since to each hour online use emits 55g CO2E, so multiply annual duration with 55, then divide by 1000 to change the unit from g to kg
    annual_online_use_in_tonnes=kg_to_tonnes(annual_online_use_in_kg)#by calling the conversion function to change the unit from kilograms to tonnes
    return annual_online_use_in_tonnes#return the value of annual_online_use_in_tonnes

def phone_use(daily_phone_use):#create a new function to calculate the CO2E of daily phone use
    '''(num) -> flt
    calculate and return the metric tonnes of CO2E of daily phone use
    the average hours of daily phone use is given as argument
    source:each daily hour spent on phone use emits 1250 kilograms CO2E a year
    >>> round(phone_use(0),4)
    0.0
    >>> round(phone_use(4),4)
    5.0
    >>> round(phone_use(24),4)
    30.0
    '''
    annual_phone_use_in_kg=daily_phone_use*1250#since to each daily hour spent on phone use emits 1250kg a year, so multiply the daily use duration with 1250 to get the total amount of a year in kg
    annual_phone_use_in_tonnes=kg_to_tonnes(annual_phone_use_in_kg)#by calling the conversion function to change the unit from kg to tonnes
    return annual_phone_use_in_tonnes#return the value of annual_phone_use_in_tonnes

def light_devices(new_light_devices):#create a new function to calculate the CO2E of new light devics you bought
    '''(num) -> flt
    calculate and return the metric tonnes of CO2E of new light devices you bought
    the number of new light devices you bought is given as argument
    source:each new light device you bought emit 75 kg CO2E during producing process
    >>> round(light_devices(0),4)
    0.0
    >>> round(light_devices(4),4)
    0.3
    >>> round(light_devices(25),4)
    1.875
    '''
    annual_light_devices_in_kg=new_light_devices*75#since to each new light device you bought emit 75 kg CO2E, so muitiply the number of light devices you bought with 75
    annual_light_devices_in_tonnes=kg_to_tonnes(annual_light_devices_in_kg)#by calling the conversion function to change the unit from kilograms to tonnes
    return annual_light_devices_in_tonnes#return the value of annual_light_devices_in_tonnes

def medium_devices(new_medium_devices):#create a new function to calculate the CO2E of new medium devices you bought
    '''(num) -> flt
    calculate and return the metric tonnes of CO2E of new medium devices you bought
    the number of new medium devices you bought is given as argument
    source:each new medium device you bought emit 200 kg CO2E during producing process
    >>> round(medium_devices(0),4)
    0.0
    >>> round(medium_devices(4),4)
    0.8
    >>> round(medium_devices(25),4)
    5.0
    '''
    annual_medium_devices_in_kg=new_medium_devices*200#since to each new medium device emit 200kg CO2E, so multiply the number of new medium devices with 200 to get annual CO2E in kilograms
    annual_medium_devices_in_tonnes=kg_to_tonnes(annual_medium_devices_in_kg)#by calling the conversion function to change the unit from kilograms to tonnes
    return annual_medium_devices_in_tonnes#return the value of annual_medium_devices_in_tonnes

def heavy_devices(new_heavy_devices):#create a new function to calculate the CO2E of new heavy devices you bought
    '''(num) -> flt
    calculate and return the metric tonnes of CO2E of new heavy devices you bought
    the number of new heavy devices you bought is given as argument
    source:each new heavy device you bought emit 800 kg CO2E during producing process
    >>> round(heavy_devices(0),4)
    0.0
    >>> round(heavy_devices(4),4)
    3.2
    >>> round(heavy_devices(25),4)
    20.0
    '''
    annual_heavy_devices_in_kg=new_heavy_devices*800#since to each new heavy device emit 800kg CO2E, so multiply the number of new heavy devicec with 800 to get annual CO2E in kilograms
    annual_heavy_devices_in_tonnes=kg_to_tonnes(annual_heavy_devices_in_kg)#by calling the conversion function to change the unit from kilograms to tonnes
    return annual_heavy_devices_in_tonnes#return the value of annual_heavy_devices_in_tonnes
    
def fp_of_computing(daily_online_use, daily_phone_use, new_light_devices, new_medium_devices, new_heavy_devices):
    '''(num, num) -> float

    Metric tonnes of CO2E from computing, based on daily hours of online & phone use, and how many small (phone/tablet/etc) & large (laptop) & workstation devices you bought.

    Source for online use: How Bad Are Bananas
        55 g CO2E / hour

    Source for phone use: How Bad Are Bananas
        1250 kg CO2E for a year of 1 hour a day

    Source for new devices: How Bad Are Bananas
        200kg: new laptop
        800kg: new workstation
        And from: https://www.cnet.com/news/apple-iphone-x-environmental-report/
        I'm estimating 75kg: new small device

    >>> fp_of_computing(0, 0, 0, 0, 0)
    0.0
    >>> round(fp_of_computing(6, 0, 0, 0, 0), 4)
    0.1205
    >>> round(fp_of_computing(0, 1, 0, 0, 0), 4)
    1.25
    >>> fp_of_computing(0, 0, 1, 0, 0)
    0.075
    >>> fp_of_computing(0, 0, 0, 1, 0)
    0.2
    >>> fp_of_computing(0, 0, 0, 0, 1)
    0.8
    >>> round(fp_of_computing(4, 2, 2, 1, 1), 4)
    3.7304
    '''
    online=online_use(daily_online_use)#create a new variable to store the value returned by online_use function
    phone=phone_use(daily_phone_use)#for the same reason
    light=light_devices(new_light_devices)#for the same reason
    medium=medium_devices(new_medium_devices)#for the same reason
    heavy=heavy_devices(new_heavy_devices)#for the same reason
    total_of_computing=online+phone+light+medium+heavy#create a new variable to store the value of the sum of above five variable
    return total_of_computing#return the value of sum


######################################
#create several helper functions
#seperate to 5 specific functions to help achieve the purpose of fp_of_diet
def vegan_diet():#create a new function to calculate the CO2E of vegan diet
    '''() -> flt
    this function is to return the value of CO2E emited by vegan diet
    source:we assume vegan diet emit 2.89kg CO2E per day
    >>> round(vegan_diet(),4)
    1.0556
    '''
    annual_vegan_diet_in_kg=daily_to_annual(2.89)#by calling the conversion function to calculate annual CO2E produced by vegan diet
    annual_vegan_diet_in_tonnes=kg_to_tonnes(annual_vegan_diet_in_kg)#by calling the conversion function to change the unit from kilograms to tonnes
    return annual_vegan_diet_in_tonnes#return the value of annual_vegan_diet_in_tonnes

def daily_meat(daily_g_meat):#create a new function to calculate the CO2E of meat consumption
    '''(num) -> flt
    this function is to return the value of CO2E emited by meat consumption
    the value of daily meat consumption in grams is given as the argument of the function
    source:each gram of meat consumption emit 26.8 grams CO2E
    >>> round(daily_meat(0),4)
    0.0
    >>> round(daily_meat(300),4)
    2.9365
    >>> round(daily_meat(2000),4)
    19.577
    '''
    annual_g_meat=daily_to_annual(daily_g_meat)#by calling the conversion function to change the daily value of meat consumption to annual value
    annual_meat_in_kg=annual_g_meat*26.8/1000#since to each gram of meat consumption emit 26.8g, so multiply the amount of annual meat consumption with 26.8, then divide by 1000 to change the unit from g to kg
    annual_meat_in_tonnes=kg_to_tonnes(annual_meat_in_kg)#by calling the conversion function to change the unit from kilograms to tonnes
    return annual_meat_in_tonnes#return the value of annual_meat_in_tonnes

def daily_cheese(daily_g_cheese):#create a new function to calculate the CO2E of cheese consumption
    '''(num) -> flt
    this function is to return the value of CO2E emited by cheese consumption
    the value of daily cheese consumption in grams is given as the argument of the function
    source:each gram of cheese consumption emit 12 grams CO2E
    >>> round(daily_cheese(0),4)
    0.0
    >>> round(daily_cheese(300),4)
    1.3149
    >>> round(daily_cheese(2000),4)
    8.7658
    '''
    annual_g_cheese=daily_to_annual(daily_g_cheese)#by calling the conversion function to change the daily value of cheese consumption to annual value
    annual_cheese_in_kg=annual_g_cheese*12/1000#since to each gram of cheese consumption emit 12g, so multiply the annual value of cheese consumption with 12, then divide by 1000 to change the unit from g to kg
    annual_cheese_in_tonnes=kg_to_tonnes(annual_cheese_in_kg)#by calling the conversion function to change the unit from kilograms to tonnes
    return annual_cheese_in_tonnes#then return the value of annual_cheese_in_tonnes

def daily_milk(daily_L_milk):#create a new function to calculate the CO2E of milk consumption
    '''(num) -> flt
    this function is to return the value of CO2E emited by milk consumption
    the value of daily milk consumption in litres is given as the argument of the function
    source:each litre of milk consumption emit 267.7777 grams CO2E
    >>> round(daily_milk(0),4)
    0.0
    >>> round(daily_milk(1),4)
    0.0978
    >>> round(daily_milk(5),4)
    0.489
    '''
    annual_L_milk=daily_to_annual(daily_L_milk)#by calling the conversion function to change the daily value of milk consumption to annual value
    annual_milk_in_kg=annual_L_milk*267.7777/1000#since to each litre of milk consumption emit 267.7777g, so multiply the annual value of milk consumption with 267.7777g, then divide by 1000 to change the unit from g to kg
    annual_milk_in_tonnes=kg_to_tonnes(annual_milk_in_kg)#by calling the conversion function to change the unit from kilograms to tonnes
    return annual_milk_in_tonnes#return the value of annual_milk_in_tonnes

def daily_eggs(daily_num_eggs):#create a new function to calculate the CO2E of eggs consumption
    '''(num) -> flt
    this function is to return the value of CO2E emited by eggs consumption
    the value of daily eggs consumption is given as the argument of the function
    source:each egg consumption emit 300 grams CO2E
    >>> round(daily_eggs(0),4)
    0.0
    >>> round(daily_eggs(1),4)
    0.1096
    >>> round(daily_eggs(5),4)
    0.5479
    '''
    annual_num_eggs=daily_to_annual(daily_num_eggs)#by calling the conversion function to change the daily value of eggs consumption to annual value
    annual_eggs_in_kg=annual_num_eggs*300/1000#since to each egg consumption emit 300g, so multiply the annual value of egg consumption with 300, then divide by 1000 to change the unit from g to kg
    annual_eggs_in_tonnes=kg_to_tonnes(annual_eggs_in_kg)#by calling the conversion function to change the unit from kilograms to tonnes
    return annual_eggs_in_tonnes#return the value of annual_eggs_in_tonnes

def fp_of_diet(daily_g_meat, daily_g_cheese, daily_L_milk, daily_num_eggs):
    '''
    (num, num, num, num) -> flt
    Approximate annual CO2E footprint in metric tonnes, from diet, based on daily consumption of meat in grams, cheese in grams, milk in litres, and eggs.

    Based on https://link.springer.com/article/10.1007%2Fs10584-014-1169-1
    A vegan diet is 2.89 kg CO2E / day in the UK.
    I infer approximately 0.0268 kgCO2E/day per gram of meat eaten.

    This calculation misses forms of dairy that are not milk or cheese, such as ice cream, yogourt, etc.

    From How Bad Are Bananas:
        1 pint of milk (2.7 litres) -> 723 g CO2E 
                ---> 1 litre of milk: 0.2677777 kg of CO2E
        1 kg of hard cheese -> 12 kg CO2E 
                ---> 1 g cheese is 12 g CO2E -> 0.012 kg CO2E
        12 eggs -> 3.6 kg CO2E 
                ---> 0.3 kg CO2E per egg

    >>> round(fp_of_diet(0, 0, 0, 0), 4) # vegan
    1.0556
    >>> round(fp_of_diet(0, 0, 0, 1), 4) # 1 egg
    1.1651
    >>> round(fp_of_diet(0, 0, 1, 0), 4) # 1 L milk
    1.1534
    >>> round(fp_of_diet(0, 0, 1, 1), 4) # egg and milk
    1.2629
    >>> round(fp_of_diet(0, 10, 0, 0), 4) # cheeese
    1.0994
    >>> round(fp_of_diet(0, 293.52, 1, 1), 4) # egg and milk and cheese
    2.5494
    >>> round(fp_of_diet(25, 0, 0, 0), 4) # meat
    1.3003
    >>> round(fp_of_diet(25, 293.52, 1, 1), 4) 
    2.7941
    >>> round(fp_of_diet(126, 293.52, 1, 1), 4)
    3.7827
    '''
    vegan=vegan_diet()#create a new variable to store the value returned by vegan_diet()
    meat=daily_meat(daily_g_meat)#for the same reason
    cheese=daily_cheese(daily_g_cheese)#for the same reason
    milk=daily_milk(daily_L_milk)#for the same reason
    eggs=daily_eggs(daily_num_eggs)#for the same reason
    total_of_diet=vegan+meat+cheese+milk+eggs#create a new variable to store the value of sum of above five variables
    return total_of_diet#then return the value of sum


#################################################

if __name__ == '__main__':
    doctest.testmod()

