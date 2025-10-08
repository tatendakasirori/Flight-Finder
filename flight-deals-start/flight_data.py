class FlightData:
    #This class is responsible for structuring the flight data.
    #Takes the iataCode_flights dict from flight_search and filters the flights accoding to price
    def __init__(self,citydata_dict:dict):
        self.citydata_dict = citydata_dict

    def flight_filter(self,jsons_list:list):
        pass

    def filter_by_price(self,iataCode_flights:dict):
        filtered_json_dict = {} # collect filtered iataCode_flights 
        for city,iata_price in self.citydata_dict.items():
            filtered_json_list = []
            json_file = iataCode_flights.get(iata_price[0])
            for flight in json_file['data']: #loop over flights in data list
                if float(flight['price']['base']) <= iata_price[1]:
                    filtered_json_list.append(flight)
                else:
                    print('Too expensive')
            filtered_json_dict[city] = filtered_json_list
        return filtered_json_list



