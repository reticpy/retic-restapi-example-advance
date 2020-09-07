# settings.py

# Retic
from retic import App as app

"""Asignar ruta de variables de entorno"""
app.env.read_env('.env.development', override=True)

"""Crear diccionario de congfiguración"""
config = {
    u"default_port": 1801
}

"""Configuración basada en un objeto"""
app.config.from_object(config)

"""Eliminar variables de configuración"""
app.config.clear()

"""Asignar variables de configuración"""
app.config.set("default_port", 1801)