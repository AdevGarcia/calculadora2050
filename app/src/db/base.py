# Import all the models, so that Base has them before being
# imported by Alembic
from app.src.db.base_class import Base  # noqa

# Users
from app.src.modules.user.models import *  # noqa

# Agricultura
from app.src.modules.agricultura.models import *  # noqa

# Bosques
from app.src.modules.bosques.models import *  # noqa

# Edificaciones
from app.src.modules.edificaciones.comercial.acondicionamiento_espacios_comerciales.models import *  # noqa
from app.src.modules.edificaciones.comercial.usos_termicos_y_equipamiento.models import *  # noqa
from app.src.modules.edificaciones.residencial.acondicionamiento_espacios_residenciales.models import *  # noqa
from app.src.modules.edificaciones.residencial.iluminacion_refrigeracion_coccion_y_otros.models import *  # noqa
from app.src.modules.edificaciones.residencial.residencial_rural.models import *  # noqa

# # Electricidad
# from app.src.modules.electricidad.autogeneracion.models import *  # noqa
# from app.src.modules.electricidad.electricidad.models import *  # noqa
# from app.src.modules.electricidad.importaciones_exportaciones.models import *  # noqa

# # Energia
# from app.src.modules.energia.bioenergia.models import *  # noqa
# from app.src.modules.energia.combustibles_fosiles.models import *  # noqa
# from app.src.modules.energia.importaciones_exportaciones.models import *  # noqa

# Ganaderia
from app.src.modules.ganaderia.models import *  # noqa

# Industria
from app.src.modules.industria.models import *  # noqa

# Residuos
from app.src.modules.residuos.aguas_residuales.models import *  # noqa
from app.src.modules.residuos.residuos_solidos.models import *  # noqa

# Transporte
from app.src.modules.transporte.internacional.aviacion.models import *  # noqa
from app.src.modules.transporte.internacional.navegacion.models import *  # noqa
from app.src.modules.transporte.nacional.transporte_carga.models import *  # noqa
from app.src.modules.transporte.nacional.transporte_pasajeros.models import *  # noqa

# # Resultados
# from app.src.modules.resultados.agricultura.models import *  # noqa
# from app.src.modules.resultados.bosques.models import *  # noqa
# from app.src.modules.resultados.edificaciones.models import *  # noqa
# from app.src.modules.resultados.electricidad.models import *  # noqa
# from app.src.modules.resultados.energia.models import *  # noqa
# from app.src.modules.resultados.ganaderia.models import *  # noqa
# from app.src.modules.resultados.general.models import *  # noqa
# from app.src.modules.resultados.industria.models import *  # noqa
# from app.src.modules.resultados.residuos.models import *  # noqa
# from app.src.modules.resultados.transporte.models import *  # noqa
