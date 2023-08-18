
SECTORES = ['agricultura', 'bosques', 'ganaderia', 'industria', 'residuos', 'edificaciones', 'transporte', 'electricidad', 'energia']

FOLDER_PATH = [
    'app/data/agricultura/',
    'app/data/bosques/',
    'app/data/edificaciones/comercial_y_servicios/acondicionamiento_espacios_comerciales/',
    'app/data/edificaciones/comercial_y_servicios/usos_termicos_y_equipamiento/',
    'app/data/edificaciones/residencial/acondicionamiento_espacios_residenciales/',
    'app/data/edificaciones/residencial/iluminacion_refrigeracion_coccion_y_otros/',
    'app/data/edificaciones/residencial/residencial_rural/',
    'app/data/electricidad/electricidad/',
    # 'app/data/electricidad/autogeneracion/',
    # 'app/data/electricidad/requerimientos_excedentes/',
    'app/data/energia/combustibles_fosiles/',
    # 'app/data/energia/bioenergia/',
    # 'app/data/energia/requerimientos_excedentes/',
    'app/data/ganaderia/',
    'app/data/industria/',
    'app/data/residuos/aguas_residuales/',
    'app/data/residuos/residuos_solidos/',
    'app/data/transporte/internacional/aviacion/',
    'app/data/transporte/internacional/navegacion/',
    'app/data/transporte/nacional/carga/',
    'app/data/transporte/nacional/pasajeros/'
]

