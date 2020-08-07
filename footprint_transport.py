# COMP 202 A1: Part 3
# Footprint of local transportation and travel
# Author: Ye Yuan
#Student ID:260921269

import doctest
from unit_conversion import *

INCOMPLETE = -1


################################################


def fp_from_driving(annual_km_driven):
    '''
    (num) -> flt
    Approximate CO2E footprint for one year of driving, based on total km driven.
    Result in metric tonnes.
    Source: https://www.forbes.com/2008/04/15/green-carbon-living-forbeslife-cx_ls_0415carbon.html#1f3715d01852
    "D.) Multiply total yearly mileage by .79 (for pounds)"

    >>> fp_from_driving(0)
    0.0
    >>> round(fp_from_driving(100), 4)
    0.0223
    >>> round(fp_from_driving(1234), 4)
    0.2748
    '''
    annual_miles_driven=km_to_miles(annual_km_driven)#by calling the conversion function to change the unit from km to miles
    annual_driven_in_pound=annual_miles_driven*0.79#multiply the value of miles with 0.79 pounds per mile
    annual_driven_in_kg=pound_to_kg(annual_driven_in_pound)#by calling the conversion function to change the unit from pound to kilograms
    annual_driven_in_tonnes=kg_to_tonnes(annual_driven_in_kg)#by calling the conversion function to change the unit from kilograms to tonnes
    return annual_driven_in_tonnes#return the value of annual_driven_in_tonnes


def fp_from_taxi_uber(weekly_uber_rides):
    '''(num) -> flt
    Estimate in metric tonnes of CO2E the annual footprint from a given
    number of weekly uber/taxi/etc rides.

    Source: https://www.mapc.org/resource-library/the-growing-carbon-footprint-of-ride-hailing-in-massachusetts/
        81 million trips -> 100,000 metric tonnes

    >>> fp_from_taxi_uber(0)
    0.0
    >>> round(fp_from_taxi_uber(10), 4)
    0.6442
    >>> round(fp_from_taxi_uber(25), 4)
    1.6104
    '''
    annual_uber_rides=weekly_to_annual(weekly_uber_rides)#by calling the conversion function to change the weekly rides value to annual rides value
    proportion_to_81million=annual_uber_rides/81000000#since to 81million rides=100000tonnes CO2E, so calculate the proportion of annual rides to 81million
    annual_uber_in_tonnes=proportion_to_81million*100000#then multiply the proportion value with 10000tonnes per 81million rides
    return annual_uber_in_tonnes#then return the value of annual_uber_in_tonnes


def fp_from_transit(weekly_bus_trips, weekly_rail_trips):
    '''
    (num, num) -> flt
    Annual CO2E tonnes from public transit based on number of weekly bus
    rides and weekly rail (metro/commuter train) rides.

    Source: https://en.wikipedia.org/wiki/Transportation_in_Montreal
    The average amount of time people spend commuting with public transit in Montreal, for example to and from work, on a weekday is 87 min. 29.% of public transit riders, ride for more than 2 hours every day. The average amount of time people wait at a stop or station for public transit is 14 min, while 17% of riders wait for over 20 minutes on average every day. The average distance people usually ride in a single trip with public transit is 7.7 km, while 17% travel for over 12 km in a single direction.[28]
    Source: https://en.wikipedia.org/wiki/Société_de_transport_de_Montréal
    As of 2011, the average daily ridership is 2,524,500 passengers: 1,403,700 by bus, 1,111,700 by rapid transit and 9,200 by paratransit service.

    Source: How Bad Are Bananas
        A mile by bus: 150g CO2E
        A mile by subway train: 160g CO2E for London Underground

    >>> fp_from_transit(0, 0)
    0.0
    >>> round(fp_from_transit(1, 0), 4)
    0.0374
    >>> round(fp_from_transit(0, 1), 4)
    0.0399
    >>> round(fp_from_transit(10, 2), 4)
    0.4544
    '''
    annual_bus_trips=weekly_to_annual(weekly_bus_trips)#by calling the conversion function to change the weekly value of bus trips to annual value
    annual_bus_in_km=annual_bus_trips*7.7#multiply the annual rides with 7.7km average per trip
    annual_bus_in_miles=km_to_miles(annual_bus_in_km)#by calling the conversion function to change the unit from km to miles
    annual_bus_in_kg=annual_bus_in_miles*150/1000#since to 150g CO2E per miles, so multiply the value of miles with 150, then divide 1000 to change the unit from grams to kilograms
    annual_bus_in_tonnes=kg_to_tonnes(annual_bus_in_kg)#by calling the conversion functionto change the unit from kilograms to tonnes
    annual_rail_trips=weekly_to_annual(weekly_rail_trips)#the same reason for rail part
    annual_rail_in_km=annual_rail_trips*7.7
    annual_rail_in_miles=km_to_miles(annual_rail_in_km)
    annual_rail_in_kg=annual_rail_in_miles*160/1000
    annual_rail_in_tonnes=kg_to_tonnes(annual_rail_in_kg)
    annual_transit_in_tonnes=annual_bus_in_tonnes+annual_rail_in_tonnes#then we add the part of bus and the part of rail
    return annual_transit_in_tonnes#return the value of annual_transit_in_tonnes(the sum of those two parts)


