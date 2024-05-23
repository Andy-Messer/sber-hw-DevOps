import requests
import time

url = 'http://my-app:8000/statistics'
output_file = 'data/logstats.txt'

def log_stat():
    
    try:
        response = requests.get(url)
        print(response.status_code)
        print(response)
        if response.status_code == 200:
            with open(output_file, 'a') as f:
                print(str(response.json()['statistics']))
                f.write(str(response.json()['statistics']) + '\n')
        else:
            print('Bad endpoint :(')
    except:
        print(f'Bedi with Internet connection: {url}')
        
log_stat()
