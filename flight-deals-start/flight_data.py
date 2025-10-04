class FlightData:
    #This class is responsible for structuring the flight data.
    #Takes the json list from flight_search and filters the flights accoding to price
    def flight_filter(jsons_list:list):
        pass
    def filter_by_price(jsons_list:list):
        filtered_json_list = []
        for json_file in jsons_list:
            for flight in json_file['data']: #loop over flights in data list
                if flight['price']['base'] <= maxprice:
                    filtered_json_list.append(flight)
        return filtered_json_list