def fp_of_transportation(weekly_bus_rides, weekly_rail_rides, weekly_uber_rides, weekly_km_driven):
    '''(num, num, num, num) -> flt
    Estimate in tonnes of CO2E the footprint of weekly transportation given
    specified annual footprint in tonnes of CO2E from diet.

    >>> fp_of_transportation(0, 0, 0, 0)
    0.0
    >>> round(fp_of_transportation(2, 2, 1, 10), 4)
    0.3354
    >>> round(fp_of_transportation(1, 2, 3, 4), 4)
    0.3571
    '''
    transit=fp_from_transit(weekly_bus_rides,weekly_rail_rides)#by calling the existed function fp_from_transit to calculate the annual CO2E of bus and rail rides
    uber=fp_from_taxi_uber(weekly_uber_rides)#by calling the existed function fp_from_taxi_uber to calculate the annual CO2E of uber rides
    driving_in_annual=weekly_to_annual(weekly_km_driven)#since to the input value of driving km is weekly value, so call the conversion function first to change it to annual value
    driving=fp_from_driving(driving_in_annual)#by calling the existed function fp_from_driving to calculate the annual CO2E of driving kilometers
    total_transportation=transit+uber+driving#then sum the three parts
    return total_transportation#return the value of total


#################################################

# You might want to put helper functions here :)
#seperate the fifth function to 5 specific functions(helper functions)
def short_flight(annual_short_flights):#create a function to calculate the CO2E of short flights
    '''(num) -> flt
    Estimate in metric tonnes of CO2E the footprint of anuual short flights
    the number of short flights is given as argument
    source:we estimate each flight shorter than 4hrs emit 1100lbs CO2E
    >>> round(short_flight(0), 4)
    0.0
    >>> round(short_flight(2), 4)
    0.9979
    >>> round(short_flight(5), 4)
    2.4948
    '''
    short_flight_in_lbs=annual_short_flights*1100#since 1100lbs per short flight, so multiply the value of short flights with 1100
    short_flight_in_kg=pound_to_kg(short_flight_in_lbs)#by calling the conversion function to change the unit from pounds to kilograms
    short_flight_in_tonnes=kg_to_tonnes(short_flight_in_kg)#by calling the conversion function to change the unit from kilograms to tonnes
    return short_flight_in_tonnes#return the value of short_flight_in_tonnes

def long_flight(annual_long_flights):#for the same reasons as the short_flight function above
    '''(num) -> flt
    Estimate in metric tonnes of CO2E the footprint of anuual long flights
    the number of long flights is given as argument
    source:we estimate each flight longer than 4hrs emit 4400lbs CO2E
    >>> round(long_flight(0), 4)
    0.0
    >>> round(long_flight(2), 4)
    3.9916
    >>> round(long_flight(5), 4)
    9.979
    '''
    long_flight_in_lbs=annual_long_flights*4400
    long_flight_in_kg=pound_to_kg(long_flight_in_lbs)
    long_flight_in_tonnes=kg_to_tonnes(long_flight_in_kg)
    return long_flight_in_tonnes

def train_ride(annual_train_rides):#create a function to calculate the CO2E of train rides
    '''(num) -> flt
    Estimate in metric tonnes of CO2E the footprint of anuual train rides
    the number of train rides is given as argument
    source:we estimate each train ride emit 34.45kg CO2E
    >>> round(train_ride(0), 4)
    0.0
    >>> round(train_ride(2), 4)
    0.0689
    >>> round(train_ride(35), 4)
    1.2058
    '''
    train_ride_in_kg=annual_train_rides*34.45#since to 34.45kilograms per train ride, so multiply the value of annual train rides with 34.45
    train_ride_in_tonnes=kg_to_tonnes(train_ride_in_kg)#by calling the conversion function to change the unit from kilograms to tonnes
    return train_ride_in_tonnes#return the value of train_ride_in_tonnes