INDICE = {
    'agricultura':[{
        'sector'    : 'agricultura',
        'subsector' : 'agricultura',
        'clase'     : '-',
        'tipo'      : ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'salidas', 'emisiones', 'metodologia'],
        'tipo_files': ['supuestos_trayectoria', 'supuestos_fijos', 'salida_biocombustibles', 'salida_cultivos', 'emisiones', 'metodologia']

    }],
    'bosques' :[{
        'sector'    : 'bosques',
        'subsector' : 'bosques',
        'clase'     : '-',
        'tipo'      : ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'emisiones'],
        'tipo_files': ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'emisiones']
    }], 
    'ganaderia' :[{
        'sector'    : 'ganaderia',
        'subsector' : 'ganaderia',
        'clase'     : '-',
        'tipo'      : ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'emisiones'],
        'tipo_files': ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'emisiones']
    }], 
    'industria' :[{
        'sector'    : 'industria',
        'subsector' : 'industria',
        'clase'     : '-',
        'tipo'      : ['supuestos_trayectoria', 'supuestos_fijos', 
                       'salidas', 
                       'salidas', 
                       'salidas', 
                       'salidas', 
                       'salidas', 
                       'salidas', 
                       'emisiones',
                       'emisiones',
                       'emisiones'],
        'tipo_files': ['supuestos_trayectoria', 'supuestos_fijos', 
                       'salida_balance_total_de_la_energia_requerida_combustible',
                       'salida_balance_total_de_la_energia_requerida_industria',
                       'salida_energia_producida_por_autogeneracion_y_cogeneracion_combustible',
                       'salida_energia_producida_por_autogeneracion_y_cogeneracion_industria',
                       'salida_energia_requerida_combustible',
                       'salida_energia_requerida_industria',
                       'emisiones_gases_efecto_invernadero',
                       'emisiones_por_el_consumo_de_bagazo_y_otros', 
                       'emisiones_sao']
    }], 
    'residuos' :[
        {
            'sector'    : 'residuos',
            'subsector' : 'aguas_residuales',
            'clase'     : '-',
            'tipo'      : ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'salidas', 'emisiones'],
            'tipo_files': ['supuestos_trayectoria', 'supuestos_fijos', 'salida_energia_consumida', 'salida_energia_producida', 'emisiones']
        },
        {
            'sector'    : 'residuos',
            'subsector' : 'residuos_solidos',
            'clase'     : '-',
            'tipo'      : ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'salidas', 'emisiones'],
            'tipo_files': ['supuestos_trayectoria', 'supuestos_fijos', 'salida_energia_consumida', 'salida_energia_producida', 'emisiones']
        },
    ], 
    'edificaciones' :[
        {
            'sector'    : 'edificaciones',
            'subsector' : 'residencial',
            'clase'     : 'acondicionamiento_espacios_residenciales',
            'tipo'      : ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'emisiones'],
            'tipo_files': ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'emisiones']
        },
        {
            'sector'    : 'edificaciones',
            'subsector' : 'residencial',
            'clase'     : 'iluminacion_refrigeracion_coccion_y_otros',
            'tipo'      : ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'emisiones', 'metodologia'],
            'tipo_files': ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'emisiones', 'metodologia']
        },
        {
            'sector'    : 'edificaciones',
            'subsector' : 'residencial',
            'clase'     : 'residencial_rural',
            'tipo'      : ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'emisiones'],
            'tipo_files': ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'emisiones']
        },
        {
            'sector'    : 'edificaciones',
            'subsector' : 'comercial_y_servicios',
            'clase'     : 'acondicionamiento_espacios_comerciales',
            'tipo'      : ['supuestos_trayectoria', 'salidas', 'emisiones'],
            'tipo_files': ['supuestos_trayectoria', 'salidas', 'emisiones']
        },
        {
            'sector'    : 'edificaciones',
            'subsector' : 'comercial_y_servicios',
            'clase'     : 'usos_termicos_y_equipamiento',
            'tipo'      : ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'emisiones'],
            'tipo_files': ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'emisiones']
        }
    ],  
    'transporte' :[
        {
            'sector'    : 'transporte',
            'subsector' : 'nacional',
            'clase'     : 'pasajeros',
            'tipo'      : ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'emisiones'],
            'tipo_files': ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'emisiones']
        },
        {
            'sector'    : 'transporte',
            'subsector' : 'nacional',
            'clase'     : 'carga',
            'tipo'      : ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'emisiones'],
            'tipo_files': ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'emisiones']
        },
        {
            'sector'    : 'transporte',
            'subsector' : 'internacional',
            'clase'     : 'aviacion',
            'tipo'      : ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'emisiones'],
            'tipo_files': ['supuestos_trayectoria', 'supuestos_fijos', 'salidas', 'emisiones']
        },
        {
            'sector'    : 'transporte',
            'subsector' : 'internacional',
            'clase'     : 'navegacion',
            'tipo'      : ['supuestos_trayectoria', 'salidas', 'emisiones'],
            'tipo_files': ['supuestos_trayectoria', 'salidas', 'emisiones']
        }
    ],  
    'electricidad' :[
        {
            'sector'    : 'electricidad',
            'subsector' : 'electricidad',
            'clase'     : '-',
            'tipo'      : ['supuestos_trayectoria', 
                           'supuestos_fijos', 
                           'salidas', 
                           'salidas',
                           'salidas',
                           'salidas',
                           'emisiones',
                           'emisiones'],
            'tipo_files': ['supuestos_trayectoria', 
                           'supuestos_fijos', 
                           'salidas_balance', 
                           'salidas_combustibles_fosiles',
                           'salidas_energias_renovables_no_convencionales',
                           'salidas_energia_demandada',
                           'emisiones_combustibles_fosiles',
                           'emisiones_energias_renovables_no_convencionales']
        }
    ], 
    'energia' :[
        {
            'sector'    : 'energia',
            'subsector' : 'combustibles_fosiles',
            'clase'     : '-',
            'tipo'      : ['supuestos_trayectoria', 'supuestos_fijos', 
                           'salidas', 
                           'salidas', 
                           'salidas', 
                           'emisiones',
                           'emisiones'],
            'tipo_files': ['supuestos_trayectoria', 'supuestos_fijos', 
                           'salidas_combustibles_fosiles_producidos',
                           'salidas_consumo_de_combustibles_fosiles_por_el_propio_sector',
                           'salidas_consumo_de_combustibles_fosiles_por_sectores_ajenos',
                           'emisiones_consumo', 
                           'emisiones_produccion']
        }
    ], 
}
