import os
import time
from dotenv import load_dotenv

from loader.util import Upload




if __name__ == "__main__":
    
    load_dotenv()
    host      = os.getenv("SERVER_HOST") 
    api       = os.getenv("API_V1_STR")
    # user      = os.getenv('FIRST_SUPERUSER')
    # password  = os.getenv('FIRST_SUPERUSER_PASSWORD')

    url = host + api

    url='http://localhost:8000/api/v1'

    time0 = time.time()

    collection_path = 'app/loader/Calculadora2050.postman_collection.json'
    
    u = Upload(collection_path=collection_path, url=url, debug=True)
    connect = u.test_connection()

    if connect:
        print('\n####### DELETE #######\n')
        init = time.time()
        u.delete_all()
        print(f'DELETE:   {time.time() - init:.2f} s')

        print('\n####### POST #######\n')
        init = time.time()
        u.post_all()
        print(f'POST:   {time.time() - init:.2f} s')
        
        print('\n####### GET #######\n')
        init = time.time()
        u.get_all()
        print(f'GET:   {time.time() - init:.2f} s')

    print(f'Total:   {time.time() - time0:.2f} s')