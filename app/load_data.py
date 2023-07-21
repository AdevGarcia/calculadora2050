import httpx
import json
import pathlib
import os
import time
from dotenv import load_dotenv


def read_json(file):
    with open(f'{DATA_PATH}{file}') as f:
        data = json.load(f)
    return data


# Get access_token
def get_auth_header(user, password):
    r = httpx.post(f'{URL}/login/access-token', data={'username': f'{user}', 'password': f'{password}'})
    token = r.json()
    print('[ACCESS TOKEN]', r.status_code) # print(token)
    auth_header = {"Authorization": f'{token["token_type"]} {token["access_token"]}'}
    return auth_header

# Delete
def delete(uri, headers):
    r = httpx.delete(url=f'{URL}{uri}', headers=headers)
    if r.status_code == 200:
        print('[DELETE]', r.status_code, uri)
    elif r.status_code == 405:
        # El servidor reconoce la solicitud, pero no esta implementada
        print('[WARNING] [DELETE]', r.status_code, uri)
        print(r.json())
    else:
        print('[ERROR] [DELETE]', r.status_code, uri)
        print(r.json())
    
# Post
def post(uri, headers):
    file = read_json(f'{uri}.json')
    data = json.dumps(file)
    r = httpx.post(url=f'{URL}{uri}', data=data, headers=headers)
    if r.status_code == 201:
        print('[POST]', r.status_code, uri)
    elif r.status_code == 400:
        print('[WARNING] [POST]', r.status_code, uri)
        print(r.json())
    elif r.status_code == 405:
        # El servidor reconoce la solicitud, pero no esta implementada
        print('[WARNING] [POST]', r.status_code, uri)
        print(r.json())
    else:
        print('[ERROR] [POST]', r.status_code, uri)
        print(r.json())
    
# Get
def get(uri, headers):
    r = httpx.get(url=f'{URL}{uri}?skip=0&limit=100', headers=headers)
    if r.status_code == 200:
        print('[GET]', r.status_code, uri)
    else:
        print('[ERROR] [GET]', r.status_code, uri)
        print(r.json())

    

