class FlightData:
    #This class is responsible for structuring the flight data.
    #Takes the iataCode_flights dict from flight_search and filters the flights accoding to price
    def __init__(self,citydata_dict:dict):
        print('Flightdata object initiated')
        self.citydata_dict = citydata_dict

    def flights_summary(self,iataCode_flights:dict):
        '''Creats a concise summary of found cheap flights and returns them
        in the form [{source:__,
        destination:___,
        departure:___,
        arrival:___
        }
        ] for notification_manager'''
        filtered_flights_list = self.filter_by_price(iataCode_flights)# filter first
        print("Summarizing flights")
        flight_summary = []
        for flight_dict in filtered_flights_list:
            flight_description = {}
            flight_description['source'] = flight_dict['itineraries'][0]['segments'][0]['departure']

    def filter_by_price(self,iataCode_flights:dict):
        print('filtering by price')
        filtered_flights = [] # collect filtered iataCode_flights 
        for iata_price in self.citydata_dict.values():
            for json_file in iataCode_flights.get(iata_price[0],{}):
                for flight in json_file['data']: #loop over flights in data list
                    print('price is : ' + str(float(flight.get('price',{}).get('base',float('inf')))))
                    if float(flight.get('price',{}).get('total',float('inf'))) <= iata_price[1]:
                        filtered_flights.append(flight) #adding each cheap flight
                        print('Cheap flight!')
                    else:
                        print('Too expensive')
        print('Flight data filtered!!!')
        return filtered_flights



