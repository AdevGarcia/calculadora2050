import os
import json
from time import sleep
import pandas as pd
import numpy as np
import httpx

from .constants import FOLDER_PATH, SECTORES, INDICE


class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKCYAN    = '\033[96m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'


def get_file_path() -> list[str]:
    l=[]
    for directory in FOLDER_PATH:
        for file in os.listdir(directory):
            l.append(os.path.join(directory, file))
    return l


def read_json(file: str) -> dict:
        """Read json file"""

        with open(f'{file}') as f:
            data = json.load(f)
        return data

#######  Read Endpoints APIRest #######

def _level0(sector: dict)-> list[dict]:
    l=[]

    for j in range(len(sector['item'])):
        bloque = sector['item'][j]

        d={
            'sector'    : 'entradas',
            'path'      : bloque['request']['url']['path'],
            'method'    : bloque['request']['method'],
            'url'       : bloque['request']['url']['raw'].replace('{{url_prefix}}', '')
        }

        l.append(d)
    return l

def _level00(sector: dict)-> list[dict]:
    l=[]

    for j in range(len(sector['item'])):
        bloque = sector['item'][j]

        for k in range(len(bloque['item'])):
            uri = bloque['item'][k]['request']

            d={
                'sector'    : sector['name'].lower(),
                'path'      : uri['url']['path'],
                'method'    : uri['method'],
                'url'       : uri['url']['raw'].replace('{{url_prefix}}', '')
            }
            
            l.append(d)
    return l


def _level1(sector: dict)-> list[dict]:
    l=[]

    for j in range(len(sector['item'])):
        bloque = sector['item'][j]

        for k in range(len(bloque['item'])):
            uri = bloque['item'][k]['request']

            d={
                'sector'    : sector['name'].lower(),
                'subsector' : sector['name'].lower(),
                'tipo'      : bloque['name'].lower().replace(' ', '_'),
                'path'      : uri['url']['path'],
                'method'    : uri['method'],
                'url'       : uri['url']['raw'].replace('{{url_prefix}}', '')
            }
            
            l.append(d)
    return l


def _level2(sector: dict)-> list[dict]:
    l=[]

    for j in range(len(sector['item'])):
        bloque = sector['item'][j]

        for k in range(len(bloque['item'])):
            uri = bloque['item'][k]

            for h in range(len(uri['item'])):
                subbloq = uri['item'][h]

                d={
                    'sector'    : sector['name'].lower(),
                    'subsector' : bloque['name'].lower().replace(' ', '_'),
                    'tipo'      : uri['name'].lower().replace(' ', '_'),
                    'path'      : subbloq['request']['url']['path'],
                    'method'    : subbloq['request']['method'],
                    'url'       : subbloq['request']['url']['raw'].replace('{{url_prefix}}', '')
                }
                
                l.append(d)
    return l


def _level3(sector: dict):
    l=[]

    for j in range(len(sector['item'])):
        bloque = sector['item'][j]

        for k in range(len(bloque['item'])):
            subbloq1 = bloque['item'][k]

            for h in range(len(subbloq1['item'])):
                subbloq2 = subbloq1['item'][h]

                for f in range(len(subbloq2['item'])):
                    subbloq3 = subbloq2['item'][f]

                    d={
                        'sector'    : sector['name'].lower(),
                        'subsector' : bloque['name'].lower().replace(' ', '_'),
                        'clase'     : subbloq1['name'].lower().replace(' ', '_'),
                        'tipo'      : subbloq2['name'].lower().replace(' ', '_'),
                        'path'      : subbloq3['request']['url']['path'],
                        'method'    : subbloq3['request']['method'],
                        'url'       : subbloq3['request']['url']['raw'].replace('{{url_prefix}}', '')
                    }
                    
                    l.append(d)
    return l


def _get_collection(file: str)-> pd.DataFrame:
    collection = read_json(file=file)
    item = collection['item']

    l, d = [], {}

    for i in range(len(item)):
        sector = item[i]

        if sector['name'].lower() in ['agricultura', 'bosques', 'ganaderia', 'industria']:
            d[sector['name'].lower()] = _level1(sector=sector)
        
        if sector['name'].lower() in ['residuos', 'electricidad', 'energia']:
            d[sector['name'].lower()] = _level2(sector=sector)

        if sector['name'].lower() in ['edificaciones', 'transporte']:
            d[sector['name'].lower()] = _level3(sector=sector)
        
        if sector['name'].lower() in ['entradas']:
            d[sector['name'].lower()] = _level0(sector=sector)
        
        if sector['name'].lower() in ['resultados']:
            d[sector['name'].lower()] = _level00(sector=sector)

    for key in d.keys():
        l.append(pd.json_normalize(d[key]))
    
    df = pd.concat(l)
    result = df[['sector', 'subsector', 'clase', 'tipo', 'path', 'method', 'url']]

    return result.replace(np.nan, '-')