rutas=[
    # Agricultura
    'agricultura/supuestos_trayectoria.json',
    'agricultura/supuestos_fijos.json',
    'agricultura/salidas.json',
    'agricultura/emisiones.json',
    # Bosques
    'bosques/supuestos_trayectoria.json',
    'bosques/supuestos_fijos.json',
    'bosques/salidas.json',
    'bosques/emisiones.json',
    # Edificaciones
        # Comercial Servicios
            # Acond
    'edificaciones/comercial_servicios/acondicionamiento_espacios_comerciales/supuestos_trayectoria.json',
    # 'edificaciones/comercial_servicios/acondicionamiento_espacios_comerciales/supuestos_fijos.json', # No tiene
    'edificaciones/comercial_servicios/acondicionamiento_espacios_comerciales/salidas.json',
    'edificaciones/comercial_servicios/acondicionamiento_espacios_comerciales/emisiones.json',
            # Usos
    'edificaciones/comercial_servicios/usos_termicos_equipamiento/supuestos_trayectoria.json',
    'edificaciones/comercial_servicios/usos_termicos_equipamiento/supuestos_fijos.json',
    'edificaciones/comercial_servicios/usos_termicos_equipamiento/salidas.json',
    'edificaciones/comercial_servicios/usos_termicos_equipamiento/emisiones.json',
        # Residencial
            # Acond
    'edificaciones/residencial/acondicionamiento_espacios_residenciales/supuestos_trayectoria.json',
    'edificaciones/residencial/acondicionamiento_espacios_residenciales/supuestos_fijos.json',
    'edificaciones/residencial/acondicionamiento_espacios_residenciales/salidas.json',
    'edificaciones/residencial/acondicionamiento_espacios_residenciales/emisiones.json',
            # Ilum
    'edificaciones/residencial/iluminacion_refrigeracion_coccion_otros/supuestos_trayectoria.json',
    'edificaciones/residencial/iluminacion_refrigeracion_coccion_otros/supuestos_fijos.json',
    'edificaciones/residencial/iluminacion_refrigeracion_coccion_otros/salidas.json',
    'edificaciones/residencial/iluminacion_refrigeracion_coccion_otros/emisiones.json',
            # Rural
    'edificaciones/residencial/residencial_rural/supuestos_trayectoria.json',
    'edificaciones/residencial/residencial_rural/supuestos_fijos.json',
    'edificaciones/residencial/residencial_rural/salidas.json',
    'edificaciones/residencial/residencial_rural/emisiones.json',
    # Electricidad
        # Autogeneracion
    'electricidad/autogeneracion/salidas.json',
        # Electricidad
    'electricidad/electricidad/supuestos_trayectoria.json',
    'electricidad/electricidad/supuestos_fijos.json',
    'electricidad/electricidad/salidas.json',
    'electricidad/electricidad/emisiones.json',
    # Energia
        # combustibles_fosiles
    'energia/combustibles_fosiles/supuestos_trayectoria.json',
    'energia/combustibles_fosiles/supuestos_fijos.json',
    'energia/combustibles_fosiles/salidas.json',
    'energia/combustibles_fosiles/emisiones.json',
    # Ganaderia
    'ganaderia/supuestos_trayectoria.json',
    'ganaderia/supuestos_fijos.json',
    'ganaderia/salidas.json',
    'ganaderia/emisiones.json',
    # Industria
    'industria/supuestos_trayectoria.json',
    'industria/supuestos_fijos.json',
    'industria/salidas.json',
    'industria/emisiones.json',
    # Residuos
        # Aguas
    'residuos/aguas_residuales/supuestos_trayectoria.json',
    'residuos/aguas_residuales/supuestos_fijos.json',
    'residuos/aguas_residuales/salidas.json',
    'residuos/aguas_residuales/emisiones.json',
        # Solidos
    'residuos/residuos_solidos/supuestos_trayectoria.json',
    'residuos/residuos_solidos/supuestos_fijos.json',
    'residuos/residuos_solidos/salidas.json',
    'residuos/residuos_solidos/emisiones.json',
    # Transporte
        # Internacional
            # Aviacion
    'transporte/internacional/aviacion/supuestos_trayectoria.json',
    'transporte/internacional/aviacion/supuestos_fijos.json',
    'transporte/internacional/aviacion/salidas.json',
    'transporte/internacional/aviacion/emisiones.json',
            # Navegacion
    'transporte/internacional/navegacion/supuestos_trayectoria.json',
    # 'transporte/internacional/navegacion/supuestos_fijos.json', # No tiene
    'transporte/internacional/navegacion/salidas.json',
    'transporte/internacional/navegacion/emisiones.json',
        # Nacional
            # Carga
    'transporte/nacional/transporte_carga/supuestos_trayectoria.json',
    'transporte/nacional/transporte_carga/supuestos_fijos.json',
    'transporte/nacional/transporte_carga/salidas.json',
    'transporte/nacional/transporte_carga/emisiones.json',
            # Pasajeros
    'transporte/nacional/transporte_pasajeros/supuestos_trayectoria.json',
    'transporte/nacional/transporte_pasajeros/supuestos_fijos.json',
    'transporte/nacional/transporte_pasajeros/salidas.json',
    'transporte/nacional/transporte_pasajeros/emisiones.json',
            
    # Resultados
    'resultados/agricultura.json',
    'resultados/bosques.json',
    'resultados/edificaciones.json',
    'resultados/electricidad.json',
    'resultados/energia.json',
    'resultados/ganaderia.json',
    'resultados/general.json',
    'resultados/industria.json',
    'resultados/residuos.json',
    'resultados/transporte.json'
    ]


if __name__ == "__main__":
    
    print('###############################')
    
    load_dotenv()
    
    DATA_PATH = 'app/data'
    
    HOST = f'http://{os.getenv("DOMAIN")}'
    URL = f'{HOST}{os.getenv("API_V1_STR")}'
    
    print(URL)
    
    for i in range(30):
        try:
            r = httpx.get(url=HOST, timeout=5)
            if r.status_code == 200:
                break
        except httpx.TimeoutException as e:
            print('ping: ', i)
        except httpx.ConnectError as e:
            print(e)
            time.sleep(1)
            continue
            
    
    auth_header = get_auth_header(
        user = os.getenv('FIRST_SUPERUSER'),
        password = os.getenv('FIRST_SUPERUSER_PASSWORD')
        )
    
    for file in rutas:
        path = pathlib.Path(DATA_PATH) / file
        aux = str(path).split(DATA_PATH)[1]
        uri = aux.split('.')[0]
        
        delete(uri=uri, headers=auth_header)
        post(uri=uri, headers=auth_header)
        get(uri=uri, headers=auth_header)
        
    