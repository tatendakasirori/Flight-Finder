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
        filtered_json_list = self.filter_by_price(iataCode_flights)# filter first
        print("Summarizing flights")
        flight_summary = []
        for json_file in filtered_json_list:
            flight_discription = {}
            flight_discription['source'] = json_file.get('data')[0]

    def filter_by_price(self,iataCode_flights:dict):
        print('filtering by price')
        filtered_json_list = [] # collect filtered iataCode_flights 
        for city,iata_price in self.citydata_dict.items():
            for json_file in iataCode_flights.get(iata_price[0],{}):
                for flight in json_file['data']: #loop over flights in data list
                    print('price is : ' + float(flight.get('price',{}).get('base',float('inf'))))
                    if float(flight.get('price',{}).get('base',float('inf'))) <= iata_price[1]:
                        filtered_json_list.append(flight) #adding each cheap flight 
                    else:
                        print('Too expensive')
        print('Flight data filtered!!!')
        return filtered_json_list