def collection(df: pd.DataFrame, **args)-> pd.DataFrame:
    """get endpoint and Filter """

    size = len(args.items())

    if size==0:
        return df
    
    query = ''
    cnt = 1
    for arg in args.items():
        query +=f'{arg[0]} == "{arg[1]}"'
        cnt += 1
        if cnt <= size:
            query += ' and '

    return df.query(query)


#######  Read File Path #######

def _get_files()->pd.DataFrame:
    l=[]

    for file in get_file_path():
        # split .json & data
        a = file.split('.')[0].split('/')[2:] # 'app/data/XXXXXX.json'
        d={}

        if a[0] in ['agricultura', 'bosques', 'ganaderia', 'industria']:
            d={
                'sector'    : a[0],
                'subsector' : a[0],
                'tipo'      : a[1],
                'file'      : file
            }
        
        if a[0] in ['residuos', 'electricidad', 'energia']:
            d={
                'sector'    : a[0],
                'subsector' : a[1],
                'tipo'      : a[2],
                'file'      : file
            }
            
        
        if a[0] in ['edificaciones', 'transporte']:
            d={
                'sector'    : a[0],
                'subsector' : a[1],
                'clase'     : a[2],
                'tipo'      : a[3],
                'file'      : file
            }
        l.append(d)
    
    result = pd.DataFrame(l)[['sector', 'subsector', 'clase', 'tipo', 'file']]

    return result.replace(np.nan, '-')

def files(df: pd.DataFrame, **args)-> pd.DataFrame:
    """get files and Filter """

    size = len(args.items())

    if size==0:
        return df
    
    query = ''
    cnt = 1
    for arg in args.items():
        query +=f'{arg[0]} == "{arg[1]}"'
        cnt += 1
        if cnt <= size:
            query += ' and '

    return df.query(query)


