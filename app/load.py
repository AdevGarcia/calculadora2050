import os
import time
from dotenv import load_dotenv

from loader.util import Upload


if __name__ == "__main__":
    
    load_dotenv()
    env       = os.getenv("API_ENV")
    host      = os.getenv("SERVER_HOST", "http://localhost")
    port      = os.getenv("SERVER_PORT", 8000)
    api       = os.getenv("API_V1_STR", "/api/v1")
    user      = os.getenv('ADMIN', 'admin@calculadora2050.com')
    password  = os.getenv('ADMIN_PASSWORD', 'password')

    time0 = time.time()

    collection_path = 'app/loader/Calculadora2050.postman_collection.json'

    if env == 'production':
        u = Upload(collection_path=collection_path, url=f'{host}:{port}{api}', user=user, password=password)
    else:
        u = Upload(collection_path=collection_path, url=f'{host}:{port}{api}', debug=True)
    connect = u.test_connection()

    if connect:
        print('\n------- DELETE -------\n')
        init = time.time()
        u.delete_all()
        print(f'DELETE:   {time.time() - init:.2f} s')

        print('\n------- POST -------\n')
        init = time.time()
        u.post_all()
        print(f'POST:   {time.time() - init:.2f} s')
        
        print('\n------- GET -------\n')
        init = time.time()
        u.get_all()
        print(f'GET:   {time.time() - init:.2f} s')

    print(f'Total:   {time.time() - time0:.2f} s')