import requests
import time

url = 'http://localhost:8000/statistics/'
output_file = 'data/logstats.txt'

def log_stat():
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(output_file, 'a') as f:
                f.write(str(response.json()['statistics']) + '\n')
        else:
            print('Bad endpoint :(')
    except:
        print('Bedi with Internet connection')
        
log_stat()