class Upload():

    def __init__(self, collection_path: str, url :str, user: str =None, password : str=None, debug: bool=False) -> None:

        self.url         = url
        self.user        = user
        self.password    = password
        self.auth_header = None
        self.debug       = debug

        self.collection_path =collection_path
        self.indice = INDICE

        if self.user != None:
            self.auth_header = self.get_auth_header()

        if self.debug:
            print('-> url         :', self.url)
            print('-> user        :', self.user)
            print('-> password    :', self.password)
            print('-> auth_header :', self.auth_header)
    

        self.collection = _get_collection(file=self.collection_path)
        self.files      = _get_files()


    def _read_json(self, file: str) -> dict:
        """Read json file"""

        with open(f'{file}') as f:
            data = json.load(f)
        return data
    

    def _status(self, method: str, r, uri: str) -> None:
        """Status HTTP Code"""

        f = {'get'   : '[GET]',
             'post'  : '[POST]',
             'delete': '[DELETE]'}
        
        match r.status_code:
            case 200:
                print(f'{bcolors.OKGREEN}[OK] {f[method]} {r.status_code} {bcolors.ENDC}', uri, f'time : {r.elapsed.total_seconds():.2f} s')
            
            case 201:
                print(f'{bcolors.OKGREEN}[OK] {f[method]} {r.status_code }{bcolors.ENDC}', uri, f'time : {r.elapsed.total_seconds():.2f} s')
            
            case 400:
                print(f'{bcolors.WARNING}[WARNING] {f[method]} {r.status_code} {bcolors.ENDC}', uri, f'time : {r.elapsed.total_seconds():.2f} s')
                print(r.json())
            
            case 405:
                # El servidor reconoce la solicitud, pero no esta implementada
                print(f'{bcolors.WARNING}[WARNING] {f[method]} {r.status_code} {bcolors.ENDC}', uri, f'time : {r.elapsed.total_seconds():.2f} s')
                print(r.json())

            case _:
                print(f'{bcolors.FAIL}[ERROR] {f[method]} {r.status_code} {bcolors.ENDC}', uri, f'time : {r.elapsed.total_seconds():.2f} s')
                print(r.json())
    

    def get_auth_header(self) -> dict:
        """Get access_token"""

        r = httpx.post(
            url=f'{self.url}/login/access-token', 
            data={'username': f'{self.user}', 'password': f'{self.password}'}
            )
        token = r.json()

        print('[ACCESS TOKEN]', r.status_code)
        auth_header = {"Authorization": f'{token["token_type"]} {token["access_token"]}'}

        return auth_header
    

    def test_connection(self, retries: int = 30, timeout: int=5) -> bool:
        """Test connection"""

        if self.debug:
            print('Test Connection...')

        for i in range(retries):
            try:
                if self.debug:
                    print(f'Retry: {i}')

                r = httpx.get(url=f'{self.url}/test', timeout=timeout)

                if r.status_code == 200:
                    return True
                    # break

            except httpx.TimeoutException as e:
                print('TimeoutException - Retry: ', i)

            except httpx.ConnectError as e:
                print(e)
                sleep(1)
                continue

    
    def delete(self, uri: str) -> None:
        """Delete"""

        url=f'{self.url}{uri}'
        headers = self.auth_header

        if self.debug:
            print('url:  ', url)
            # if self.user != None:
            #     print('headers: ', headers)

        r = httpx.delete(url=url, headers=headers, timeout=None)

        self._status(method='delete',r=r, uri=uri)
    

    def post(self, uri: str, file: str) -> None:
        """Post"""

        url     = f'{self.url}{uri}', 
        data    = json.dumps(self._read_json(file)), 
        headers = self.auth_header

        if self.debug:
            print('url:  ', url[0])
            print('file: ', file)
            # if self.user != None:
            #     print('headers: ', headers)

        r = httpx.post(url=url[0], data=data[0], headers=headers, timeout=None)

        self._status(method='post',r=r, uri=uri)
        

    def get(self, uri: str) -> None:
        """Get"""

        url=f'{self.url}{uri}', 
        headers=self.auth_header
        
        if self.debug:
            print('url:  ', url[0])
            # if self.user != None:
            #     print('headers: ', headers)

        r = httpx.get(url=url[0], headers=headers, timeout=None)

        self._status(method='get',r=r, uri=uri)
    

    def post_all(self) -> None:
        """ Postea toda la DDBB - En localhost 6m 40s"""

        d = self.indice

        for sector in SECTORES:
            for i in range(len(d[sector])):
                item = d[sector][i]
                if self.debug:
                    print('-----------------------------------')
                    print('-> sector: ', item['sector'], '| subsector: ', item['subsector'], '| clase: ', item['clase'])
                
                df0 = collection(
                    df        = self.collection, 
                    sector    = item['sector'],
                    subsector = item['subsector'],
                    clase     = item['clase'],
                    method    = 'POST')
                
                df1 = files(
                    df        = self.files,
                    sector    = item['sector'],
                    subsector = item['subsector'],
                    clase     = item['clase'])
                
                for j in range(len(item['tipo'])):
                    r = df0[df0.tipo.str.contains(item['tipo'][j])]
                    s = df1[df1.tipo.str.contains(item['tipo_files'][j])]

                    direct = s.file.to_list()[0]
                    str1 = direct.split('.')[0].split('/')[-1]
                    str2 = direct.split('.')[0].split('/')[-1].split('_')[-1]

                    cont=True
                    lr = r.url.to_list()
                    for k in range(len(lr)):
                        if str1 in lr[k]:
                            self.post(uri=lr[k], file=direct)
                            cont=False
                            break
                    if cont:
                        for k in range(len(lr)):
                            if str2 in lr[k]:
                                self.post(uri=lr[k], file=direct)
    

    def delete_all(self) -> None:
        """ Borra toda la DDBB - En localhost 2m 30s"""

        d = self.indice

        for sector in SECTORES:
            for i in range(len(d[sector])):
                item = d[sector][i]
                if self.debug:
                    print('-----------------------------------')
                    print('-> sector: ', item['sector'], '| subsector: ', item['subsector'], '| clase: ', item['clase'])
                
                df = collection(
                    df        = self.collection, 
                    sector    = item['sector'],
                    subsector = item['subsector'],
                    clase     = item['clase'],
                    method    = 'DELETE')
                
                ltipo = [t for t in set(item['tipo'])]
                
                for j in range(len(ltipo)):
                    r = df[df.tipo.str.contains(ltipo[j])]

                    for k in range(len(r.url.to_list())):
                        self.delete(uri=r.url.to_list()[k])
    

    def get_all(self) -> None:
        """ get de toda la DDBB - En localhost 4m 30s"""

        d = self.indice

        for sector in SECTORES:
            for i in range(len(d[sector])):
                item = d[sector][i]
                if self.debug:
                    print('-----------------------------------')
                    print('-> sector: ', item['sector'], '| subsector: ', item['subsector'], '| clase: ', item['clase'])
                
                df = collection(
                    df        = self.collection, 
                    sector    = item['sector'],
                    subsector = item['subsector'],
                    clase     = item['clase'],
                    method    = 'GET')
                
                ltipo = [t for t in set(item['tipo'])]
                
                for j in range(len(ltipo)):
                    r = df[df.tipo.str.contains(ltipo[j])]

                    for k in range(len(r.url.to_list())):
                        self.get(uri=r.url.to_list()[k])
        
        print('-----------------------------------')
        print('-> sector: Entradas')
            
        df = collection(
            df        = self.collection, 
            sector    = 'entradas',
            method    = 'GET')

        for url in df.url.to_list():
            self.get(uri=url)
        
        print('-----------------------------------')
        print('-> sector: Resultados')
        
        df = collection(
            df        = self.collection, 
            sector    = 'resultados',
            method    = 'GET')

        for url in df.url.to_list():
            self.get(uri=url)
