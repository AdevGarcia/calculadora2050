from fastapi import APIRouter

# from api.endpoints import login
from api.endpoints import utils
from modules.excel import download_excel

# Agricultura
from modules.agricultura import endpoints as agricultura

# Bosques
from modules.bosques import endpoints as bosques

# Edificaciones
from modules.edificaciones.comercial.acondicionamiento_espacios_comerciales import endpoints as acec  # noqa
from modules.edificaciones.comercial.usos_termicos_y_equipamiento import endpoints as uste  # noqa
from modules.edificaciones.residencial.acondicionamiento_espacios_residenciales import endpoints as acer  # noqa
from modules.edificaciones.residencial.iluminacion_refrigeracion_coccion_y_otros import endpoints as ilrco  # noqa
from modules.edificaciones.residencial.residencial_rural import endpoints as rural  # noqa

# Electricidad
from modules.electricidad.autogeneracion import endpoints as autogeneracion  # noqa
from modules.electricidad.electricidad import endpoints as electricidad  # noqa
from modules.electricidad.requerimientos_excedentes import endpoints as elie  # noqa

# Energia
from modules.energia.bioenergia import endpoints as bioenergia  # noqa
from modules.energia.combustibles_fosiles import endpoints as fosiles  # noqa
from modules.energia.requerimientos_excedentes import endpoints as enie  # noqa

# Ganaderia
from modules.ganaderia import endpoints as ganaderia  # noqa

# Industria
from modules.industria import endpoints as industria  # noqa

# Residuos
from modules.residuos.aguas_residuales import endpoints as aguas  # noqa
from modules.residuos.residuos_solidos import endpoints as solidos  # noqa

# Transporte
from modules.transporte.internacional.aviacion import endpoints as aviacion  # noqa
from modules.transporte.internacional.navegacion import endpoints as navegacion  # noqa
from modules.transporte.nacional.transporte_carga import endpoints as carga  # noqa
from modules.transporte.nacional.transporte_pasajeros import endpoints as pasajeros  # noqa

# Entradas
from modules.entradas import endpoint_ener_combfosil as entrada_ener_combfosil  # noqa
from modules.entradas import endpoint_ener_bioener as entrada_ener_bioener  # noqa
from modules.entradas import endpoint_ener_import_export as entrada_ener_import_export  # noqa
from modules.entradas import endpoint_elect_electricidad as entrada_elect_electricidad  # noqa
from modules.entradas import endpoint_elect_autogen as entrada_elect_autogen  # noqa
from modules.entradas import endpoint_elect_import_export as entrada_elect_import_export  # noqa
from modules.entradas import endpoint_ind as entrada_ind  # noqa

# # Resultados
# from modules.resultados.agricultura import endpoints as agricultura_result  # noqa
# from modules.resultados.bosques import endpoints as bosques_result  # noqa
# from modules.resultados.edificaciones import endpoints as edificaciones_result  # noqa
# from modules.resultados.electricidad import endpoints as electricidad_result  # noqa
# from modules.resultados.energia import endpoints as energia_result  # noqa
# from modules.resultados.ganaderia import endpoints as ganaderia_result  # noqa
# from modules.resultados.general import endpoints as general_result  # noqa
# from modules.resultados.industria import endpoints as industria_result  # noqa
# from modules.resultados.residuos import endpoints as residuos_result  # noqa
# from modules.resultados.transporte import endpoints as transporte_result  # noqa


api_router = APIRouter()
# api_router.include_router(login.router, tags=["login"])
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(utils.router, tags=["test"])

api_router.include_router(download_excel.router, prefix="/download", tags=["Download Excel"])

# Entradas
api_router.include_router(entrada_ener_combfosil.router, prefix="/entradas/energia", tags=["Entradas"])
api_router.include_router(entrada_ener_bioener.router, prefix="/entradas/energia", tags=["Entradas"])
api_router.include_router(entrada_ener_import_export.router, prefix="/entradas/energia", tags=["Entradas"]) 
api_router.include_router(entrada_elect_electricidad.router, prefix="/entradas/electricidad", tags=["Entradas"]) 
api_router.include_router(entrada_elect_autogen.router, prefix="/entradas/electricidad", tags=["Entradas"])
api_router.include_router(entrada_elect_import_export.router, prefix="/entradas/electricidad", tags=["Entradas"])
api_router.include_router(entrada_ind.router, prefix="/entradas/industria", tags=["Entradas"])

