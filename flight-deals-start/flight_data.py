class FlightData:
    #This class is responsible for structuring the flight data.
    #Takes the iataCode_flights dict from flight_search and filters the flights accoding to price
    def __init__(self,citydata_dict:dict):
        print('Flightdata object initiated')
        self.citydata_dict = citydata_dict

    def flight_filter(self,jsons_list:list):
        pass

    def filter_by_price(self,iataCode_flights:dict):
        print('filtering by price')
        filtered_json_dict = {} # collect filtered iataCode_flights 
        for city,iata_price in self.citydata_dict.items():
            filtered_json_list = [] #stores filtered json_lists for each city
            for json_file in iataCode_flights.get(iata_price[0],{}):
                print(f'this is jsonfile for {city}')
                for flight in json_file['data']: #loop over flights in data list
                    if float(flight.get('price',{}).get('base',float('inf'))) <= iata_price[1]:
                        filtered_json_list.append(flight) #adding each cheap flight 
                    else:
                        print('Too expensive')
            filtered_json_dict[city] = filtered_json_list # making city: [flight_jsons] dict
        print('Flight data filtered!!!')
        return filtered_json_list



