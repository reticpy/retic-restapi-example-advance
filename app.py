# app.py

"""Main app"""

# Retic
from retic import App as app

# Settings
import settings

# Apps
from apps import urls

# Routes
from routes import router

# Agregar las rutas a la aplicación
app.use(router)

if __name__ == "__main__":
    # Create web server
    app.listen(
        # Obtener la variable de entorno APP_HOSTNAME en el formato por defecto (str)
        hostname=app.env("APP_HOSTNAME"),
        # Obtener la variable de entorno APP_PORT en formato númerico. De no existir, retorna 1801.
        port=app.env.int("APP_PORT", app.config.get("default_port"))
    )