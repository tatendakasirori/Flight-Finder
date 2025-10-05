class FlightData:
    #This class is responsible for structuring the flight data.
    #Takes the iataCode_flights dict from flight_search and filters the flights accoding to price
    def __init__(self,citydata_dict:dict):
        self.citydata_dict = citydata_dict

    def flight_filter(jsons_list:list):
        pass

    def filter_by_price(jsons_list:list):
        filtered_json_list = {}
        for ()
        for json_file in jsons_list:
            for flight in json_file['data']: #loop over flights in data list
                if flight['price']['base'] <= lowestprice:
                    filtered_json_list.append(flight)
        return filtered_json_list