def bus_ride(annual_coach_bus_rides):#for the same reason as the train_ride above
    '''(num) -> flt
    Estimate in metric tonnes of CO2E the footprint of anuual coach bus rides
    the number of coach bus rides is given as argument
    source:we estimate each coach bus ride emit 33kg CO2E
    >>> round(bus_ride(0), 4)
    0.0
    >>> round(bus_ride(2), 4)
    0.066
    >>> round(bus_ride(35), 4)
    1.155
    '''
    bus_ride_in_kg=annual_coach_bus_rides*33#since 33kilograms per coach bus ride, so multiply the value of annual_coach_bus_rides with 33
    bus_ride_in_tonnes=kg_to_tonnes(bus_ride_in_kg)
    return bus_ride_in_tonnes

def hotel_stay(annual_dollars_on_hotel_stay):#create a new function to calculate the CO2E of hotel_stay
    '''(num) -> flt
    Estimate in metric tonnes of CO2E the footprint of anuual expense on hotel stay
    the amount of expense in dollor is given as argument
    source:we estimate each dollar expended in hotel stay emit 270 grams CO2E
    >>> round(hotel_stay(0), 4)
    0.0
    >>> round(hotel_stay(2222), 4)
    0.5999
    >>> round(hotel_stay(9876), 4)
    2.6665
    '''
    hotel_stay_in_kg=annual_dollars_on_hotel_stay*270/1000#since to 270grams per dollars, so multiply the value of total dollars with 270, then divide 1000 to change the unit from grams to kilograms
    hotel_stay_in_tonnes=kg_to_tonnes(hotel_stay_in_kg)#by calling the conversion function to change the unit from kg to tonnes
    return hotel_stay_in_tonnes#return the value of hotel_stay_in_tonnes

#################################################

def fp_of_travel(annual_long_flights, annual_short_flights, annual_train, annual_coach, annual_hotels):
    '''(num, num, num, num, num) -> float
    Approximate CO2E footprint in metric tonnes for annual travel, based on number of long flights (>4 h), short flights (<4), intercity train rides, intercity coach bus rides, and spending at hotels.

    Source for flights: https://www.forbes.com/2008/04/15/green-carbon-living-forbeslife-cx_ls_0415carbon.html#1f3715d01852 --- in lbs
    "E.) Multiply the number of flights--4 hours or less--by 1,100 lbs
    F.) Multiply the number of flights--4 hours or more--by 4,400 libs"

    Source for trains: https://media.viarail.ca/sites/default/files/publications/SustainableMobilityReport2016_EN_FINAL.pdf
    137,007 tCO2E from all of Via Rail, 3974000 riders
        -> 34.45 kg CO2E

    Source for buses: How Bad Are Bananas
        66kg CO2E for ROUND TRIP coach bus ride from NYC to Niagara Falls
        I'm going to just assume that's an average length trip, because better data not readily avialible.

    Source for hotels: How Bad Are Bananas
        270 g CO2E for every dollar spent

    >>> fp_of_travel(0, 0, 0, 0, 0)
    0.0
    >>> round(fp_of_travel(0, 1, 0, 0, 0), 4) # short flight
    0.499
    >>> round(fp_of_travel(1, 0, 0, 0, 0), 4) # long flight
    1.9958
    >>> round(fp_of_travel(2, 2, 0, 0, 0), 4) # some flights
    4.9895
    >>> round(fp_of_travel(0, 0, 1, 0, 0), 4) # train
    0.0345
    >>> round(fp_of_travel(0, 0, 0, 1, 0), 4) # bus
    0.033
    >>> round(fp_of_travel(0, 0, 0, 0, 100), 4) # hotel
    0.027
    >>> round(fp_of_travel(6, 4, 24, 2, 2000), 4) # together
    15.4034
    >>> round(fp_of_travel(1, 2, 3, 4, 5), 4) # together
    3.2304
    '''
    short=short_flight(annual_short_flights)#use created function short_flight above to calculate the CO2E of short flights and create a new variable to store the value
    long=long_flight(annual_long_flights)#for the same reason
    train=train_ride(annual_train)#for the same reason
    bus=bus_ride(annual_coach)#for the same reason
    hotel=hotel_stay(annual_hotels)#for the same reason
    total_travel=short+long+train+bus+hotel#then sum up the five seperate parts
    return total_travel#return the total value

#################################################

if __name__ == '__main__':
    doctest.testmod()
