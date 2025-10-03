import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self,url:str,auth:str):
        self.url = url
        self.auth = auth
        self.headers = sh_headers={
        'Authorization': auth,
        "Content-Type": "application/json"
        }
        self.data = self.get_data()

    # returns all the data in the google sheet
    def get_data(self) -> dict: 
        response = requests.get(url=self.url,headers=self.headers)
        prices = response.json()
        return prices
    
    # gets a list of all cities in the sheet
    def get_cities(self) -> list: 
        '''Returns a list of all the cities in the google sheet'''
        res_dict = self.get_data()['prices']
        city_list = [i['city'] for i in res_dict]
        return city_list
    
    #writes iata codes in google sheet
    def write_iata(self,iata_list:list):
        '''Takes a list of iata_code and "PUTs" the iata_code in the google sheet.
        Prints out if this was succesful and an error code if not'''
        print('Logging iata codes......')
        for row_id in range(len(iata_list)): # loop over the row ids 
            url = self.url + f'/{row_id + 2}' #make the row url to 'PUT' the iatacode
            body ={
                "price":{
                    "iataCode": iata_list[row_id]
                }
            }
            response = requests.put(url=url,json=body,headers=self.headers)
            if response.status_code != 200:
                print(response.json())
                return
        self.data = self.get_data() # updated data
        print("Succefuly entered iata codes!!!")
    

        




