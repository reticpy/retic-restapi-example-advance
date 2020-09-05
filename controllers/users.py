# controllers/users.py

# Retic
from retic import Request, Response, Next

# Services
from services.users import users


def get_by_id(req: Request, res: Response, next: Next):
    """Obtener un usuario por su identificador"""

    user = users.get_by_id_db(req.param("id", callback=int))

    """Transformar información de respuesta"""
    if user:
        """Retornar una respuesta al cliente"""
        res.ok({
            u"valid": True,
            u"msg": "Usuario encontrado.",
            u"data": user
        })
    else:
        """Retornar un mensaje de error al cliente"""
        res.not_found({
            u"valid": False,
            u"msg": "Usuario no encontrado."
        })
