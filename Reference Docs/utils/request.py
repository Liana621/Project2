import urllib.request
import urllib.parse
import requests


class USDA:
    
    from utils.connections import keys

    #API Key
    keys = keys()
    key = keys['value'][0]
    
    @classmethod
    def get_data(cls,query=None,key=key):
        
        get_url = 'http://quickstats.nass.usda.gov/api/api_GET/?'

        #Update query with key 
        print('Passing key to query params..')
        query_params = {'key':key}
        query_params.update(query)
        
        #API

        #Combine and encode
        querystring = urllib.parse.urlencode(query_params)
        url = get_url + querystring
        
        print(f'Connecting to {get_url}')

        #API Response
        try:
            resp = requests.get(url).json()
            print('Success!')
            
        except requests.exceptions.RequestException as e:
            print(e)

        return resp
    
    
    @classmethod
    def param_info(cls,param_name=None,key=key):
        
        get_url = 'http://quickstats.nass.usda.gov/api/get_param_values/?'
        
        param = {'key':key}
        param['param']=param_name
        
        querystring = urllib.parse.urlencode(param)
        url = get_url + querystring
        print(url)
        
        try:
            resp = requests.get(url).json()
            print('Success!')
            
        except requests.exceptions.RequestException as e:
            print(e)

        return resp
    