# Resultados
# api_router.include_router(general_result.router, prefix="/resultados", tags=["Resultados"])
# api_router.include_router(agricultura_result.router, prefix="/resultados", tags=["Resultados"])
# api_router.include_router(bosques_result.router, prefix="/resultados", tags=["Resultados"])
# api_router.include_router(edificaciones_result.router, prefix="/resultados", tags=["Resultados"])
# api_router.include_router(electricidad_result.router, prefix="/resultados", tags=["Resultados"])
# api_router.include_router(energia_result.router, prefix="/resultados", tags=["Resultados"])
# api_router.include_router(ganaderia_result.router, prefix="/resultados", tags=["Resultados"])
# api_router.include_router(industria_result.router, prefix="/resultados", tags=["Resultados"])
# api_router.include_router(residuos_result.router, prefix="/resultados", tags=["Resultados"])
# api_router.include_router(transporte_result.router, prefix="/resultados", tags=["Resultados"])


### Modules of sectors ###

# Agricultura
api_router.include_router(
    router=agricultura.router, 
    prefix="/agricultura", 
    tags=["Agricultura"]
)


# Bosques
api_router.include_router(
    router=bosques.router, 
    prefix="/bosques", 
    tags=["Bosques"]
)


# Edificaciones
# Edificaciones Residenciales
api_router.include_router(
    router=acer.router,
    prefix="/edificaciones/residencial/acondicionamiento_espacios_residenciales",
    tags=["Edificaciones Residencial"]
)
api_router.include_router(
    router=ilrco.router, 
    prefix="/edificaciones/residencial/iluminacion_refrigeracion_coccion_otros", 
    tags=["Edificaciones Residencial"]
)
api_router.include_router(
    rural.router, 
    prefix="/edificaciones/residencial/residencial_rural", 
    tags=["Edificaciones Residencial"]
)


# Edificaciones Comerciales y de Servicios
api_router.include_router(
    router=acec.router, 
    prefix="/edificaciones/comercial_servicios/acondicionamiento_espacios_comerciales", 
    tags=["Edificaciones Comercial y Servicios"]
)
api_router.include_router(
    router=uste.router, 
    prefix="/edificaciones/comercial_servicios/usos_termicos_equipamiento", 
    tags=["Edificaciones Comercial y Servicios"]
)


# Electricidad
api_router.include_router(
    router=electricidad.router, 
    prefix="/electricidad/electricidad", 
    tags=["Electricidad"]
)
# api_router.include_router(
#     router=autogeneracion.router,
#     prefix="/electricidad/autogeneracion", 
#     tags=["Electricidad"]
# )
# api_router.include_router(
#     router=elie.router, 
#     prefix="/electricidad/importaciones_exportaciones", 
#     tags=["Electricidad"]
# )


# Energia
api_router.include_router(
    router=fosiles.router, 
    prefix="/energia/combustibles_fosiles", 
    tags=["Energia"]
)
# api_router.include_router(
#     router=bioenergia.router, 
#     prefix="/energia/bioenergia", 
#     tags=["Energia"]
# )
# api_router.include_router(
#     router=enie.router, 
#     prefix="/energia/importaciones_exportaciones", 
#     tags=["Energia"]
# )


# Ganaderia
api_router.include_router(
    router=ganaderia.router, 
    prefix="/ganaderia", 
    tags=["Ganaderia"]
)


# Industria
api_router.include_router(
    router=industria.router, 
    prefix="/industria", 
    tags=["Industria"]
)


# Residuos
api_router.include_router(
    router=solidos.router, 
    prefix="/residuos/residuos_solidos", 
    tags=["Residuos Solidos"]
)
api_router.include_router(
    router=aguas.router, 
    prefix="/residuos/aguas_residuales", 
    tags=["Residuos Aguas"]
)


# Transporte
# Transporte Nacional
api_router.include_router(
    router=carga.router, 
    prefix="/transporte/nacional/transporte_carga", 
    tags=["Transporte Nacional"]
)
api_router.include_router(
    router=pasajeros.router, 
    prefix="/transporte/nacional/transporte_pasajeros", 
    tags=["Transporte Nacional"]
)
# # Transporte Internacional
api_router.include_router(
    router=aviacion.router, 
    prefix="/transporte/internacional/aviacion", 
    tags=["Transporte Internacional"]
)
api_router.include_router(
    router=navegacion.router, 
    prefix="/transporte/internacional/navegacion", 
    tags=["Transporte Internacional"]
)
